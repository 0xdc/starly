from starlette.applications import Starlette
from starlette.routing import Mount
from starlette.staticfiles import StaticFiles

from . import settings
from .url import routes

if settings.DEBUG:
    routes.append(Mount("/", app=StaticFiles(directory="static", html=True), name="static"))

app = Starlette(debug=settings.DEBUG, routes=routes)
