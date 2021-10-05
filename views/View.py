import controllers.CtrlEmprestimo
from controllers import CtrlUsuario, CtrlEmprestimo, CtrlLivro

from database.Database import Database


class View:
    def __init__(self):
        self.database = Database()
        self.ctrl_usuario = controllers.CtrlUsuario.CtrlUsuario(self.database)
        self.ctrl_emprestimo = controllers.CtrlEmprestimo.CtrlEmprestimo(self.database)
        self.ctrl_livro = controllers.CtrlLivro.CtrlLivro(self.database)

    def start(self):
        print('Que tipo de operação deseja realizar?')
        print('1 - Criar novo usuário')
        print('2 - Inserir novo livro')
        print('3 - Criar novo empréstimo')
