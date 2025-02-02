from infrastructure.database import save_code

class CodeService:
    @staticmethod
    def upload_code(student_id, lab_number, repo_url=None, content=None):
        """ Загружает код студента и сохраняет в БД """
        code = Code(code_id=None, student_id=student_id, lab_number=lab_number, repo_url=repo_url, content=content)
        save_code(code)
        return code
