import platform
import os
#-----------------------------------------------------------------------------
#                           Variaveis padrões 
#
entrada = "\n Insira qualquer tecla para continuar : "
barras = 30 * "-"
banner = '''
                ***************************************************
                *                                                 *
                *            GERENCIADOR DE VENDAS                *
                *                                                 *
                ***************************************************
'''
# Criador         : Brayan vieira 
# função          : Um sistema pratico e simples de gerenciamento de vendas 
# versão          : 1.0
# data da criação : 20/2/2024
#-----------------------------------------------------------------------------
#                       Menu de escolha do programa

#-----------------------------------------------------------------------------
#                           Função ver os registros salvos 
def ver_os_registros():
    limpador()
    with open("registro_de_vendas.txt", "r", encoding="utf-8") as Total_vendas:
        vendas_totais = Total_vendas.read()
        print(vendas_totais)
        return input(entrada)
#-----------------------------------------------------------------------------
#                               Função para limpar a tela
def limpador():
#                       detectando o sistema para fazer o clear 
    sistema_operacional = platform.system()
    if sistema_operacional == "Windows":
        limpador = "cls"
    elif sistema_operacional == "Linux" or "Mac":
        limpador = "clear"
    return os.system(limpador)
#-----------------------------------------------------------------
#                   verificando se o arquivo esta criado 
def verificar_arquivo():
    try:
        with open("registro_de_vendas.txt", "r") as testando:
            a = testando.readline()
    except FileNotFoundError:
        with open("registro_de_vendas.txt", "w") as testando:
            testando.write("\n")
#-----------------------------------------------------------------------------
#                               inserindo arquivos no nosso registro 
def adicionar_registros():
#-----------------------------------------------------------------------------
#                               input de dados
        limpador()
        nome = input(" \n Insira o nome do cliente :  ")
        pecas = input(" \n Insira a peça/produto vendido : ")
        limpador()
        data = input(" \n Insira a data da venda : ")
        tipo_pagamento = input("\n Insira o metodo de pagamento usado : ")
        limpador()
#-----------------------------------------------------------------------------
#                       verificando erros de valor 
        try:
            valor_total = float(input(" \n insira o valor total de gastos \n \n Ex : peças,Frete \n \n Insira R$ : "))
            limpador()
            valor_lucro = float(input(" \n quanto você teve de lucro líquido ? R$ : "))
            Nfe = int(input(" \n Insira o número da Nfe : "))
        except ValueError:
            print(" \n \n Erro, Insira somente numeros \n ")
            exit()
#-----------------------------------------------------------------------------
#                           pegando o lucro liquido 
        lucro_liquido = valor_lucro - valor_total
#-----------------------------------------------------------------------------
#                            criando um dicionario de informações 
#
        informacoes_de_venda ={"registro de venda": {
                                "nome do cliente": nome,
                                "data da venda": data,
                                "tipo de pagamento": tipo_pagamento,
                                "peças vendidas": pecas,
                                "Numero da nota fiscal":Nfe,
                                "gasto R$": valor_total,
                                "lucro liquido R$": lucro_liquido,
                                }}
#-----------------------------------------------------------------------------
#                       abrindo o arquivo e adicionando os valores 
#
        with open("registro_de_vendas.txt", "a", encoding="utf-8") as arquivo:
            arquivo.write("\n \n ")
            arquivo.write(barras)
#-----------------------------------------------------------------------------
#                          percorrendo os dados 
#
            for indice, total in informacoes_de_venda.items():
                for chave, valores in total.items():
#-----------------------------------------------------------------------------
#                       adicionando no arquivo 
#
                    arquivo.write(f"\n {chave} : {valores} ")
                return True
#-----------------------------------------------------------------------------
#                   função calcular todo o lucro liquido 
def lucro_total():
    lucro_calculado = 0.0
#-----------------------------------------------------------------------------
#                       abrindo o arquivo para leitura
    with open("registro_de_vendas.txt", "r") as arquivo:
#-----------------------------------------------------------------------------
#                       acessando cada valor 
        for linha in arquivo:
#-----------------------------------------------------------------------------
#                   Verificando a linha do lucro 
            if "lucro liquido" in linha:
#-----------------------------------------------------------------------------
#                       separando o texto do valor 
                indice, liquido = linha.split(":")
#-----------------------------------------------------------------------------
#                          calculando todo o lucro 
                lucro_calculado += float(liquido.strip())
                limpador()
#-----------------------------------------------------------------------------
#                               mostrando o lucro total 
    return input(f" \n \n O seu lucro Total e : {lucro_calculado} R$ \n \n {entrada}")
#-----------------------------------------------------------------------------
#                   Função apagar toda a lista 
def apagar_toda_lista():
#-----------------------------------------------------------------------------
#                    abrindo o arquivo 
    limpador()
    certeza = input("Você têm certeza que deseja apagar tudo ? [ S ] Sim | [ N ] Não : ").lower().startswith("s")
    if certeza:
        with open("registro_de_vendas.txt", "w") as arquivo:
            limpador()
            print("Apagado com sucesso..... ")
            return input(entrada)
    print(" \n Operação cancelada..... \n ")
    input(entrada)
while True:
    verificar_arquivo()
    limpador()
#-----------------------------------------------------------------------------
#                                   Variaveis do Menu
    menu = " \n             [A] adicionar vendas            | [V] Ver vendas registradas \n             [D] Deletar todos os registros  | [L] Ver todo o lucro liquido registrado \n "
    print(banner)
    menu = input(f" \n              Menu : \n {menu} \n \n              \n insira : ").lower()
#-----------------------------------------------------------------------------
#                               Opçoes do menu 
    match menu:
        case "a":
            adicionar_registros()
        case "v":
            ver_os_registros()
        case "d":
            apagar_toda_lista()
        case "l":
            lucro_total()
        case _:
            print(" \n Você inseriu um caracter invalido ")
            input(" \n \n Insira qualquer tecla para continuar : ")
