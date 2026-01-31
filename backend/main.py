from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import RedirectResponse

app = FastAPI(
    swagger_ui_parameters={"defaultModelsExpandDepth": -1},
    title="Color Mask API Server",
    description="Created and owned by Corgo LC",
    summary="Tech stack: Language(Python), API(FastAPI), UI(Swagger)",
    contact={
        "name": "Hunter Salazar",
        "email": "Hunter.Salazar@bon.nm.gov",
    },
)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", include_in_schema=False)
async def redirect_to_docs() -> RedirectResponse:
    """Redirect index to the Swagger"""
    return RedirectResponse(url="/docs")
