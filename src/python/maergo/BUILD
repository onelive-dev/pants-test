python_sources(
    name="modules",
    dependencies=[
        "3rdparty/python:poetry#fastapi",
        "3rdparty/python:poetry#uvicorn",
        "3rdparty/python:poetry#pydantic",
    ],
)


pex_binary(
    name="main",
    entry_point="main.py",
    dependencies=[
        ":modules",
    ],
    complete_platforms=("3rdparty/platforms:docker_python_3_10_bullseye",),
)
