init:
	pip install -r requirements/install.txt

test:
    pip install -r requirements/test.txt
    pytest -n auto
