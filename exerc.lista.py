'''
frutas = ["maçã","banana", "uva"]
numeros = [1,2,3 ,4]
#Acessando elementos
print("Primeira fruta:",frutas[0])   # "macã"
print("Ultima fruta:", frutas[-1])   # "uva"

#Alternando elementos
frutas[1] = "banana-nanica"
print("Após alterar:",frutas)

# Adicionando elementos 
frutas.append("morango")
frutas.insert(1, "pera")
print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("uva")
ultima = frutas.pop()
print("Após remover uva e pop():", frutas, "/ Última removida:", ultima)
'''

# exercício lista 
lista_compras = ["macarrão","açucar","feijão" "arroz"]
itens = [1,2,3,4]

# acessando os itens
print("Primeiro itens:",lista_compras [0]) # macarrão
print("ultimo itens:", lista_compras[-1]) # arroz

# alternando iten
macarrao[-1] = "macarrão-parafuso"
print("Após alterar:", itens)

# Adicionando iten
itens.append("fubá")
itens.insert(1,"sal")
print("Após adicionar:", itens)

# Removendo iten
itens.remove("arroz")
ultimo = itens.pop()

