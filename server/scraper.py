from bs4 import BeautifulSoup
import requests
from requests import HTTPError, ConnectionError
from typing import Optional
from error_module.errors import dynamic_error, default_error, connection_error, http_error

def get_pinned_repos(username: str) -> dict:
    if username == '':
        return dynamic_error('Username not specified')
    
    try:
        url = f'https://github.com/{username}'
        website = requests.get(url).text
        soup = BeautifulSoup(website, 'lxml')
        pinned_repos = {
            "repos": []
        }
        pinned_list = soup.find_all('li', class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')

        for pin in pinned_list:
            owner = username
            name = pin.find('span', class_='repo')
            description = pin.find('p', class_='pinned-item-desc color-text-secondary text-small d-block mt-2 mb-3')
            language = pin.find('span', itemprop='programmingLanguage')

            if name and description and language:
                repo = {
                    'owner': owner,
                    'name': name.text,
                    'description': description.text.replace('   ', '').replace('\n', ''),
                    'language': language.text,
                    'link': f'https://github.com/{username}/{name.text}'
                }
            elif description is None:
                repo = {
                    'owner': owner,
                    'name': name.text,
                    'description': None,
                    'language': language.text,
                    'link': f'https://github.com/{username}/{name.text}'
                }
            elif language is None:
                repo = {
                    'owner': owner,
                    'name': name.text,
                    'description': description.text.replace('   ', '').replace('\n', ''),
                    'language': None,
                    'link': f'https://github.com/{username}/{name.text}'
                }
            else:
                repo = dynamic_error("This user does not have pinned repos")

            pinned_repos['repos'].append(repo)
        
        return pinned_repos
    except UnicodeEncodeError as e:
        return dynamic_error(f'unicode_error({e}), language not supported')
    except HTTPError as e:
        return http_error(e)
    except ConnectionError as e:
        return connection_error(e)
    except Exception as e:
        return dynamic_error(e)
    except:
        return default_error()

if __name__ == '__main__':
    #print(get_pinned_repos('AIBUSHISHOU'))
    #print(get_pinned_repos('lind0-oss'))
    print(get_pinned_repos('Los-had'))