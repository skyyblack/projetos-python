from pathlib import Path
import json

from biblioteca import Biblioteca
from livro import Livro
from pessoa import Leitor

ROOT = Path(__file__).parent
NOME_ARQUIVO = ROOT / 'main.json'

p1 = Leitor('matheus', 20)
l1 = Livro('python', 'matheus')
b = Biblioteca()

b.adicionar_leitor(p1)
b.adicionar_livro(l1)
b.emprestar_livro(p1,l1)
# b.devolver_livro(l1,p1)

p2 = Leitor('joao', 19)
l2 = Livro('santania', 'matheus')
b.adicionar_leitor(p2)
b.adicionar_livro(l2)
b.emprestar_livro(p2,l1)


with open(NOME_ARQUIVO, 'w', encoding='utf-8') as file:
    json.dump(b.indict() ,file, indent=2, ensure_ascii=False)