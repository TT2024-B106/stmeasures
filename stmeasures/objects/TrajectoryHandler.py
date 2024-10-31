import folium
import numpy as np
import matplotlib.pyplot as plt
from typing import List, Tuple, Union
from stmeasures.objects.cstructures import Trajectory, Point
import ctypes

class TrajectoryHandler:
    """
    A class for visualizing multiple geographical trajectories.
    
    This class provides methods to plot trajectories using both Folium (for interactive maps)
    and Matplotlib (for static visualizations).
    """
    
    def __init__(self):
        """Initialize the TrajectoryHandler."""
        self.colors = [
            'red', 'blue', 'green', 'purple', 'orange', 
            'darkred', 'lightblue', 'darkgreen', 'cadetblue', 'darkpurple'
        ]
    
    def create_trajectory(self, coordinates):
       """
       Helper function to create a Trajectory object from a list of coordinates.
       """
       size = len(coordinates)
       points_array = (Point * size)()
    
       for i, (lat, lon) in enumerate(coordinates):
          points_array[i] = Point(lat, lon)
    
       trajectory = Trajectory()
       trajectory.points = ctypes.cast(points_array, ctypes.POINTER(Point))
       trajectory.size = size

       return trajectory
    
    def _convert_trajectory_to_points(self, trajectory: Trajectory) -> List[Tuple[float, float]]:
        """
        Convert a Trajectory structure to a list of (latitude, longitude) tuples.
        
        Parameters
        ----------
        trajectory : Trajectory
            A trajectory structure containing points
            
        Returns
        -------
        List[Tuple[float, float]]
            List of (latitude, longitude) coordinates
        """
        points = []
        for i in range(trajectory.size):
            point = trajectory.points[i]
            points.append((point.latitude, point.longitude))
        return points
    
    def plot_folium(self, 
                   trajectories: List[Union[Trajectory, List[Tuple[float, float]]]], 
                   labels: List[str] = None,
                   zoom_start: int = 10) -> folium.Map:
        """
        Create an interactive map with multiple trajectories using Folium.
        
        Parameters
        ----------
        trajectories : List[Union[Trajectory, List[Tuple[float, float]]]]
            List of trajectories to plot
        labels : List[str], optional
            Labels for each trajectory
        zoom_start : int, optional
            Initial zoom level for the map
            
        Returns
        -------
        folium.Map
            Interactive map with plotted trajectories
        """
        if not trajectories:
            raise ValueError("No trajectories provided")
            
        processed_trajectories = []
        all_lats = []
        all_lons = []
        
        for traj in trajectories:
            if isinstance(traj, Trajectory):
                points = self._convert_trajectory_to_points(traj)
            else:
                points = traj
                
            processed_trajectories.append(points)
            lats, lons = zip(*points)
            all_lats.extend(lats)
            all_lons.extend(lons)
        
        center_lat = np.mean(all_lats)
        center_lon = np.mean(all_lons)
        
        m = folium.Map(location=[center_lat, center_lon], zoom_start=zoom_start)
        
        for idx, points in enumerate(processed_trajectories):
            color = self.colors[idx % len(self.colors)]
            label = labels[idx] if labels and idx < len(labels) else f"Trajectory {idx + 1}"
            
            for lat, lon in points:
                folium.CircleMarker(
                    [lat, lon],
                    radius=3,
                    color=color,
                    fill=True,
                    popup=f"{label}: ({lat:.4f}, {lon:.4f})"
                ).add_to(m)
            
            folium.PolyLine(
                points,
                weight=2,
                color=color,
                opacity=0.8,
                popup=label
            ).add_to(m)
        
        return m
    
    def plot_matplotlib(self, 
                       trajectories: List[Union[Trajectory, List[Tuple[float, float]]]], 
                       labels: List[str] = None,
                       figsize: Tuple[int, int] = (10, 8),
                       show_points: bool = True) -> None:
        """
        Create a static plot of multiple trajectories using Matplotlib.
        
        Parameters
        ----------
        trajectories : List[Union[Trajectory, List[Tuple[float, float]]]]
            List of trajectories to plot
        labels : List[str], optional
            Labels for each trajectory
        figsize : Tuple[int, int], optional
            Size of the figure
        show_points : bool, optional
            Whether to show individual points
        """
        if not trajectories:
            raise ValueError("No trajectories provided")
        
        plt.figure(figsize=figsize)
        
        for idx, traj in enumerate(trajectories):
            if isinstance(traj, Trajectory):
                points = self._convert_trajectory_to_points(traj)
            else:
                points = traj
                
            lats, lons = zip(*points)
            color = self.colors[idx % len(self.colors)]
            label = labels[idx] if labels and idx < len(labels) else f"Trajectory {idx + 1}"
            
            plt.plot(lons, lats, color=color, label=label)
            
            if show_points:
                plt.scatter(lons, lats, color=color, s=30, alpha=0.5)
        
        plt.grid(True, linestyle='--', alpha=0.7)
        plt.legend()
        plt.xlabel('Longitude')
        plt.ylabel('Latitude')
        plt.title('Trajectory Comparison')
        plt.show()
