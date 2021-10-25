### Setup instructions

1. Install python and pip
1. create virtual env named `deven` using `python -m venv deven`
1. Activate the venv `deven` with

   > `source deven/bin/activate` in linux

   > `.\deven\Scripts\activate.bat` in windows **powershell**

   > `source deven/Scripts/activate` in windows **git bash**

1. Run `pip install -r requirements.txt`

### Running the app in development

`python manage.py runserver`

### `.env` file

Create a `.env` file in the project root (where manage.py resides)
for all the settings that are not same in all cases and
for secrets. They are loaded to the settings file with the help of
python package: `python-decouple`

An example `.env` file looks as follows:

```
DEBUG=True
DATABASE_NAME=django_db
DATABASE_USER=django
DATABASE_PASSWORD=abcd
DATABASE_HOST=localhost
DATABASE_PORT=5432
```

Add any new settings relying on `.env` file to the above.
