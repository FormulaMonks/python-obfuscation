PYTHONLIB := /usr/include/python2.7
CFLAGS := -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I${PYTHONLIB}

all: ihook.so
	@ python ihook.py app/
	@ cp ihook.so m.py app/

%.c: %.py
	@ echo "Compiling $<"
	@ cython --no-docstrings $< -o $(patsubst %.py,%.c,$<)

%.so: %.c
	@ $(CC) $(CFLAGS) -o $@ $<
	@ strip --strip-all $@

clean-build:
	@ find . -iname "*.py[co]" -delete

clean:
	@ rm -rf ./app

run: clean
	@ cp -R ../app .
	@ find . -name "*.py[co]" -delete
	@ $(MAKE) && $(MAKE) clean-build

.DEFAULT: all
.PHONY: all clean clean-build run
