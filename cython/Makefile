PYTHONLIB := /usr/include/python2.7
CFLAGS := -shared -pthread -fPIC -fwrapv -O2 -Wall -fno-strict-aliasing -I${PYTHONLIB}
PYTHON_FILES := $(shell find . -name "*.py" ! -name "__init__.py" ! -name "manage.py")
OBJECTS := $(patsubst %.py,%.so,$(PYTHON_FILES))

all: $(OBJECTS)

%.c: %.py
	@ echo "Compiling $<"
	@ cython --no-docstrings $< -o $(patsubst %.py,%.c,$<)

%.so: %.c
	@ $(CC) $(CFLAGS) -o $@ $<

clean-py:
	@ find . ! -name "__init__.py" ! -name "manage.py" -name "*.py" -delete
	@ find . -name "__init__.so" -o -name "manage.so" -delete

clean:
	@ find . -name "*.so" -delete

.DEFAULT: all
.PHONY: all %.c %.so clean clean-py
