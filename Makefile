CC = gcc

CFLAGS = -fPIC -Wall -O -g
LDFLAGS = -shared
OBJFLAGS = -c -o

# Define object files
EUCLIDEAN_OBJ = euclidean.pic.o
HAUSDORFF_OBJ = hausdorff.pic.o

all: libeuclidean.so libhausdorff.so libfrechet.so libdtw.so

# Compile euclidean.o as a position-independent object
$(EUCLIDEAN_OBJ): src/euclidean.c
	$(CC) $(CFLAGS) $(OBJFLAGS) $@ src/euclidean.c

libeuclidean.so: src/euclidean.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libhausdorff.so: $(EUCLIDEAN_OBJ) src/hausdorff.c
	$(CC) $(CFLAGS) $(OBJFLAGS) $@ src/hausdorff.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $(HAUSDORFF_OBJ) $(EUCLIDEAN_OBJ)

libfrechet.so: src/frechet.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c

libdtw.so: src/dtw.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/dtw.c

clean:
	rm -f *.so *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
