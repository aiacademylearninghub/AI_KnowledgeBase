import os
import uvicorn
from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from app.api.v1.endpoints import chat_with_knowledge_base, socket
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from fastapi import Request
from fastapi.responses import RedirectResponse


app = FastAPI(
    title="Chat with Knowledge Base API Documentation",
    version="0.0.1",
    description="API Documentation for Knowledge Base Chatbot",
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(
    chat_with_knowledge_base.router,
    prefix="/v1/knowledge-base",
    tags=["Chat with Knowledge Base"],
)
app.include_router(
    socket.router,
    tags=["Socket"],
)

# Serving - static files
static_files_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "static")
app.mount("/", StaticFiles(directory=static_files_path), name="static")
templates = Jinja2Templates(directory=static_files_path)


@app.get("/", response_class=HTMLResponse)
@app.get("/index.html", response_class=HTMLResponse)
def read_index(request: Request):
    """Serve the index.html file of front-end code at the root."""
    return templates.TemplateResponse("index.html")

# @app.middleware("http")
# async def redirect_middleware(request: Request, call_next):
#     if "static/" in request.url.path and "index.html" not in request.url.path : 
#         new_url = request.url.path+"/index.html"
#         return RedirectResponse(url=new_url)
#     return await call_next(request)


def main():
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=False)


if __name__ == "__main__":
    main()
    
    
    # Need to add everytime when ever you built that file inside the head tag
# <style>
#     #__docusaurus>nav:nth-child(2) {
#         display: none;
#     }
#     #__docusaurus>div:nth-child(3) {
#         display: none;
#     }
# </style>
