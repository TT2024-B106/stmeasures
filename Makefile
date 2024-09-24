CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared

all: libeuclidean.so

libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

clean:
	rm -f ./*.so
	rm -f ./*.out
