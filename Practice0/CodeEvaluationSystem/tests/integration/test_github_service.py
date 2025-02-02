from unittest.mock import MagicMock
from usecase.github_service import GitHubService


def test_get_student_repos():
    mock_github = MagicMock()
    mock_github.get_user.return_value.get_repos.return_value = [
        MagicMock(clone_url="https://github.com/user/repo1"),
        MagicMock(clone_url="https://github.com/user/repo2")
    ]

    service = GitHubService("fake_token")
    service.g = mock_github  # Подменяем реальный GitHub API

    repos = service.get_student_repos("user")

    assert repos == ["https://github.com/user/repo1", "https://github.com/user/repo2"]
