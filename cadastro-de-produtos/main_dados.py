from os import removedirs

from db import cursor, connection, sql, TABLE_NAME

produtos = []


def listar_produtos(lista_produtos):
    for i, produtos in enumerate(lista_produtos):
        i+=1
        print('ID:', i, '-', 'Produto:', produtos['nome do produto'], '/', 'Preço:', produtos['preço'],  '/', 'Estoque:', produtos['estoque'])

    return 'nada pra listar'
def cadastrar_produto(user_nome_produto: str, user_preco: int | float, user_estoque: int, lista_produtos):  
        list = [
            {
            'nome do produto': user_nome_produto,
            'preço': user_preco,
            'estoque': user_estoque,  
            }
        ]
        lista_produtos+=list

def atualizar_produtos(user_id, user_estoque, lista_produtos):
    for i, produto in enumerate(lista_produtos):
        i+=1
        if user_id == i:
            produto['estoque'] = user_estoque

def excluir_produto(user_id,lista_produtos):

    indice = user_id - 1
    if 0 <= indice < len(lista_produtos):
        removido = lista_produtos.pop(indice)
        print('O produto removido foi:', removido)




while True:

    user = input("=== MENU DE OPÇÕES ===\n"
        "[L] - Listar produtos\n"
        "[ADD] - Adicionar produto\n"
        "[AT] - Atualizar produto\n"
        "[R] - Remover produto\n"
        "[S] - Sair\n"
        "======================\n"
        "Digite a opção desejada: ").lower()
    

    if user == 'add':
        user_nome_produto = input('Digite o nome do produto: ')
        user_preco = float(input('Digite o preço do produto: '))
        user_estoque = int(input('Digite a quantidade de estoque desse produto: '))
        cadastrar_produto(user_nome_produto, user_preco, user_estoque, produtos)

        dados =  [
        { 
            'name_product': user_nome_produto,
            'preço': user_preco,
            'estoque': user_estoque
        }, 
        ]
        cursor.executemany(sql, dados)
        connection.commit()
         
    elif user == 'at':
        user_id = int(input('Digite o ID o produto que deseja atualizar: '))
        user_estoque = int(input('Digite a quantidade de estoque desse produto: '))
        atualizar_produtos(user_id, user_estoque, produtos)

        dados1 = { 
                'id': user_id,
                'estoque': user_estoque
            }

        dados2 = (f'UPDATE {TABLE_NAME} ' 
            'SET estoque = :estoque '
            'WHERE id = :id')
        
        cursor.execute(dados2, dados1)
        connection.commit()

    elif user == 'r':
        user_id = int(input('Digite o ID o produto que deseja remover: '))
        excluir_produto(user_id, produtos)

        dados3 = { 
            'id': user_id,
            }

        date = (f'DELETE FROM {TABLE_NAME} '
            'WHERE id = :id')
        
        cursor.execute(date, dados3)
        connection.commit()

    elif user == 'l':
        # listar_produtos(produtos)
        cursor.execute(
        f'SELECT * FROM {TABLE_NAME} '
        )

        for row in cursor.fetchall(): 
            _id, name_product, preco, estoque = row
            print(_id, name_product,preco, estoque)

    elif user == 's':
        print('Você saiu do programa. ')
        break

cursor.close()
connection.close()



            

    


