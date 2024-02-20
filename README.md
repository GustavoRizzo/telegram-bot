# Telegram-bot

Testing the Telegram bot.

## Tech Stack

- [Python](https://www.python.org/)

To help to create the local environment without Docker, you can use these version managers:

- Simple Python Version Management: [pyenv](https://github.com/pyenv/pyenv)



## Prepare `.env` file

Make a copy from `.env.example` to `.env` file. Edit and adjust the file. After that, just need to load the environment
variables:

```shell
cp .env.example .env
vi .env
```


## PYENV - To create the local environment:

````shell
cd ./be
pyenv local && pyenv install
python -m venv venv
source venv/bin/activate
pip install pip setuptools --upgrade
pip install -r requirements.txt
````
