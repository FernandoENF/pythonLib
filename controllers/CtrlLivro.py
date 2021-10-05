from models.Livro import Livro


class CtrlLivro:
    def __init__(self, database):
        self.database = database

    def create_livro(self, titulo, autor, editora):
        novo_livro = Livro(titulo, autor, editora)
        self.database.add_livro(livro=novo_livro)
        return novo_livro
