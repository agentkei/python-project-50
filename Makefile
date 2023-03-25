install:
	poetry install

test:
	poetry run pytest

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8

retry:
	poetry install
	poetry build
	python3 -m pip install --user  --force-reinstall dist/*.whl

#test:
	