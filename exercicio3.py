valor = float(input("Insira o valor da casa a comprar? "))
salario = float(input("Digite o valor do seu salario: "))
anos_pagar = int(input("Em quantos anos voce dejesa pagar o valor da casa? "))
meses = anos_pagar * 12
porcentagem = salario * 0.30
prestacao = valor / meses
if prestacao <= porcentagem:
  print(f"O emprestimo bancario foi aprovado, pois o valor da prestaçao mensal R${int(prestacao)} nao foi superior a 30% do seu salario")
else:
  print("Nao funcionou")