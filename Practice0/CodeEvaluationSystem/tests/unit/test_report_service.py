import pytest
from usecase.report_service import ReportService


@pytest.fixture
def mock_code_data(mocker):
    mock_db = mocker.patch("infrastructure.database.get_code_by_lab")
    mock_db.return_value = [
        {"code_id": 1, "status": "checked"},
        {"code_id": 2, "status": "pending"}
    ]
    return mock_db


def test_generate_report(mock_code_data):
    reports = ReportService.generate_report(lab_number=1)

    assert len(reports) == 2
    assert "Отчет по коду 1: оценка checked" in reports
    assert "Отчет по коду 2: оценка pending" in reports
