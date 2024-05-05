import os

import uvicorn
from fastapi import FastAPI, HTTPException, Request, Security, Depends
from fastapi.responses import HTMLResponse, FileResponse, StreamingResponse
from fastapi.middleware.cors import CORSMiddleware
from fastapi.templating import Jinja2Templates
from fastapi.security import APIKeyHeader

from utils.config import API_KEY, API_NAME, origins
from utils.enums import HttpStatusCode
from utils.models import Conversation, StreamingContent
from utils.pipelines import suggestions

app = FastAPI(
    title=API_NAME,
    description="API for the AI Copilot.",
    version="0.1.0",
    openapi_tags=[
        {"name": API_NAME, "description": "Endpoints for AI Copilot"},
    ],
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Index"], response_class=HTMLResponse)
def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/robots.txt", include_in_schema=False)
async def get_robots_txt():
    robots_txt_path = os.path.join("static", "robots.txt")
    return FileResponse(robots_txt_path, media_type="text/plain")


templates = Jinja2Templates(directory="static")


api_key_header = APIKeyHeader(
    name="X-API-Key",
    auto_error=False,
)


async def get_api_key(api_key_header: str = Security(api_key_header)):
    if api_key_header:
        if api_key_header == API_KEY:
            return API_KEY
        else:
            raise HTTPException(
                status_code=HttpStatusCode.UNAUTHORIZED.value,
                detail="Invalid API Key",
            )
    else:
        raise HTTPException(
            status_code=HttpStatusCode.BAD_REQUEST.value,
            detail="Please enter an API key",
        )


@app.post(
    path="/get_suggestions",
    tags=["Model Endpoints"],
    response_description="Successful Response",
    description="Get AI Summaries and Suggestions",
    name=API_NAME,
)
async def process(
    conversationRequest: Conversation, api_key: str = Depends(get_api_key)
):
    return StreamingResponse(
        suggestions(conversationRequest), media_type="text/event-stream"
    )


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001, reload=True, workers=4)
