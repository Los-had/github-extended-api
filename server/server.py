import requests
from requests import HTTPError, ConnectionError
import json
from typing import Optional
from error_module.errors import dynamic_error, default_error, connection_error, http_error

def get_all_info(username: str, filter: Optional[str] = None) -> dict:
    if filter:
        activate_filter = True
    else:
        activate_filter = None

    if username == '':
        return dynamic_error('No username specified')
    
    try:
        url = f'https://api.github.com/users/{username}'
        github_api = requests.get(url)
        repos_link = requests.get(f'https://api.github.com/users/{username}/repos')
        repos_response = json.loads(repos_link.text)
        response = json.loads(github_api.text)

        if 'message' in response:
            if response['message'].startswith('API rate limit'):        
                return 'Wait one hour the limit is 60 request for hour'
            return dynamic_error('User not found, try again.')
        
        if activate_filter:
            return {
                filter: response[filter]
            }

        bio = response['bio'].replace('\r\n', '')
        name = response['name']
        user = response['login']
        followers = response['followers']
        following = response['following']
        site = response['blog']
        
        email = response['email']
        if email == None:
            email = "Don't have a public email"
        
        hireable = response['hireable']
        if hireable == None:
            hireable = 'Not hireable'
        
        twitter_username = response['twitter_username']
        location = response['location']
        company = response['company']
        profile_picture = response['avatar_url']
        repos = response['public_repos']
        newest_repo = repos_response[0]['full_name']
        profile_link = f'https://github.com/{user}'
        api_response = {
            'bio': bio, 
            'name': name, 
            'username': user,
            'followers': followers, 
            'following': following, 
            'website': site, 
            'twitter': twitter_username, 
            'location': location, 
            'company': company, 
            'picture': profile_picture, 
            'repos': repos,
            'newest_repo': newest_repo,
            'link': profile_link
        }

        return api_response
    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except Exception as e:
        return dynamic_error(e)
    except:
        return default_error()

def get_repo(repo: str, username :str) -> dict:
    if username == '':
        return dynamic_error('No username specified')
    
    try:
        url = f'https://api.github.com/users/{username}/repos'
        repos_link = requests.get(url)
        repos_response = json.loads(repos_link.text)
        repos = {
            'repo': []
        }

        if 'message' in repos_response:
            if repos_response['message'].startswith('API rate limit'):        
                return dynamic_error('Wait one hour the limit is 60 request for hour')
            return dynamic_error('User not found, try again.')
        
        for repo_s in repos_response:
            if repo_s['name'] == repo:
                owner = repo_s['owner']['login']
                if 'license' in repo_s:
                    license = repo_s['license']
                else:
                    license = None
                
                if 'language' in repo_s:
                    language = repo_s['language']
                
                name = repo_s['name']
                full_name = repo_s['full_name']
                is_a_fork = repo_s['fork']
                has_issues = repo_s['has_issues']
                has_projects = repo_s['has_projects']
                has_wiki = repo_s['has_wiki']
                number_of_forks = repo_s['forks_count']
                default_branch = repo_s['default_branch']
                description = repo_s['description']
                repo_url = repo_s['url']
                stars = repo_s['stargazers_count']
                open_issues = repo_s['open_issues_count']
                repo_response = {
                    'name': name,
                    'full_name': full_name,
                    'description': description,
                    'owner': owner,
                    'license': license,
                    'language': language,
                    'repo_url': repo_url,
                    'stars': stars,
                    'number_of_forks': number_of_forks,
                    'is_a_fork': is_a_fork,
                    'default_branch': default_branch,
                    'has_issues': has_issues,
                    'number_of_open_issues': open_issues,
                    'has_wiki': has_wiki,
                    'has_projects': has_projects,

                }

                repos['repo'].append(repo_response)
        
        return repos
    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except Exception as e:
        return dynamic_error(e)
    except:
        return default_error()

def get_all_repos(username: str) -> dict:
    if username == '':
        return dynamic_error('No username specified')
    
    try:
        url = f'https://api.github.com/users/{username}/repos'
        repos_link = requests.get(url)
        repos_response = json.loads(repos_link.text)
        repos = {
            'repos': []
        }

        if 'message' in repos_response:
            if repos_response['message'].startswith('API rate limit'):        
                return dynamic_error('Wait one hour the limit is 60 request for hour')
            return dynamic_error('User not found, try again.')
        
        for repo in repos_response:
            owner = repo['owner']['login']
            if 'license' in repo:
                license = repo['license']
            else:
                license = None
            
            if 'language' in repo:
                language = repo['language']
            
            name = repo['name']
            full_name = repo['full_name']
            is_a_fork = repo['fork']
            has_issues = repo['has_issues']
            has_projects = repo['has_projects']
            has_wiki = repo['has_wiki']
            number_of_forks = repo['forks_count']
            default_branch = repo['default_branch']
            description = repo['description']
            repo_url = repo['url']
            stars = repo['stargazers_count']
            open_issues = repo['open_issues_count']
            repo_response = {
                'name': name,
                'full_name': full_name,
                'description': description,
                'owner': owner,
                'license': license,
                'language': language,
                'repo_url': repo_url,
                'stars': stars,
                'number_of_forks': number_of_forks,
                'is_a_fork': is_a_fork,
                'default_branch': default_branch,
                'has_issues': has_issues,
                'number_of_open_issues': open_issues,
                'has_wiki': has_wiki,
                'has_projects': has_projects,

            }

            repos['repos'].append(repo_response)
        
        return repos
    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except UnicodeEncodeError as e:
        return dynamic_error(f'unicode_error({e}), language not supported')
    except Exception as e:
        return dynamic_error(e)
    except:
        return default_error()

if __name__ == '__main__':
    '''
    print(get_all_repos('lind0-oss'))
    print('\n\n\n\n')
    print(get_all_info('lind0-oss'))
    print(get_all_repos('AIBUSHISHOU'))
    print(get_repo('Los-had', 'Los-had'))
    '''
    print(get_repo('whatsapp-automation', 'Los-had'))