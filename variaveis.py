"""
nome = "Jose"
numero = 6
troco = 4.65
is_login = True # sempre com letra maiuscula True.
print(type(nome))
print(type(numero))
print(type(troco))
print(type(is_login))
"""
nomes = ["Maria","João","Fabio","Ana","Zé",]
print(type(nomes)) # mostrar o tipo da lista.
print(nomes) #mostrar a lista.
print(nomes.pop())#mostrar posição 2.
print(nomes)#exclui a ultima posição e mostra o nome.
nomes.pop()#mostra a lista novamente.
print(nomes)#exclui a ultima posição.
nomes.append("Ana")#Adiciona um nome no final da lista.
nomes.append("Lorenzo")
print(nomes)


for x in nomes:
    print(x)
