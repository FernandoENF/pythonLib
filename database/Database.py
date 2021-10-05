class Database:
    def __init__(self):
        self.livros = []
        self.emprestimos = []
        self.usuarios = []

    def add_livro(self, livro):
        self.livros.append(livro)

    def add_user(self, user):
        self.usuarios.append(user)

    def get_user_by_nome(self, nome):
        for user in self.usuarios:
            if nome == user.nome:
                return user
        return None

    def get_livro_by_nome(self, titulo):
        for livro in self.livros:
            if titulo == livro.titulo:
                return livro
        return None

    def get_livros(self):
        return self.livros

    def get_users(self):
        return self.usuarios

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def consultar_livro(self, target_livro):
        for livro in self.livros:
            if livro == target_livro:
                return True
        return False
