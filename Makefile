install:
	@echo "Set poetry with the current python version"
	poetry env use `python3 --version | grep -Eo '[0-9]+([.][0-9]+)+([.][0-9]+)?'`
	@echo "Install dependencies"
	poetry install
	$(MAKE) path

update:
	poetry update

path:
	@echo "Python virtual environment (virtualenv) path is:"
	poetry show -v | grep "Using virtualenv"

clean:
	@echo "Uninstall python environment"
	poetry env remove --all

run:
	python3 ./learn_dj/manage.py runserver
