{{ cookiecutter.project }}
==========================

Requirements:
* Database server (SQLAlchemy compatible; primarily MySQL, sqlite3 for smaller installations)
* Static file webserver

Install:

```sh
pip install -e git+https://github.com/0xdc/{{ cookiecutter.project }}#egg={{ cookiecutter.project }}
```

Development:

```sh
alembic upgrade head
(cd static; npm install --dev; parcel serve *.html) &
DEBUG=1 python -m{{ cookiecutter.project }}
```

Production:

```sh
(cd static; npm install --dev; npm run build)
uvicorn {{ cookiecutter.project }}.asgi:app
```

Create migrations:

```sh
alembic revision --autogenerate -m "message"
```

Test:

```sh
pip install -e .[test]
coverage run -m pytest
coverage report -m --include="{{ cookiecutter.project }}/*,migrations/*,tests/*"
```

Technology used
---------------
* [Starlette](https://www.starlette.io)
* [SQLAlchemy](https://sqlalchemy.org)
* [Parcel](https://parceljs.org)
* [HTML5 platform](https://platform.html5.org)
