SHELL := /bin/bash -O globstar


run:
	hypercorn --reload --config=hypercorn.toml 'fomento_repeat.main:app'


test:
	pytest -x --cov-report term-missing --cov-report html --cov-branch \
	       --cov fomento_repeat/


lint:
	@echo
	ruff .
	@echo
	blue --check --diff --color .
	@echo
	mypy .
	@echo
	pip-audit


format:
	ruff --silent --exit-zero --fix .
	blue .


build:
	docker build -t fomento_repeat .


smoke_test: build
	docker run --rm -d -p 5000:5000 --name fomento_repeat fomento_repeat
	sleep 2; curl http://localhost:5000/hello
	docker stop fomento_repeat


install_hooks:
	@ scripts/install_hooks.sh
