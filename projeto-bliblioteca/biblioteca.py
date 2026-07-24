from pessoa import Leitor
from livro import Livro

class Biblioteca:
    def __init__(self,):
        self.lista_de_livros = []
        self.lista_de_leitores = []

    def adicionar_livro(self,livro):
        self.lista_de_livros.append(livro)
        return True
    
    def adicionar_leitor(self, leitor):  
        return self.lista_de_leitores.append(leitor)
    
    def emprestar_livro(self,leitor, livro):
        if not livro.emprestado:
            if livro in self.lista_de_livros:
                print('livro emprestado')
                livro.emprestado = True
                return

        print('livro ja foi emprestado')
        return 


    def devolver_livro(self, livro, leitor): 
        livro_devolvido = livro
        self.lista_de_livros.remove(livro)
        print(f'o livro: {livro_devolvido!r}  foi devolvido!')
        return False

    def __repr__(self):
        attrs = f'({self.lista_de_livros!r}, {self.lista_de_leitores!r})'
        return attrs

    def indict(self):
        livros = [livros.__dict__ for livros in self.lista_de_livros]
        leitor = [leitor.__dict__ for leitor in self.lista_de_leitores]
        array = [
            {
                "leitores": leitor,
                "livros": livros,
            }
        ]
        return array

       
            

        
            


# if __name__ == '__main__':
#     p1 = Leitor('matheus', 20)
#     l1 = Livro('python', 'matheus')
#     b = Biblioteca()

#     b.adicionar_leitor(p1)
#     b.adicionar_livro(l1)
#     b.emprestar_livro(p1,l1)
#     # b.devolver_livro(l1,p1)

#     p2 = Leitor('joao', 19)
#     l2 = Livro('santania', 'matheus')
#     b.adicionar_leitor(p2)
#     b.adicionar_livro(l2)
#     b.emprestar_livro(p2,l1)

#     # b.devolver_livro(l2,p2)
#     # print(b)

    
#
