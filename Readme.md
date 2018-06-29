# RobotDB
## About
tbd

## Prerequisites
The only requirements are `Python 3.6+` and `pipenv`.

### Archlinux
Python is already up-to-date and `pipenv` is available in repo, so simply install it:
```sh
sudo pacman -S python-pipenv
```

### Ubuntu 18.04
Ubuntu 18.04 already has Python in required version (3.6+), so `pipenv` installation is simple:
```sh
sudo apt install python3-pip
pip3 install --user pipenv
export PATH=$PATH:~/.local/bin
```

### Debian, Ubuntu < 18.04
Debian 9 and older releases of Ubuntu ship with Python 3.4/3.5.

The easiest way to get newer versions is via [`pyenv`](https://github.com/pyenv/pyenv-installer). Installing `pyenv` dependencies and `pyenv` itself:
```sh
sudo apt install -y make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev xz-utils tk-dev libffi-dev
curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
```

Add these lines to your `.bashrc`, `.zshrc` or such (for Oh-My-Zsh there's a `pyenv` plugin that does the same thing):
```sh
export PATH="~/.pyenv/bin:$PATH"
eval "$(pyenv init -)"
eval "$(pyenv virtualenv-init -)"
```

Then refresh your shell by either sourcing proper `.bashrc`/`.zshrc`/whichever file, relogging or opening a new terminal window and finally install new Python (3.6.6 is the newest available in 3.6 branch as of writing this):
```sh
pyenv install -v 3.6.6
pyenv global 3.6.6
```

`pyenv` installs full CPython as provided on [python.org](python.org), so it ships with `pip` already available.
Therefore installing `pipenv` is just:
```sh
pip3 install --user pipenv
export PATH=$PATH:~/.local/bin
```

## Preparation
If during `pipenv install` the script prompts to install Python 3.6, confirm it.
`exit` closes `pipenv shell`, omit it if you want to run the server right away.

```sh
git clone https://github.com/mjbogusz/robotdb.git
cd robotdb
pipenv install
pipenv shell
./manage.py makemigrations robotdb
./manage.py migrate
./manage.py createsuperuser
exit
```

## Run
### Local
```sh
pipenv shell
./manage.py runserver
exit
```

### Global (visible outside)
```sh
sudo ufw allow 8000
pipenv shell
./manage.py runserver 0:8000
exit
```
