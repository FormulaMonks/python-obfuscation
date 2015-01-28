all:
	@ python -m compileall app/

clean-py:
	@ find . ! -name "manage.py" -name "*.py" -delete

clean:
	@ find . -name "*.pyc" -delete

.DEFAULT: all
.PHONY: all clean clean-py
