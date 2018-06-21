### Prerequisites

Archlinux
```sh
sudo pacman -S python-pipenv
```

Debian/Ubuntu
```sh
sudo apt install python3-pip
pip install --user pipenv
export PATH=$PATH:~/.local/bin
```

### Preparation
```sh
pipenv install
pipenv shell
./manage.py makemigrations robotdb
./manage.py migrate
./manage.py createsuperuser
exit
```

### Run
```sh
pipenv shell
./manage.py runserver
exit
```
