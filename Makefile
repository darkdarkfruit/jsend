files = jsend/__init__.py jsend/jsend.py jsend/test_jsend.py
file_pytest_genscript = jsend/test_jsend_pytest.py

default: test
	echo ''


test_python_setup: ${file_pytest_genscript}
	echo '==> generate "test.pytest.py"'
	py.test --genscript=${file_pytest_genscript}


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


# upload to pypi
upload: sdist
	python setup.py sdist upload


install : test
	python setup.py install


# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/python-jsend.git` first
git_push:
	git push 


# git push with tags
git_push_tags:
	git push --tags
