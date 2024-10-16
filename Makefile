CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libhausdorff.so libfrechet.so libdtw.so

# Compile Euclidean library
libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

# Compile Hausdorff library using the object file from Euclidean
libhausdorff.so: euclidean.pic.o
	$(CC) $(CFLAGS) $(POSFLAGS) src/hausdorff.c $(OBJFLAGS) hausdorff.pic.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ euclidean.pic.o hausdorff.pic.o

# Compile Frechet library
libfrechet.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c

# Compile DTW library
libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/dtw.c

# Compile Euclidean object file for reuse
euclidean.pic.o:
	$(CC) $(CFLAGS) $(OBJFLAGS) $@ src/euclidean.c

# Clean up
clean:
	rm -f *.so
	rm -f *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
