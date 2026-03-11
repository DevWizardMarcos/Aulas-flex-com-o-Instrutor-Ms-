
# # # # nomes = ['Marcos','Gabriel','Ricardo','Juliano','Pablo']


# # # # for n in range(len(nomes)):
# # # #     print(f'o nome que esta na posiçao {n} é {nomes[n]}')



# # # nomes = ['Marcos','Gabriel','Ricardo','Juliano','Pablo']

# # # nomes.append('Thigas') #adiciona no final da lista 

# # # print(nomes)

# # # nomes.insert(2,'Peter') #adciona pelo index 

# # # print(nomes)

# # # print(nomes.count('Marcos')) #quantos tem na lista

# # # print(nomes.index('Peter')) #qual nome esta na posição

# # # nomes.pop() #remove o ultimo elemento 

# # # print(nomes)

# # # nomes.remove('Juliano') # remove pelo nome 
# # # print(nomes)

# # # print(len(nomes))


# # # nomes2 = nomes.copy() #copia 
# # # nomes.clear() #limpa tudo 
# # # print(nomes)
# # # print(nomes2)


# # # nome = 'Marcos'

# # # print(len(nome))


# # # print(nomes2[0::2]) #fatiamento
# # # print(nomes2[0:2]) #fatiamento
# # # print(nomes2[0::]) #fatiamento





# # # # nomes = ['Marcos','Gabriel','Ricardo','Juliano','Pablo']


# # # # for n in range(len(nomes)):
# # # #     print(f'o nome que esta na posiçao {n} é {nomes[n]}')



# # # nomes = ['Marcos','Gabriel','Ricardo','Juliano','Pablo']

# # # nomes.append('Thigas') #adiciona no final da lista 

# # # print(nomes)

# # # nomes.insert(2,'Peter') #adciona pelo index 

# # # print(nomes)

# # # print(nomes.count('Marcos')) #quantos tem na lista

# # # print(nomes.index('Peter')) #qual nome esta na posição

# # # nomes.pop() #remove o ultimo elemento 

# # # print(nomes)

# # # nomes.remove('Juliano') # remove pelo nome 
# # # print(nomes)

# # # print(len(nomes))


# # # nomes2 = nomes.copy() #copia 
# # # nomes.clear() #limpa tudo 
# # # print(nomes)
# # # print(nomes2)


# # # nome = 'Marcos'

# # # print(len(nome))


# # # print(nomes2[0::2]) #fatiamento
# # # print(nomes2[0:2]) #fatiamento
# # # print(nomes2[0::]) #fatiamento





# # # quantidade = int(input('Digite a quantidade de produtos que deseja colocar : '))

# # # produtos = []


# # # for q in range(quantidade):
# # #     nomeProduto = input(f'digite o {q + 1 } - produto : ')
# # #     produtos.append(nomeProduto)
# # #     valorProduto = int(input(f'digite o {q + 1 } - valor : '))
# # #     produtos.append(valorProduto)
# # #     remover = input(f'Deseja remover algum produto : {produtos}')

# # #     if remover == 's':
# # #         removendo = input(f'Digite o nome do produto que deseja remover : {produtos} ')
# # #         produtos.remove(removendo)
# # # for lista in produtos:
# # #     print(lista)



# # nomes = ('Marcos', 'Gabriel', 'Ricardo')

# # print(nomes.count('Marcos'))
# # print(nomes.index('Gabriel'))



# # transformar = list(nomes)

# # print(transformar)

# # transformar2 = tuple(transformar)

# # print(transformar2)



# # numeros = ()

# # transformar3 = 10,20


# # numeros = transformar3


# # print(numeros)


# # funcionarios = [
# #     ('Joao', 'Dev', 5000),
# #     ('Maria', 'Analista', 4500),
# #     ('Pedro', 'Gerente', 7000)

# # ]

# # for  nome, cargo, salario in funcionarios:
# #     print(f'o nome é {nome} o cargo é {cargo} e salario {salario} ')


# # salarios = [s[2] for s in funcionarios]  # Extrai só os salários
# # maior = max(salarios)
# # menor = min(salarios)
# # total = sum(salarios)
# # print(f'o maior salario é {maior} o menor é {menor} e o total é {total}')


# funcionarios = (
#     ('Joao', 120, 5000),
#     ('Maria', 140, 4500),
#     ('Pedro', 180, 7000)

# )


# maiorValor = 0

# maiorQuantidade = 0

# for nome, quantidade ,valor in funcionarios:
#     if quantidade >= maiorQuantidade:
#         maiorValor = valor
#         maiorQuantidade = quantidade
# print(f'o maior  valor é {maiorValor} e quantidade é {maiorQuantidade}') 


# nomes = ('Marcos','Gabriel','Pablo')

# print(nomes[2])


# print(type(nomes))


# nomes = ('')


# print(type(nomes))


# print(nomes[0])


# frutas = ('Laranja','Uva','Pera','Abacaxi','Banana')

# perguntar = 'Banana'


# if perguntar in frutas:
#     print(f'rapz possui {frutas.count(perguntar)} uma  ')
# else:
#     print('nao possui')