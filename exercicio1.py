var = float(input("Qual a distancia que voce deseja percorrer em KM? "))
if var <= 200:
  conta = var * 0.50
  print(f"Valor da passagem: R${conta} reias")
elif var > 200:
  conta1 = var * 0.40
  print(f"Valor da passagem: R${conta1} reais")  