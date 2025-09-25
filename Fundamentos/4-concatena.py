name = input("Digite o nome do filme:\n")
launchYear = int(input("Digite o ano de lançamento do filme:\n"))
movieGrade = float(input("Digite a avaliação do filme:\n"))

print("Dados do Filme")
print("====================================")

#alternativa 1
print("Nome do filme:",name)
print("Ano de lançamento:", launchYear)
print("Avaliação do filme:", movieGrade)

#alternativa 2
print("Nome do filme:",name, "\nAno de lançamento:", launchYear, "\nAvaliação do filme:", movieGrade)

#alternativa 3
print(f"Nome do filme:{name}\n"
      f"Ano de lançamento:{launchYear}\n"
      f"Avaliação do filme:{movieGrade}"
      )
