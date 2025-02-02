def __init__(self, code_id, student_id, lab_number, repo_url=None, content=None, status="pending"):
    self.code_id = code_id
    self.student_id = student_id
    self.lab_number = lab_number  # Студент сам указывает в репозитории
    self.repo_url = repo_url  # Либо ссылка на GitHub
    self.content = content  # Либо загруженный код
    self.status = status  # "pending", "checked"
