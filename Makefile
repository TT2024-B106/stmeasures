CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libdtw.so libeuclidean.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libdtw.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/dtw.c src/euclidean.c src/matrix.c
	
clean:
	rm -f *.so
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
