from fastapi import FastAPI
from server import get_all_info, get_repo, get_all_repos
from scraper import get_pinned_repos

app = FastAPI()

@app.get('/api/v1/get-all-user-info/{username}')
def get_all_user_information(*, username: str, filter=None):
    if filter is None:
        return get_all_info(username)
    
    return get_all_info(username, filter)

@app.get('/api/v1/get-all-repos')
def get_all_repositories(username: str):
    return get_all_repos(username)

@app.get('/api/v1/get-repo/{repo}')
def get_repository(repo: str, username: str):
    return get_repo(repo, username)

@app.get('api/v1/get-pinned-repos')
def get_pinned_repositories(username: str):
    return get_pinned_repos(username)