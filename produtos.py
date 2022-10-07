def cadastro():
    nome = input("nome do produto: ")
    codigo = input("codigo do produto: ")
    valor = float(input("valor do produto: R$"))
    quantidade = int(input("quantidade do produto: "))
    return [nome, codigo, valor, quantidade]
def exibir(produtos):
    for i in produtos:
        print("nome: ", i[0])
        print("codigo: ", i[1])
        print("valor: R$", i[2])
        print("quantidade: ", i[3])
def adicionar(produtos):
    x = input("qual o codigo do item que você deseja alterar? ")
    o = 1
    for i in produtos:
       if i[1] == x:
        y = int(input("atualizar quantidade: "))
        z = i[3]+y
        i[3] = z
        o = 0
        return i
    if o == 1:
     print("item não encontrado")
     item = input("cadastrar novo item?\ns - sim n - não: ")
     if item == "s":
        produtos.append(cadastro())
        return(produtos)
def retirar(venda,produtos):
    for i in venda[2:]:
        for x in produtos:
            if i[0] == x[0]:
                x[3]-i[2]
def verificação(produtos):
    for i in produtos:
     if i[3] <= 10:
        print("produto:",i[0],"está com baixa quantidade")