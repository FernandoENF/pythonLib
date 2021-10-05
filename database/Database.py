class Database:
    def __init__(self):
        self.livros = []
        self.emprestimos = []
        self.usuarios = []

    def add_livro(self, livro):
        self.livros.append(livro)

    def add_user(self, user):
        self.usuarios.append(user)

    def add_emprestimo(self, emprestimo):
        self.emprestimos.append(emprestimo)

    def consultar_livro(self, target_livro):
        for livro in self.livros:
            if livro == target_livro:
                return True
        return False
