CC = gcc

CFLAGS = -fPIC -Wall
LDFLAGS = -shared
OUT_DIR = stmeasures/calculate

all: $(OUT_DIR)/libeuclidean.so

$(OUT_DIR)/libeuclidean.so:
	$(CC) $(CFLAGS) $(LDFLAGS) -o $@ src/euclidean.c

clean:
	rm -f $(OUT_DIR)/*.so
