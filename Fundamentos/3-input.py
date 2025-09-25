#Utilizando o input
#retorno do input será sempre str, por isso as conversões
"""
name = input("Digite o nome do filme:\n")
launchYear = input("Digite o ano de lançamento do filme:\n")
movieGrade = input("Digite a avaliação do filme:\n")
"""

name = input("Digite o nome do filme:\n")
launchYear = int(input("Digite o ano de lançamento do filme:\n"))
movieGrade = float(input("Digite a avaliação do filme:\n"))

print(type(name))
print(type(launchYear))
print(type(movieGrade))

