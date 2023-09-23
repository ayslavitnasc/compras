num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))
operacao = input("Qual operaçao deseja realizar? ")
if operacao == "soma":
  conta = num1 + num2
  print(f"O resultado desta operaçao é {conta}")
elif operacao == "subtraçao":
  conta1 = num1 - num2
  print(f"O resultado desta operaçao é {conta1}")
elif operacao == 'multiplicaçao':
  conta2 = num1 * num2
  print(f"O resultado desta operaçao é {conta2}")
elif operacao == "divisao":
  conta3 = num1 / num2
  print(f"O resultado desta operaçao é {conta3}")  
else:
  print("Operaçao invalida") 