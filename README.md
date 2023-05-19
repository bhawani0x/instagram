# instagram

# PROJECT SETUP

## __Frontend__

### change directory to frontend
`cd frontend`

### install dependencies
`npm install`

### create frontend build (Need to run this for every update)
`npm run build`

## __Backend__

### create venv
`virtualenv venv`

### activate venv
for linux - `source venv/bin/activate`
for windows - `source venv/Script/activate`

### install dependencies
`pip3 install -r requirement.txt`

### run migrations
`python manage.py makemigrations`
`python manage.py migrate`
`python manage.py makemigrations api`
`python manage.py migrate api`

### create superuser
`python manage.py createsuperuser`

### start backend local server
`python manage.py runserver`
