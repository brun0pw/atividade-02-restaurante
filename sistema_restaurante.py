"""
Informe o número da turma: 
Turma - 93313

Nome completo dos componentes.
1 - Bruno Henrique Alves Santos
2 - 
"""
import os
# Limpa o terminal.
os.system("cls || clear") 

# Definindo a função para forma de pagamento
def forma_de_pagamento(valor_total, pagamento):
    if pagamento == 1:
        desconto = valor_total * 0.10  # Desconto de 10%
        valor_final = valor_total - desconto
        print("A forma de pagamento foi à vista.")
        print(f"O subtotal foi de: R$ {valor_total:.2f}")
        print(f"O desconto foi de: R$ {desconto:.2f}")
        return valor_final, desconto
    elif pagamento == 2:
        acrescimo = valor_total * 0.10  # Acréscimo de 10%
        valor_final = valor_total + acrescimo
        print("A forma de pagamento foi no cartão.")
        print(f"O subtotal foi de: R$ {valor_total:.2f}")
        print(f"O acréscimo foi de: R$ {acrescimo:.2f}")
        return valor_final, acrescimo
    else:
        return "Método inválido", 0

# Criando uma lista que tenha código, nome do prato e valor
Cardapio = [
    {"Código do prato": 1, "Nome": "Feijoada", "Valor": 60.0},
    {"Código do prato": 2, "Nome": "Buchada", "Valor": 50.0},
    {"Código do prato": 3, "Nome": "Mocofato", "Valor": 45.0},
    {"Código do prato": 4, "Nome": "Dobradinha", "Valor": 40.0},
    {"Código do prato": 5, "Nome": "Panelada", "Valor": 35.0},
    {"Código do prato": 6, "Nome": "Baião de dois", "Valor": 30.0},
    {"Código do prato": 7, "Nome": "Caldo de sururu", "Valor": 25.0}
]

# Lista para armazenar os valores dos pratos escolhidos
valores_pedidos = []
pratos_escolhidos = []

# Perguntando ao usuário se ele vai querer ver o cardápio
vercadapio = int(input("""
=== BEM-VINDO AO RESTAURANTE DE COMIDAS TÍPICAS ===
             DESEJA VER O CARDÁPIO? 
                 1 - SIM
                 2 - NÃO
"""))
os.system("cls || clear")

# Caso sim, ele mostra o cardápio
if vercadapio == 1:
    while True:
        # Mostra o cardápio
        for menu in Cardapio:
            print(f"| Código do prato: {menu['Código do prato']} | Nome: {menu['Nome']} | Valor: R$ {menu['Valor']} |")
        
        valor_total = sum(valores_pedidos)  # Cálculo do subtotal
        escolha = int(input("Digite o código do seu pedido: \nCaso não deseje pedir nada, digite 0\n"))

        # Caso o pedido seja inválido
        if escolha < 0 or escolha > 7:
            print("Código inválido")
        elif escolha == 0:
            print("=== FIM ===")
            break
        else:
            valor_prato = Cardapio[escolha - 1]["Valor"]
            valores_pedidos.append(valor_prato)  # Adicionando o valor do prato à lista
            pratos_escolhidos.append(Cardapio[escolha - 1])  # Adicionando o prato à lista de escolhidos
            print(f"Código escolhido: {Cardapio[escolha - 1]['Código do prato']} | Nome: {Cardapio[escolha - 1]['Nome']} | Valor: R$ {valor_prato}")
            os.system("cls || clear")
            # Pergunta se o cliente deseja pedir mais
            if input("Deseja pedir mais alguma coisa? (S/N) ").strip().upper() != "S":
                break

# Caso não, o código encerra
else:
    print("=== FIM ===")

# Pede a forma de pagamento
pagamento = int(input("""
=== PAGAMENTO ===
Digite sua forma de pagamento:
   1 - para Dinheiro
   2 - para Cartão         
"""))

# Calculando o valor final e o desconto/acréscimo
valor_final, ajuste = forma_de_pagamento(valor_total, pagamento)

# Exibindo todas as informações
print("\n=== RESUMO DO PEDIDO ===")
print("Pratos escolhidos:")
for prato in pratos_escolhidos:
    print(f"- {prato['Nome']} (Código: {prato['Código do prato']}, Valor: R$ {prato['Valor']})")

print(f"\nSubtotal: R$ {valor_total}")
print(f"Forma de pagamento: {'Dinheiro' if pagamento == 1 else 'Cartão'}")
print(f"Desconto ou acréscimo aplicado: R$ {ajuste}")
print(f"O valor final a pagar é: R$ {valor_final}")


