import pytest
from domain.code import Code
from usecase.code_service import CodeService


@pytest.fixture
def sample_code():
    return Code(code_id=1, student_id=123, lab_number=1, repo_url="https://github.com/user/repo",
                content="print('Hello')")


def test_upload_code(sample_code, mocker):
    mock_save = mocker.patch("infrastructure.database.save_code")

    code = CodeService.upload_code(student_id=123, lab_number=1, repo_url="https://github.com/user/repo",
                                   content="print('Hello')")

    assert code.student_id == 123
    assert code.lab_number == 1
    assert code.repo_url == "https://github.com/user/repo"
    mock_save.assert_called_once()
