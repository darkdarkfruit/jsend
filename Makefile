files = jsend/__init__.py jsend/jsend.py jsend/test_jsend.py
file_pytest_genscript = test.pytest.py

default: test
	echo ''


test_python_setup: ${file_pytest_genscript}
	echo '==> generate "test.pytest.py"'
	py.test --genscript=test.pytest.py


test: ${files} test_python_setup
	echo ''
	echo '==> use "py.test jsend" directly: '
	py.test jsend
	echo ''
	echo '==> use "python setup.py test": '
	python setup.py test

# just py.test jsend
stest: 
	py.test jsend


# make a source distribution in dist/
sdist: ${files} test_python_setup
	python setup.py sdist