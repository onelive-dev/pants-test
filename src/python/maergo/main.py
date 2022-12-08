import uvicorn
from fastapi import FastAPI
from fastapi.responses import RedirectResponse

from .routers.v1 import v1_organizations
from .core.config import config

app = FastAPI(title="Maergo1")
app.include_router(v1_organizations.router, prefix=config.API_V1_PREFIX)


@app.get("/")
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=config.PORT)
