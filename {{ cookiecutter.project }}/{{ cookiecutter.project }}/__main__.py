import uvicorn

uvicorn.run("{{ cookiecutter.project }}.asgi:app", reload=True)
