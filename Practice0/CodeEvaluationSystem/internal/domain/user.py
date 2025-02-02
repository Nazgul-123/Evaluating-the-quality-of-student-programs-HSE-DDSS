def __init__(self, user_id, username, role, email, github_nick, group=None):
    self.user_id = user_id
    self.username = username
    self.role = role  # "student", "teacher", "admin"
    self.email = email
    self.github_nick = github_nick
    self.group = group  # Только для студентов
