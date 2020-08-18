BASEDIR=$(CURDIR)


clean:
	find . -iname "__pycache__" -type "d" | xargs rm -rfv
	find . -iname "*.pyc" | xargs rm -fv
	rm -rfv build/ dist/ *.egg-info


install:
	python setup.py install


uninstall:
	pip uninstall yari -y


reinstall: uninstall install clean


.PHONY: clean, install, reinstall
