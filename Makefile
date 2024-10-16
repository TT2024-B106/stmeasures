CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libhausdorff.so libfrechet.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libhausdorff.so:
	$(CC) $(CFLAGS) $(POSFLAGS) src/euclidean.c $(OBJFLAGS) euclidean.pic.o
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/hausdorff.c
  
libfrechet.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c

libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/dtw.c

clean:
	rm -f *.so
	rm -f *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
