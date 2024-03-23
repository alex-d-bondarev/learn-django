install:
	@echo "Set poetry with the current python version"
	poetry env use `python --version | grep -Eo '[0-9]+([.][0-9]+)+([.][0-9]+)?'`
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

