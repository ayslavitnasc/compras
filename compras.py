
#opçoes a ser digitadas no primeiro input (1 ou 2).
#opçoes a ser digitada no pirmeiro bloco "if" (arroz ou feijao),(entre outras coisa que sera facil o usuario interpretar).
#opçoes a ser digitada no segundo bloco "elif" (alvejante ou amaciante), (entre outras coisa que sera facil o usuario interpretar).

atendimento = int(input("digite 1 se for pordutos alimenticios, digite 2 se for produtos de limpeza."))
if(atendimento == 1):
      produto = input("Digite o nome do produto:")
      if(produto == "arroz"):
        print("o preço do arroz é R$4.50 a unidade e R$180 o fardo.")
        var = input("unidade ou fardo?")
        if(var == 'unidade'):
          print("Nao tem desconto em unidade")
          uni = int(input("Quantas unidades de arroz deseja?"))
          soma = uni * 4.50
          print("o total de", uni,"unidade(s) de arroz é de", soma)     
          voltarMenuPrincipal = str(input("Desseja voltar ao menu principal? (s/n)")).lower
        elif(var == "fardo"):
          des = 180 * (5 / 100)
          sub = 180 - des
          print("o fardo de arroz tem 5% de desconto o preço final do produto é", int(sub))
      elif(produto == "feijao"):
          print("a unidade é R$9.50 o saco com 60kg é R$310")
          var1 = int(input("ser for em unidade digite -unidade- se for em saco digite em kg:"))
          if(var1 == "unidade"):
            print("nao tem desconto em unidade")
          elif(var1 <= 30):
            print("sem desconto!") 
          elif(var1 > 30 or var1 <= 60 ):
            des1 = 310 * (5 / 100)
            sub1 = 310 - des1
            print("voce obeteve 5% de desconto em",var1," kilos de feijao, o prelo final é de R$",sub1)
elif(atendimento == 2):
      produto2 = input("Insira o nome do produto:")
      if(produto2 == "alvejante"):
        print("o alvejante de 1L é de R$5.80")
        uni1 = int(input("Quantas unidades?"))
        soma1 = uni1 * 5.80
        print("o total de", uni1,"alvejante(s) é de", soma1)
      elif(produto2 == "amaciante"):
        print("O amaciante de 500ml é de R$4.90")
        uni2 = int(input("Quantas unidades?"))
        soma3 = uni2 * 4.90
        print("O total de", uni2,"amaciante de 500ml é de", soma3)
else:
    print("opçao invalida.")
   

