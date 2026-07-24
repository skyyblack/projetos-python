class Livro:
    def __init__(self,titulo: str,
            autor: str ):
        self.titulo = titulo
        self.autor = autor
        self.emprestado = False

    def detalhes(self):
        print(f'livro escolhido: {self.titulo}, do autor: {self.autor}')

    def __repr__(self):
            attrs = f'({self.titulo!r}, {self.autor!r})'
            return attrs
                
if __name__ == '__main__':
    l = Livro('leonardo dicaprio', 'leo dicaprio')
    l.detalhes()