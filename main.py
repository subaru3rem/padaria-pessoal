import produtos, caixa

escolha=""
prod=[]
compras = [[0]]

while escolha !="0":
  print("Menu")
  print("1 - Estoque")
  print("2 - caixa")
  print("0 - Fim")
  escolha=input("Escolha uma opção: ")
  if escolha =="0":
    escolha=input("Tem certeza que quer sair?\n 0 - Sim , 5 - Não\n")
  elif escolha =="1":
    cad = ""
    while cad !="0":
      cad = input("1 - para cadastrar novo produto\n2 - para adicionar itens a produtos existentes\n3 - para visualizar estoque\n0 - para retornar\n")
      if cad == "1":
        prod.append(produtos.cadastro())
      elif cad == "2":
        produtos.adicionar(prod)
      elif cad == "3":
        produtos.exibir(prod)
      elif cad == "0":
        print("retornando...")
  elif escolha == "2":
    cad = ""
    while cad != "0":
      produtos.verificação(prod)
      cad = input("bem vindo a padaria sonhos\ndigite 1 para começar as compras: ")
      if cad == "1":
        gta = ""
        caixa.ProdutosList(prod)
        while gta !="s": 
         for i in caixa.compras(prod):
           compras.append(i)
         caixa.nota(compras)
         gta = input("finalizar compra?\ns - sim\nn - não\n")
         if gta == "cancel":
          caixa.cancel(compras)
          gta = input("finalizar compra?\ns - sim\nn - não\n")
        print("troco: R$",caixa.troco(compras))
        input()
        produtos.retirar(compras,prod)
        print("finalizando compra...")
        compras.clear()
        compras.append([0])
