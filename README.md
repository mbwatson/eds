# Earth Data Science

## Description

This is the (very beginning of the) foundation for a Django-based website for the Earth Date Science group at Renaissance Computing Institute ([http://www.renci.org](RENCI)).

## Development Server

Set `DEBUG = True` in `/eds/settings.py`, and execute `python3 manage.py runserver` in base directory of installation.

## Production

Set `DEBUG = False` and in `/eds/settings.py` and set yourself a `DJANGO_SECRET_KEY` environment variable.