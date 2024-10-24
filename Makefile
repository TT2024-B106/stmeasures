CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libmanhattan.so libeditdist.so liblcss.so libfrechet.so libhausdorff.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c
	$(CC) $(CFLAGS) $(POSFLAGS) src/euclidean.c $(OBJFLAGS) euclidean.pic.o

libfrechet.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/frechet.c $(OBJFLAGS) frechet.pic.o
	$(CC) $(LDFLAGS) euclidean.pic.o frechet.pic.o -o $@

libhausdorff.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/hausdorff.c

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.c
	$(CC) $(CFLAGS) $(POSFLAGS) src/manhattan.c $(OBJFLAGS) manhattan.pic.o

libeditdist.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/edit_distance.c $(OBJFLAGS) editdist.pic.o
	$(CC) $(LDFLAGS) manhattan.pic.o editdist.pic.o -o $@

liblcss.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/lcss.c

clean:
	rm -f *.so *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
