from models.Usuario import Usuario


class CtrlUsuario:
    def __init__(self, database):
        self.database = database

    def create_user(self, nome, email, senha):
        new_user = Usuario(nome, email, senha)
        self.database.add_user(user=new_user)
        return new_user
