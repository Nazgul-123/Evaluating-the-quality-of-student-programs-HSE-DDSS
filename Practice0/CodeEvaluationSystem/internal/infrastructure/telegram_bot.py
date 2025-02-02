import telebot
from config import TELEGRAM_TOKEN

bot = telebot.TeleBot(TELEGRAM_TOKEN)

def setup_telegram_handlers(bot, code_service, report_service):
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, "Добро пожаловать! Выберите действие: /upload, /report")

    @bot.message_handler(commands=['upload'])
    def upload_code(message):
        bot.reply_to(message, "Отправьте файл с кодом или укажите ссылку на GitHub")

    @bot.message_handler(content_types=['document'])
    def handle_code_upload(message):
        file_info = bot.get_file(message.document.file_id)
        downloaded_file = bot.download_file(file_info.file_path)

        code_service.upload_code(message.chat.id, downloaded_file.decode())
        bot.reply_to(message, "Код загружен!")

    @bot.message_handler(commands=['report'])
    def handle_report_request(message):
        reports = report_service.generate_report()
        bot.reply_to(message, "\n".join(reports))

    bot.polling()
