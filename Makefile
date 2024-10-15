CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: librdp.so libeuclidean.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

librdp.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/rdp.c	

clean:
	rm -f *.so
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
