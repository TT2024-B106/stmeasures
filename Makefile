CC = gcc
CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so libfrechet.so

libeuclidean.so:
    $(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libfrechet.so:
    $(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c

clean:
    rm -f *.so
    [ -e "dist" ] && rm -r dist || :
    [ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
