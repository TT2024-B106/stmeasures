CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libmanhattan.so libeditdist.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.c
	$(CC) $(CFLAGS) $(POSFLAGS) src/manhattan.c $(OBJFLAGS) manhattan.pic.o

libeditdist.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/edit_distance.c $(OBJFLAGS) editdist.pic.o
	$(CC) $(LDFLAGS) manhattan.pic.o editdist.pic.o -o $@

clean:
	rm -f *.so
	rm -f *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
