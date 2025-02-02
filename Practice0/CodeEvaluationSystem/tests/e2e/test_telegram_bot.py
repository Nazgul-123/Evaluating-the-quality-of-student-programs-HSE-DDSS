import pytest
import telebot
from unittest.mock import MagicMock, patch
from infrastructure.telegram_bot import bot, handle_code_upload, handle_report_request

@pytest.fixture
def mock_telegram_message():
    message = MagicMock()
    message.chat.id = 12345
    message.document.file_id = "test_file_id"
    return message

@patch("telebot.TeleBot.get_file")
@patch("telebot.TeleBot.download_file")
def test_handle_code_upload(mock_download_file, mock_get_file, mock_telegram_message):
    mock_get_file.return_value.file_path = "path/to/file"
    mock_download_file.return_value = b"print('Hello')"

    handle_code_upload(mock_telegram_message)

    mock_get_file.assert_called_once()
    mock_download_file.assert_called_once()
    bot.send_message.assert_called_with(12345, "Код загружен! ID:")


@patch("usecase.report_service.ReportService.generate_report", return_value=["Отчет по коду 1: оценка 5"])
def test_handle_report_request(mock_generate_report, mock_telegram_message):
    handle_report_request(mock_telegram_message)

    mock_generate_report.assert_called_once()
    bot.send_message.assert_called_with(12345, "Отчет по коду 1: оценка 5")