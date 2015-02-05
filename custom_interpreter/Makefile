PYTHON_DIR := Python-2.7.9
PYTHON_CUSTOM_DIR := $(PYTHON_DIR)-customized
PYTHON_XZ := Python-2.7.9.tar.xz

all: pyenv
	@ cp -R ../app .
	@ pip install -r app/requirements.txt

clean:
	@ rm -rf app $(PYTHON_DIR) $(PYTHON_CUSTOM_DIR) *.diff

$(PYTHON_XZ):
	@ wget -c https://www.python.org/ftp/python/2.7.9/Python-2.7.9.tar.xz

$(PYTHON_DIR): $(PYTHON_XZ)
	@ tar xJf Python-2.7.9.tar.xz

$(PYTHON_CUSTOM_DIR): $(PYTHON_DIR)
	@ cp -R $(PYTHON_DIR) $(PYTHON_CUSTOM_DIR)

# Do "diff .. || true" because diff exits status is based on if there
# are differences between the files or not (like cmp)
scramble: $(PYTHON_CUSTOM_DIR)
	@ python scramble-opcodes.py --python-source=$(PYTHON_CUSTOM_DIR)
	@ diff -u $(PYTHON_DIR)/Include/opcode.h $(PYTHON_CUSTOM_DIR)/Include/opcode.h \
		> scrambled-opcodes.diff || true

pyenv: scramble
	@ cat scrambled-opcodes.diff | filterdiff --strip=1 | pyenv install -sp 2.7.9-custom
	@ pyenv local 2.7.9-custom

run: clean $(PYTHON_CUSTOM_DIR) scramble

.DEFAULT: all
.PHONY: all clean clean-build run
