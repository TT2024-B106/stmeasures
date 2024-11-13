# stmeasures/abstractions/geojson.py

class GeoJSON:
    """
    Represents a GeoJSON data structure for storing trajectories.

    This class is used to load, store, and process GeoJSON data representing multiple 
    trajectories. It can extract relevant features like the trajectory coordinates, 
    IDs, and timestamps from raw GeoJSON data.

    :param data: Raw GeoJSON data in a list format, where each item contains features with 
                 geometry and properties related to the trajectory.
    :type data: list[dict]
    """

    def __init__(self, data):
        """
        Initializes the GeoJSON object with the provided data and extracts trajectories.

        :param data: Raw GeoJSON data to be processed into trajectory data.
        :type data: list[dict]
        """
        self.data = data
        self.trajectories = self._extract_trajectories()

    def _extract_trajectories(self):
        """
        Extracts trajectories from the raw GeoJSON data.

        This method scans through the GeoJSON data, looking for features with 
        geometry type 'LineString'. For each such feature, it extracts the 
        coordinates, trajectory ID, and timestamp, and stores them in a list.

        :return: A list of trajectories, each represented by a dictionary containing 
                 its 'id', 'timestamp', and 'coordinates'.
        :rtype: list[dict]
        """
        trajectories = []
        for item in self.data:
            features = item.get('features', [])
            for feature in features:
                if feature['geometry']['type'] == 'LineString':
                    coordinates = feature['geometry']['coordinates']
                    trajectories.append({
                        'id': feature['properties'].get('name'),
                        'timestamp': feature['properties'].get('tiempo'),
                        'coordinates': coordinates
                    })
        return trajectories

    # TODO: Add algorithms to work with
    # def find_similar(self, trajectory, trajectories):
    #     """
    #     Finds the top 5 trajectories similar to a given trajectory using Euclidean distance.

    #     This method compares the specified trajectory to each trajectory in the provided 
    #     list of trajectories and returns the top 5 most similar ones, based on the 
    #     Euclidean distance between their coordinates.

    #     :param trajectory: The trajectory to compare.
    #     :type trajectory: dict
    #     :param trajectories: List of trajectories to compare against.
    #     :type trajectories: list of dicts
    #     :return: List of top 5 most similar trajectories, sorted by their Euclidean 
    #              distance to the input trajectory.
    #     :rtype: list of dicts
    #     """
    #     similar_trajectories = []

    #     # Iterate over each trajectory in the list
    #     for traj in trajectories:
    #         # Calculate Euclidean distance between `trajectory` and `traj`
    #         distance = euclidean.Euclidean.distance(trajectory.coordinates, traj.coordinates)

    #         # Append each trajectory with its distance
    #         similar_trajectories.append((distance, traj))

    #     # Sort by distance in ascending order
    #     similar_trajectories.sort(key=lambda x: x[0])

    #     # Select the top 5 closest trajectories
    #     top_5_similar = similar_trajectories[:5]

    #     # Return only the trajec
