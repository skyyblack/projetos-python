class Pessoa:
    def __init__(self,nome: str,idade: int):
        self.nome = nome
        self.idade = idade

    def __repr__(self):
            attrs = f'({self.nome!r}, {self.idade!r})'
            return attrs

class Leitor(Pessoa):
    def __init__(self, nome, idade):
        super().__init__(nome, idade)