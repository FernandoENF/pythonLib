import controllers.CtrlEmprestimo
from controllers import CtrlUsuario, CtrlEmprestimo, CtrlLivro
from datetime import date, timedelta
from database.Database import Database


class View:
    def __init__(self):
        self.database = Database()
        self.ctrl_usuario = controllers.CtrlUsuario.CtrlUsuario(self.database)
        self.ctrl_emprestimo = controllers.CtrlEmprestimo.CtrlEmprestimo(self.database)
        self.ctrl_livro = controllers.CtrlLivro.CtrlLivro(self.database)

    def start(self):
        while True:
            self.print_menu()
            opcao = input('Insira o número da opção desejada: ')
            if opcao == '0':
                print('-'*30)
                nome = input('Digite o nome do usuário: ')
                print('-'*30)
                email = input('Digite o email do usuário: ')
                print('-'*30)
                senha = input('Digite a senha do usuário: ')
                usuario = self.ctrl_usuario.create_user(nome, email, senha)
                print('Usuário inserido!')
                print('-'*30)
                print('| Nome: {}'.format(usuario.nome))
                print('| Email: {}'.format(usuario.email))
                print('| Senha: {}'.format(usuario.senha))
                print('-'*30)

            elif opcao == '1':
                print('-'*30)
                titulo = input('Digite o titulo do livro: ')
                print('-' * 30)
                autor = input('Digite o nome do autor: ')
                print('-' * 30)
                editora = input('Digite o nome da editora: ')
                self.ctrl_livro.create_livro(titulo, autor, editora)
                print('Livro inserido!')
                print('-' * 30)
                print('| Nome: {}', usuario.nome)
                print('| Email: {}', usuario.email)
                print('| Senha: {}', usuario.senha)
                print('-' * 30)
            elif opcao == '2':
                print('-' * 30)
                lista = self.ctrl_usuario.get_users()
                if lista == []:
                    print('Não existe nenhum usuário cadastrado, por favor cadastre um usuário!')
                self.show_users(lista)
                nome = input('Digite o nome do usuário desejado: ')
                usuario = self.ctrl_usuario.get_user_by_nome(nome)
                lista2 = self.ctrl_livro.get_livros()
                if lista2 == []:
                    print('Não existe nenhum livro cadastrado, por favor cadastre um livro!')
                    continue
                self.show_livros(lista2)
                nome2 = input('Digite o nome do livro desejado: ')
                livro = self.ctrl_livro.get_livro_by_nome(nome2)
                data_de_emprestimo = date.today()
                prazo = timedelta(days=+7)
                data_de_devolucao = data_de_emprestimo + prazo
                emprestimo = self.ctrl_emprestimo.create_emprestimo(usuario, livro, data_de_emprestimo,
                                                                    data_de_devolucao)
                if emprestimo is not None:
                    print('Empréstimo feito!')
                    print('-'*30)
                    print('| Usuario: {}'.format(emprestimo.usuario.nome))
                    print('| Livro: {}'.format(emprestimo.livro.titulo))
                    print('| Data de Empréstimo: {}'.format(emprestimo.data_de_emprestimo))
                    print('| Data de Devolução: {}'.format(emprestimo.data_de_devolucao))
                    print('-'*30)
                else:
                    print('O livro já está alugado!')
            elif opcao == '9':
                print('O sistema será desligado!')
                break
            else:
                print('Opção inválida!')

    def show_users(self, lista):
        for user in lista:
            print('-'*30)
            print('| Nome: {}'.format(user.nome))
            print('| Email: {}'.format(user.email))
            print('-'*30)

    def show_livros(self, lista):
        for livro in lista:
            print('-'*30)
            print('| Titulo: {}'.format(livro.titulo))
            print('| Autor: {}'.format(livro.autor))
            print('| Editora: {}'.format(livro.editora))
            print('-'*30)

    def print_menu(self):
        print('Que tipo de operação deseja realizar?')
        print('0 - Criar novo usuário')
        print('1 - Inserir novo livro')
        print('2 - Criar novo empréstimo')
        print('9 - Sair')
