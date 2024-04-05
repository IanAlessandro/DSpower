nome = input("Digite seu nome: ")
negativado = input("Você está negativado? (s/n): ").lower() == 'n'
tem_emprego = input("Você possui emprego? (s/n): ").lower() == 's'
tem_salario = input("Você possui salário? (s/n): ").lower() == 's'
tem_casa_propria = input("Você possui casa própria? (s/n): ").lower() == 's'

# Verificar se o cliente atende aos critérios para concessão de crédito
if not negativado and tem_emprego and tem_salario and tem_casa_propria:
    salario_declarado = float(input("Digite seu salário: "))
    if salario_declarado * 1.5 > 0:
        print(f"Parabéns, {nome}! Seu crédito foi aprovado.")
    else:
        print("Desculpe, não podemos conceder o crédito neste momento.")
else:
    print("Desculpe, não podemos conceder o crédito neste momento.")