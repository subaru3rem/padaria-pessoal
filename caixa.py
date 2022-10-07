def ProdutosList(produtos):
    for i in produtos:
        if i[3] >= 1:
            print(i[0],":","R$",i[2])  
def compras(produtos):
    compras = [0]  
    
    o = 1
    while o != 0:
      x = input("item q deseja comprar: ")
      y = 0
      f = 1
      for i in produtos:
         if x == i[0]:
            while f != 0:
             y = int(input("quantidade: "))
             if i[3] >= y:
                 compras[0] = i[2]*y+compras[0]    
                 compras.append([i[0],y,i[2]])
                 i[3] = i[3]-y  
                 f = 0
                 o = 0
             else:
                 print("quantidade do item excedida!")
      if f == 1:
        print("item não encontrado")
        input()
    compras[0] = [compras[0]]
    return compras
def nota(compras):
    for i in compras:
          if len(i) <= 2:
            compras[0]=[i[0]+compras[0][0]]
            compras.remove(i)
    for i in compras:
        if len(i) >=2:
           print(i[0],"x",i[1]," valor: R$",i[1]*i[2])
    print("valor a pagar: R$", compras[0][0])
    compras.insert(0,[0])
def cancel(compras):
    x = input("item que deseja cancelar: ")
    for i in compras:
        if i[0] == x:
            compras[1] = [compras[1][0]-i[1]*i[2]]
            compras.remove(i)
    for i in compras:
      if len(i) >= 2:
        print(i[0],"x",i[1]," valor: R$",i[1]*i[2])
        print("valor a pagar: R$",compras[1][0])
def troco(compras): 
    y = 1
    while y != 0:
        x = float(input("valor recebido: R$"))
        if x >= compras[1][0]:
            return float(x-compras[1][0])
            y = 0
        else:
            print("valor insuficiente")