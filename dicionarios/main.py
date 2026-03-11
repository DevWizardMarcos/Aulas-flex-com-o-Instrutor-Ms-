# # nomes = {'Nome': 'Marcos',
          
# #          'Idade' : 26, 

# #          'Altura': 1.88 
# #          }

# # print(nomes['Nome'])
# # print(nomes['Idade'])
# # print(nomes['Altura'])


# # novoNome = nomes ['Nome2'] = 'Gabriel'

# # print(nomes)

# # del nomes ['Nome']


# # if 'Marcos' in nomes:
# #     print(f'o valor da chave é {nomes["Nome"]}')



# # verificar = nomes.get('Marcos', 'nao possui esssa chave')

# # print(verificar)

# # print(nomes['Marcos'])


# # nomes = {'Nome': 'Marcos',
          
# #          'Idade' : 26, 

# #          'Altura': 1.88 
# #          }

# # print(nomes.pop('Idade'))
# # del nomes ['Nome']
# # print(nomes)

# # nomes.clear()

# # print(nomes)



# # print(nomes.keys())
# # print(nomes.values())
# # print(nomes.items())

# # for c, v in nomes.items():
# #     print(c,v)

# # for v1 in nomes.values():
# #     print(v1)

# # for c2 in nomes.keys():
# #     print(c2)


# # eu objetivo é descobrir qual país possui a maior população usando um loop for. Passo a passo sugerido: Crie duas variáveis de controle: Uma para guardar o nome do país com maior população (ex: pais_maior_pop), iniciando com uma string vazia. Outra para guardar o valor da maior população encontrada até agora (ex: maior_pop), iniciando com 0. Percorra o dicionário com um for, acessando o país e sua população. A cada iteração, compare a população atual com o valor de maior_pop: Se a população atual for maior, atualize as duas variáveis (maior_pop e pais_maior_pop). Ao final do laço, exiba na tela o resultado no formato: O país com a maior população é: X com Y habitantes.


# # populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000}



# # # print(list(populacoes.items())[2])

# # paisMaior = '' 

# # maiorPolucao = 0



# # for p, m in populacoes.items():
# #     if m > maiorPolucao:
# #         paisMaior = p 
# #         maiorPolucao = m 

# # print(f'o pais com a maior populção é {paisMaior} e sua popução é de {maiorPolucao}')


# nomes = {'Marcos', 'Gabriel', 'Ricardo', 'Gadriel'}

# nomes.add('Walter')

# print(nomes)


# nomes.remove('Ricardo')

# print(nomes)

# nomes.pop()

# print(nomes)


# nomes.discard('Marcos2')

# print(nomes)

# nomes.update(['Marcos2','Ricardo2'])

# print(nomes)


# elemento = nomes.pop()

# print(elemento)


# nomes2 = {'Andreia','Thigas','Peter','Lu','Marcos','Gabriel'}

# print(nomes | nomes2)


# print(nomes & nomes2)

# print(nomes2 - nomes)

# print(nomes ^ nomes2)

# valor = set()

# print(type(valor))





# populacoes = {"Brasil": 215_000_000, "China": 1_400_000_000, "EUA": 333_000_000, "Índia": 1_220_000_000, "Brasil": 215_000_000,}


# transformar = set(populacoes)

# print(populacoes)



