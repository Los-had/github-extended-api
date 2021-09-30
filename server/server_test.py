from .server import get_repo, get_all_repos, get_all_info
import pytest

def test_typing_for_all_functions():
    get_repo_response = get_repo('Los-had', 'Los-had')
    get_all_repos_response = get_all_repos('Los-had')
    get_all_info_response_without_filter = get_all_info('Los-had')
    get_all_info_response_with_filter = get_all_info('Los-had', 'bio')
    assert type(get_all_repos_response) == dict
    assert type(get_repo_response) == dict
    assert type(get_all_info_response_with_filter) == dict
    assert type(get_all_info_response_without_filter) == dict
