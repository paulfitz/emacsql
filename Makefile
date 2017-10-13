sdist:
	rm -rf dist
	cp README.md README
	python setup.py sdist
	ls -l dist/emacsql*.tar.gz
	sleep 5
	cd dist && mkdir tmp && cd tmp && tar xzvf ../emacsql*.tar.gz && cd emacsql*[0-9] && ./setup.py build
	python setup.py sdist
	twine upload dist/emacsql*.tar.gz
	rm -rf dist
	rm README
