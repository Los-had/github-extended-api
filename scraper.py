from bs4 import BeautifulSoup
import requests
from requests import HTTPError, ConnectionError
from errors import connection_error, http_error, dynamic_error, default_error

def get_pinned_repos(username: str):
    if username == '':
        return dynamic_error('Username not specified')
    
    url = f'https://github.com/{username}'
    website = requests.get(url).text
    soup = BeautifulSoup(website, 'lxml')
    pinned_repos = {
        "repos": []
    }
    pinned_list = soup.find_all('li', class_='mb-3 d-flex flex-content-stretch col-12 col-md-6 col-lg-6')
    
    for pin in pinned_list:
        name = pin.find('span', class_='repo')
        if name:
            description = pin.find('p', class_='pinned-item-desc color-text-secondary text-small d-block mt-2 mb-3')
            stars_not_used = pin.find('a', class_='pinned-item-meta Link--muted')
            if stars_not_used:
                stars = stars_not_used.replace(' ', '').replace(',', '.')
                repo = {
                    "name": name.text.replace('\n', ''),
                    "description": description.replace('    ', ''),
                    "stars": float(stars),
                    "url": f"https://github.com/{username}/{name}"
                }
            else:
                stars = None
                repo = {
                "name": name.text.replace('\n', ''),
                "description": description.replace('    ', ''),
                "stars": stars,
                "url": f"https://github.com/{username}/{name}"
            }

            pinned_repos['repos'].append(repo)
        else:
            return dynamic_error("This user doesn't have pinned repos")
    
    return pinned_repos

if __name__ == '__main__':
    #print(get_pinned_repos('AIBUSHISHOU'))
    print(get_pinned_repos('Los-had'))