from .scraper import get_pinned_repos
import pytest

def test_typing():
    response = get_pinned_repos('Los-had')
    assert type(response) == dict

def test_response():
    response = get_pinned_repos('Los-had')
    los_had_pinned_repos_response = {'repos': [{'owner': 'Los-had', 'name': 'whatsapp-automation', 'description': '  Automating whatsapp with python', 'language': 'Python', 'link': 'https://github.com/Los-had/whatsapp-automation'}, {'owner': 'Los-had', 'name': 'mercado-livre-api', 'description': '  search and save products in mercado livre', 'language': 'Python', 'link': 'https://github.com/Los-had/mercado-livre-api'}, {'owner': 'Los-had', 'name': 'curso-ruby', 'description': '  arquivos de um curso de ruby que conclui ', 'language': 'Ruby', 'link': 'https://github.com/Los-had/curso-ruby'}, {'owner': 'Los-had', 'name': 'github-profile-search', 'description': '  search github profiles.', 'language': 'HTML', 'link': 'https://github.com/Los-had/github-profile-search'}, {'owner': 'Los-had', 'name': 'CSSvariables', 'description': '  variaveis no CSS3', 'language': None, 'link': 'https://github.com/Los-had/CSSvariables'}, {'owner': 'Los-had', 'name': 'random-person-api', 'description': '  retorna informações de pessoas que não existem', 'language': 'Python', 'link': 'https://github.com/Los-had/random-person-api'}]}

    assert response == los_had_pinned_repos_response