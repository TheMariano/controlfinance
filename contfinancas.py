import sys, random, string, os, csv

filename = "controle.csv"
controle = 0
saldo = 0

if os.path.exists(filename):
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            if not row or row[0] == "Tipo":
                continue
            tipo = row[0]
            valor = float(row[1])
            if tipo == "d":
                saldo -= valor
            elif tipo == "r":
                saldo += valor
else:
    with open(filename, "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Tipo", "Valor", "Descrição", "Saldo"])
        writer.writerow([controle])

print("   [+] Controle de Finanças [+]")
print("   [ 1 ] > Gerenciar Finanças")
print("   [ 2 ] > Limpar histórico de Finanças")
print("   [ 3 ] > Sair do programas")
print(f'Seu saldo atual é: {saldo}')

print("")
print("By: TheMariano")
A = input("Alternativa: ")

if A == "1" or A == "01":
 while True:
    print("[+] Gerenciar Finanças [+]")
    valor = float(input("[+] Digite o valor: "))
    tipo = input("Digite 'd' para despesa ou 'r' para receita: ")
    descricao = input("Digite a descrição da transação: ")

    if tipo == "d":
        controle -= valor
    elif tipo == "r":
        controle += valor
    else:
        print("Entrada inválida, por favor digite 'd' para despesa ou 'r' para receita.")
        continue
    with open(filename, "a") as file:
        writer = csv.writer(file)
        writer.writerow([tipo, valor, descricao, controle])
    continuar = input("Deseja continuar digitando valores? (s/n)")
    if continuar.lower() != "s":
        break

if A == "2" or A == "02":

    clear = input("Você deseja limpar os valores do arquivo? (s/n)")
    if clear == "s":
        with open(filename, "w") as file:
            file.write("")

elif A == "3" or A == "3":
    sys.exit()