# Environments in python

# tools help create isolated environments to manage specific projects and manage its dependencies
# pipenv, virtualenv, pyenv

# Virtualenv - venv
# allows multiple environmnets with different packages for different environments
# avoids conflicts between global and project dependencies

# install virtualenv
pip install virtualenv
# create a environment
virtualenv myenv # environment name is myenv
# activating the environment
myenv\Scripts\activate
# deactivate environment
deactivate
# use pip to install packages

# Pipeenv
# higher-level tool which integrates pip and virtualenv
# automatically creates and manages virtual environments
# uses Pipfile for specifying dependencies
# uses Pipfile.lock to ensure package versions

# install pipenv
pip install pipenv
# create and manage dependencies with pipenv
pipenv install
pipenv install packages
# activate environment
pipenv shell
# deactivate environment
exit
# install a dependency for only developement
pipenv install package_name --dev
# run scripts inside pipenv
pipenv run python myscript.py
# uninstall packages
pipenv uninstall package_name

# Pyenv  
# to manage multiple versions of python on system
# allows per project python version management

# install pyenv
#  Install dependencies for building Python
sudo apt-get update; sudo apt-get install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm \
libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl git

#  Install pyenv
curl https://pyenv.run | bash

# Virtualenv: If you want a simple, lightweight way to isolate environments and manage packages yourself.

# Pipenv: If you want automatic environment and dependency management with a focus on deterministic builds.

# Pyenv: If you need to manage multiple Python versions for different projects and easily switch between them.


