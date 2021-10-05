from models.Livro import Livro


class CtrlLivro:
    def __init__(self, database):
        self.database = database

    def create_livro(self, titulo, autor, editora):
        novo_livro = Livro(titulo, autor, editora)
        self.database.add_livro(livro=novo_livro)
        return novo_livro

    def get_livros(self):
        return self.database.get_livros()

    def get_livro_by_nome(self, titulo):
        return self.database.get_livro_by_nome(titulo)
