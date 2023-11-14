import pytest
from modules.api.clients.github import GitHub


@pytest.mark.api
def test_user_exists(github_api):
    user = github_api.get_user("defunkt")
    assert user["login"] == "defunkt"


@pytest.mark.api
def test_user_not_exists(github_api):
    r = github_api.get_user("butenkosergii")
    assert r["message"] == "Not Found"


@pytest.mark.api
def test_repo_can_be_found(github_api):
    r = github_api.search_repo("become-qa-auto")
    assert r["total_count"] == 50
    assert "become-qa-auto" in r["items"][0]["name"]


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    r = github_api.search_repo("bunechko_repo_not_exist")
    assert r["total_count"] == 0


@pytest.mark.api
def test_repo_with_single_char_be_found(github_api):
    r = github_api.search_repo("a")
    assert r["total_count"] != 0

# -------------------------------------------------------------------------------
# Project task 4. Module 27. API testing

@pytest.mark.api
def test_for_the_presence_of_commits(github_api):
    r = github_api.statistics("Bunechko", "Bunechko_QA_Auto")
    assert r[0]["total"] != 0


@pytest.mark.api
def test_subscribers(github_api):
    r = github_api.repository_subscribers("Bunechko", "Bunechko_QA_Auto")
    assert r[0]["login"] == "Bunechko"


@pytest.mark.api
def test_count_subscribers(github_api):
    r = github_api.repo_subscribers_count("Bunechko", "Bunechko_QA_Auto")
    assert r["subscribers_count"] == 1

# -------------------------------------------------------------------------------
