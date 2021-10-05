from models.Emprestimo import Emprestimo


class CtrlEmprestimo:
    def __init__(self, database):
        self.database = database

    def create_emprestimo(self, usuario, livro, data_de_emprestimo, data_de_devolucao):
        if self.database.consultar_livro(livro):

            new_emprestimo = Emprestimo(usuario, livro, data_de_emprestimo, data_de_devolucao)
            return new_emprestimo
        return 'error'


