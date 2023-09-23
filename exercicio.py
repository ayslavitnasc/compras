salario = float(input("Digite o valor do seu salario: "))
cota = 1250
if salario > cota:
  conta = (salario * 0.10) + salario
  print(f"Seu salario atual é de R${conta}")
elif salario <= cota:
  conta2 = (salario * 0.15) + salario
  print(f"Seu salario atual é de R${conta2}")