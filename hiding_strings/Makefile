INPUT_DIR := ../app
OUTPUT_DIR := ./app

all: encode

encode: copy
	@ python encode.py $(OUTPUT_DIR)

copy: clean
	@ cp -R $(INPUT_DIR) $(OUTPUT_DIR)

clean:
	@ rm -rf $(OUTPUT_DIR)

.DEFAULT: all
.PHONY: encode copy clean
