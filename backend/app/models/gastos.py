# area destinada as importações 
import datetime

gastos_usuario = {}
id_atual = 1


def entradas(): # esta função coleta e valida os dados que o usuario informar, ainda falta criar as funções de validação.
    global id_atual

    valor = input("valor R$: ")
    categoria = input("Categoria: ")
    descricao = input("Descrição: ")
    data = input("Data: ")


    if data == "":
        data = datetime.datetime.now()
    
    else:
        pass

    gastos_usuario[id_atual] = {
        "valor": valor,
        "categoria": categoria,
        "descricao": descricao,
        "data": data
    }

    id_atual += 1

    return gastos_usuario


def armazenar_gastos(): # função que vai fazer o armazenamento dos dados no banco de dados
    print('oi')


def listar(gastos_usuario): #refatorar 
    for chave, gasto in gastos_usuario.items():
        print(gasto['valor'])
        print(gasto['categoria'])
        print(gasto['descricao'])
        print(gasto['data'])
        print('---')


