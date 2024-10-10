CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so libmanhattan.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libmanhattan.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/manhattan.c

clean:
	rm -f *.so
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
