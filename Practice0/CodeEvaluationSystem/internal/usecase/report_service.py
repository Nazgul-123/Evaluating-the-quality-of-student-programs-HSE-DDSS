@staticmethod
def generate_report(lab_number=None, student_id=None, group=None):
    """ Генерирует отчет по коду (по лабораторной, студенту или группе) """
    reports = []
    # Получаем код по критериям
    if student_id:
        reports = get_code_by_student(student_id)
    elif lab_number:
        reports = get_code_by_lab(lab_number)
    elif group:
        reports = get_code_by_group(group)

    # Генерируем отчеты
    return [f"Отчет по коду {c.code_id}: оценка {c.status}" for c in reports]
