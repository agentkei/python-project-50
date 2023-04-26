install:
	poetry install

build:
	poetry build

publish:
	poetry publish --dry-run

package-install:
	python3 -m pip install --user --force-reinstall dist/*.whl

lint:
	poetry run flake8 _tests hexlet_code
	
retry:
	poetry install
	poetry build
	poetry publish --dry-run
	python3 -m pip install --user --force-reinstall dist/*.whl

test:
	poetry run pytest

coverage:
	coverage run --source=hexlet_code -m pytest
	coverage report -m