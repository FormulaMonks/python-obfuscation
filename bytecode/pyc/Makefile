all:
	@ python -m compileall app/

clean-build:
	@ find . ! -name "manage.py" -name "*.py" -delete

clean:
	@ rm -rf ./app

run: clean
	@ cp -R ../../app .
	@ find . -iname "*.py[co]" -delete
	@ $(MAKE) && $(MAKE) clean-build

.DEFAULT: all
.PHONY: all clean clean-build
