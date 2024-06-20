.DEFAULT_GOAL := test

check_prereqs:
	bash -c '[[ -n $$VIRTUAL_ENV ]]'
	bash -c '[[ $$(python3 --version) == *3.11* ]]'

install: check_prereqs
	python3 -m pip install -e '.[dev]'

test: install
	pylint singer --extension-pkg-whitelist=ciso8601 -d missing-docstring,broad-except,bare-except,too-many-return-statements,too-many-branches,too-many-arguments,no-else-return,too-few-public-methods,fixme,protected-access,broad-exception-raised,consider-using-f-string
	python3 -m doctest -v singer/utils.py
	python3 -m unittest -v
