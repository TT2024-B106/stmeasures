CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libhausdorff.so
all: libeuclidean.so libmanhattan.so libeditdist.so libhausdorff.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.c

libeditdist.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/manhattan.c $(OBJFLAGS) manhattan.pic.o
	$(CC) $(CFLAGS) $(POSFLAGS) src/math_utils.c $(OBJFLAGS) math_utils.pic.o
	$(CC) $(CFLAGS) $(POSFLAGS) src/edit_distance.c $(OBJFLAGS) editdist.pic.o
	$(CC) $(LDFLAGS) manhattan.pic.o math_utils.pic.o editdist.pic.o -o $@

libhausdorff.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/euclidean.c $(OBJFLAGS) euclidean.pic.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/hausdorff.c
	$(CC) $(LDFLAGS) manhattan.pic.o math_utils.pic.o editdist.pic.o -o $@


clean:
	rm -f *.so
	rm -f *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
