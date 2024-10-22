CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libfrechet.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c
	$(CC) $(CFLAGS) $(POSFLAGS) src/euclidean.c $(OBJFLAGS) euclidean.pic.o

libfrechet.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/frechet.c $(OBJFLAGS) frechet.pic.o
	$(CC) $(LDFLAGS) euclidean.pic.o frechet.pic.o -o $@

libhausdorff.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/hausdorff.c

clean:
	rm -f *.so *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
