from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from typing import Optional
from server.server import get_all_info, get_repo, get_all_repos
from server.scraper import get_pinned_repos

app = FastAPI()

@app.get('/')
async def home():
    return RedirectResponse('https://github.com/Los-had/github-extended-api')

@app.get('/api/v1/get-all-user-info/{username}')
async def get_all_user_information(username: str, filter: Optional[str] = None):
    if filter is None:
        return get_all_info(username)
    
    return get_all_info(username, filter)

@app.get('/api/v1/get-all-repos')
async def get_all_repositories(username: str):
    return get_all_repos(username)

@app.get('/api/v1/get-repo/{repo}')
async def get_repository(repo: str, username: str):
    return get_repo(repo, username)

@app.get('/api/v1/get-pinned-repos')
async def get_pinned_repositories(username: str):
    return get_pinned_repos(username)
