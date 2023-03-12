install:
	poetry install

test:
	poetry run pytest

build:	check
	poetry build

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl
