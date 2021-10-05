class Livro:
    def __init__(self, titulo, autor, editora):
        self.__titulo = titulo
        self.__autor = autor
        self.__editora = editora
        self.__status = True

    @property
    def is_not_rented(self):
        return self.__status

    @property
    def titulo(self):
        return self.__titulo

    @titulo.setter
    def titulo(self, titulo):
        self.__titulo = titulo

    @property
    def autor(self):
        return self.__autor

    @autor.setter
    def autor(self, autor):
        self.__autor = autor

    @property
    def editora(self):
        return self.__editora

    @editora.setter
    def editora(self, editora):
        self.__editora = editora
