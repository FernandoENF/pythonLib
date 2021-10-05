from models.Usuario import Usuario


class CtrlUsuario:
    def __init__(self, database):
        self.database = database

    def create_user(self, nome, email, senha):
        new_user = Usuario(nome, email, senha)
        self.database.add_user(user=new_user)
        return new_user

    def get_users(self):
        return self.database.get_users()

    def get_user_by_nome(self, nome):
        return self.database.get_user_by_nome(nome)

