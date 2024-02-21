# Criador         : Brayan vieira 
# função          : Um sistema pratico e simples de gerenciamento de vendas 
# versão          : 1.0
# data da criação : 20/2/2024
import arquivos_adicionais as extern
#-----------------------------------------------------------------------------
#                       Menu de escolha do programa
while True:
    extern.limpador()
#-----------------------------------------------------------------------------
#                                   Variaveis do Menu
    menu = " \n             [A] adicionar vendas            | [V] Ver vendas registradas \n             [D] Deletar todos os registros  | [L] Ver todo o lucro liquido registrado \n "
    print(extern.banner)
    menu = input(f" \n              Menu : \n {menu} \n \n              \n insira : ").lower()
#-----------------------------------------------------------------------------
#                               Opçoes do menu 
    match menu:
        case "a":
            extern.adicionar_registros()
        case "v":
            extern.ver_os_registros()
        case "d":
            extern.apagar_toda_lista()
        case "l":
            extern.lucro_total()
        case _:
            print(" \n Você inseriu um caracter invalido ")
            input(" \n \n Insira qualquer tecla para continuar : ")