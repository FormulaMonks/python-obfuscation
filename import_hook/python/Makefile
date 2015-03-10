all:
	@ python ihook.py app/
	@ cp ihook.py m.py app/

clean-build:
	@ find . -iname "*.py[co]" -delete

clean:
	@ rm -rf ./app

run: clean
	@ cp -R ../../app .
	@ find . -name "*.py[co]" -delete
	@ $(MAKE) && $(MAKE) clean-build

.DEFAULT: all
.PHONY: all clean clean-build run
