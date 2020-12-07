# Programming languages salary analyzer

This is a Python script for analyzing and issuing statistics on the average salary [popular programming languages for 2020](https://octoverse.github.com/ "Link") from popular job sites - [HeadHunter](https://hh.ru/) and [SuperJob](https://www.superjob.ru/).

## How to use
You should create .env file with your SuperJob token:
```
SUPERJOB_TOKEN='your_token'
```
Then run this script with console command:
```
python main.py
```
The result will look like this:

| Programming language | Vacancies found | Vacancies processed | Average salary (RUB) |
|----------------------|-----------------|---------------------|----------------------|
| JavaScript           | 1900            | 792                 | 144684               |
| Python               | 1900            | 433                 | 166804               |
| Java                 | 1900            | 455                 | 191695               |
| TypeScript           | 740             | 227                 | 185064               |
| C#                   | 1150            | 366                 | 165673               |

## Python3 should be already installed
Then use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```
