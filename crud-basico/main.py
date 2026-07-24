"""
🧠 Exercício: Sistema de Tarefas com prioridades (versão evoluída)

Você vai criar um programa de terminal de tarefas, tipo o que já fez, 
mas com algumas melhorias.

📌 Regras do sistema:

Você vai trabalhar com uma lista de tarefas assim:

tarefas = []

Cada tarefa será um dicionário:

{"nome": "estudar python", "feito": False, "prioridade": 1}
⚙️ Funcionalidades obrigatórias:
1. Adicionar tarefa

O usuário digita:

adicionar estudar python 2
"estudar python" = nome
2 = prioridade

Salva assim:

{"nome": "estudar python", "feito": False, "prioridade": 2}
2. Listar tarefas

Comando:

listar

Mostra assim:

1. estudar python (prioridade 2) [PENDENTE]
2. academia (prioridade 1) [FEITO]
3. Marcar como feita

Comando:

feita 1

Marca a tarefa como:

"feito": True
4. Remover tarefa

Comando:

remover 2

Remove pelo índice.
"""
tarefas = []
def listar(lista_tarefas):
         for x, i in enumerate(lista_tarefas):
            print(x,'nome:', i['nome'],'feita:', i['feita'], 'prioridade:', i['prioridade'])
            # print('feita:', i['feita'])
            # print('prioridade:', i['prioridade'])

def adcionar_tarefas(tarefa_usuario, prioridade_usuario, lista_tarefas, feito_usuario):
        newlist = [
            {
                'nome': tarefa_usuario,
                'feita': True,
                'prioridade': prioridade_usuario ,
            }
        ] 

        lista_tarefas += newlist

        if tarefa_usuario and prioridade_usuario:
                if feito_usuario == 'nao':
                        lista_tarefas[-1]['feita'] = False
                else:
                        lista_tarefas[-1]['feita'] = True
                     
  

def alterar_tarefa(usuario_marcar_feita, lista_tarefas): 
    for  i, tarefas in enumerate(lista_tarefas):
        if usuario_marcar_feita == i:
            lista_tarefas[i]['feita'] = True
            print(*lista_tarefas)
            return
        
def remover_tarefa(usuario_marcar_feita,lista_tarefas):
            
            lista_tarefas.pop(usuario_marcar_feita)
            print(*lista_tarefas)
            return
     
while True:
    add_usuario = input('pretende adicionar uma tarefa? [S] ou [N]: ').lower()
    
    if add_usuario == 's':
        tarefa_usuario = input('Qual o nome da tarefa? ').lower()
        prioridade_usuario = int(input('qual o nivel de prioridade? Digite em numeros: '))
        feito_usuario = input('a tarefa foi feita? ').lower()
        comando_usuario = input('escolha um comando:\n'
                            'Listar, \n'
                                'alterar a tarefa(digite[A]) \n '
                                'Remover Tarefa[R]: ').lower()
        adcionar_tarefas(tarefa_usuario, prioridade_usuario, tarefas, feito_usuario)

        if comando_usuario == 'listar' or comando_usuario == 'l':
            listar(tarefas)

        elif comando_usuario == 'a':
            usuario_marcar_feita = int(input('qual indice deseja alterar? '))
            alterar_tarefa(usuario_marcar_feita, tarefas)

        elif comando_usuario == 'r':
            usuario_marcar_feita = int(input('Qual indice deseja remover? '))
            remover_tarefa(usuario_marcar_feita, tarefas)
        else:
            break

    # if comando_usuario == 'feita' + comando_usuario.isdigit():
    #     pass
