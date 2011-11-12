files = jsend/__init__.py jsend/jsend.py jsend/test_jsend.py

test: ${files}
	py.test jsend


# make a source distribution in dist/
sdist: ${files}
	python setup.py sdist