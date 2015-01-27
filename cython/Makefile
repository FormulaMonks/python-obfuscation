PYTHONLIB := /usr/include/python2.7
CFLAGS := -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I${PYTHONLIB}
OBJECTS := $(patsubst %.py,%.so,$(wildcard *.py))
SUBDIRS := $$(find . -maxdepth 1 ! -path . -type d | tr "\n" " " | sed -e "s/\.\///g")

all: $(OBJECTS) subdirs

%.c: %.py
	@ echo "Compiling $<"
	@ cython --no-docstrings $< -o $(patsubst %.py,%.c,$<)

%.so: %.c
	@ $(CC) $(CFLAGS) -o $@ $<

subdirs:
	@ for d in $(SUBDIRS); do \
		$(MAKE) -C $$d; \
	done

clean-py:
	@ find . ! -name "__init__.py" ! -name "manage.py" -name "*.py" -delete
	@ find . -name "__init__.so" -o -name "manage.so" -delete

clean:
	@ find . -name "*.so" -delete

.DEFAULT: all
.PHONY: all %.c %.so clean subdirs
