CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so libfrechet.so

libeuclidean.so: src/euclidean.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libfrechet.so: src/frechet.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c

clean:
	rm -f *.so
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :