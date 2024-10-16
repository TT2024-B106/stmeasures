CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
POSFLAGS = -O -g
OBJFLAGS = -c -o

# Object files
OBJ_FILES = euclidean.pic.o hausdorff.pic.o frechet.pic.o dtw.pic.o

# Targets for shared libraries
all: libeuclidean.so libhausdorff.so libfrechet.so libdtw.so

libeuclidean.so: src/euclidean.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

libhausdorff.so: src/hausdorff.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

libfrechet.so: src/frechet.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

libdtw.so: src/dtw.c
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ $<

# Rule for building object files if needed
%.pic.o: src/%.c
	$(CC) $(CFLAGS) $(POSFLAGS) $(OBJFLAGS) $< $@

clean:
	rm -f *.so *.o
	[ -e "dist" ] && rm -r dist || :
	[ -e "stmeasures-clib" ] && rm -r stmeasures-clib || :
