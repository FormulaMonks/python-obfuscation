INPUT_DIR := ../app
OUTPUT_DIR := ./app

all: scramble

scramble: copy
	@ python scramble.py $(OUTPUT_DIR)
	@ cp ihook.py scrambler.py manage.py $(OUTPUT_DIR)

unscramble:
	@ python unscramble.py $(OUTPUT_DIR)

copy: clean
	@ cp -R $(INPUT_DIR) $(OUTPUT_DIR)

clean:
	@ rm -rf $(OUTPUT_DIR)

.DEFAULT: all
.PHONY: unscramble scramble copy clean
