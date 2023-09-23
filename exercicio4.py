

energia = int(input("Quantidade de KWh consumida? "))
instalacao = input("Qual o tipo de instalaçao feita ? \n [Insira R para residencias] \n [Insira I pçara industrias] \n [Insira C para comercios] \n")
sai = 'sim'
while sai != "nao":
  if instalacao == "R" or instalacao == "r":
    if energia <= 500:
      conta1 = energia * 0.40
      print(f"Valor total a pagar: R${int(conta1)}")
      break
    elif energia > 500:
      conta2 = energia * 0.65
      print(f"Valor total a pagar: R${int(conta2)}")
      break
  elif instalacao == "C" or instalacao == "c":
    if energia <= 1000:
      conta3 = energia * 0.55
      print(f"Valor total a pagar: R${int(conta3)}")
      break
    elif energia > 1000:
      conta4 = energia * 0.60
      print(f"Valor total a pagar: R${int(conta4)}")
      break
  elif instalacao == "I" or instalacao == "i":
    if energia <= 5000:
      conta5 = energia * 0.55
      print(f"Valor total a pagar: R${int(conta5)}")
      break
    elif energia > 5000:
      conta6 = energia * 0.60
      print(f"Valor total a pagar: R${int(conta6)}")
      break
  else:
    print("Erro no sistema! \n Tente novamente.")
  sai = input("Tentar novamente ? \n Sim[0] \n Nao[1] \n")
  continue
 
