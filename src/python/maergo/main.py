import uvicorn

from fastapi import FastAPI
from fastapi.responses import RedirectResponse

app = FastAPI(title="Maergo")


@app.get("/")
async def docs_redirect() -> RedirectResponse:
    return RedirectResponse(url="/docs")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)