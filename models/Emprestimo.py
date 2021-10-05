class Emprestimo:
    def __init__(self, usuario, livro, data_de_emprestimo, data_de_devolucao):
        self.__usuario = usuario
        self.__livro = livro
        self.__data_de_devolucao = data_de_devolucao
        self.__data_de_emprestimo = data_de_emprestimo

    @property
    def usuario(self):
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        self.__usuario = usuario

    @property
    def livro(self):
        return self.__livro

    @livro.setter
    def livro(self, livro):
        self.__livro = livro

    @property
    def data_de_devolucao(self):
        return self.__data_de_devolucao

    @data_de_devolucao.setter
    def data_de_devolucao(self, data_de_devolucao):
        self.__data_de_devolucao = data_de_devolucao

    @property
    def data_de_emprestimo(self):
        return self.__data_de_emprestimo

    @data_de_emprestimo.setter
    def data_de_emprestimo(self, data_de_emprestimo):
        self.__data_de_emprestimo = data_de_emprestimo