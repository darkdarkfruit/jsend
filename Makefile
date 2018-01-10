files = jsend/__init__.py jsend/jsend.py jsend/test_jsend.py
# file_pytest_genscript = jsend/test_jsend_pytest.py

default: test
	echo ''


# test_python_setup: ${file_pytest_genscript}
# 	echo '==> generate "test.pytest.py"'
# 	py.test --genscript=${file_pytest_genscript}


test: ${files} 
	echo ''
	echo '==> use "pytest jsend" directly: (pip3 install pytest)'
	pytest jsend/

# just py.test jsend
stest: 
	pytest jsend


# make a source distribution in dist/
sdist: ${files}
	python setup.py sdist


# upload to pypi
upload: sdist
	python setup.py sdist upload


install : test
	python setup.py install


# git push to github
# do `git remote add origin https://github.com/darkdarkfruit/python-jsend.git` first
git_push:
	git push --all


# git push with tags
git_push_tags:git_push
	git push --tags
