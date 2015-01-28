all:
	@ python -OO -m compileall app/

clean-py:
	@ find . ! -name "__init__.py" ! -name "manage.py" -name "*.py" -delete

clean:
	@ find . -name "*.pyc" -delete

.DEFAULT: all
.PHONY: all clean clean-py
