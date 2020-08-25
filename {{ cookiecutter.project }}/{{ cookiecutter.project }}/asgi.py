from starlette.applications import Starlette
from starlette.staticfiles import StaticFiles
from starlette.middleware import Middleware
from starlette.middleware.cors import CORSMiddleware

from . import settings
from .url import routes

if settings.DEBUG:
    from starlette.routing import Mount
    static = StaticFiles(directory="static/dist", html=True)
    routes.append(Mount("/", app=static, name="static"))

middleware = [
    Middleware(
        CORSMiddleware,
        allow_origins=['*'],
        allow_methods=['*']
    ),
]

app = Starlette(
    debug=settings.DEBUG,
    middleware=middleware,
    routes=routes,
)
