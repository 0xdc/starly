import uvicorn

uvicorn.run("{{ cookiecutter.project }}:app", reload=True)
