CC = gcc
CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

all: libeuclidean.so libfrechet.so

libeuclidean.so:
    $(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

libfrechet.so:
    $(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/frechet.c
    $(CC) $(CFLAGS) $(POSFLAGS) src/frechet.c $(OBJFLAGS) frechet.pic.o

clean:
    rm -f *.so
    rm -f *.oruf
    [ -e "dist" ] && rm -r dist || :
    [ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
