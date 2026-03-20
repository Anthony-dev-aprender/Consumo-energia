aparelho = input("Nome do aparelho eletrônico: ")
watts = int(input("Potência do aparelho em watts: "))
horasDia = int(input("Horas de consumo diário: "))

consumoMensal = (watts * horasDia * 30) / 1000
print(f"Aparelho: {aparelho}")
print(f"Consumo estimado: {consumoMensal:.2f} kWh/mês")

resposta = input("Você gostaria saber o preço do consumo? (s/n): ")

if resposta == "s":
    print("Calculando o preço...")
    precoDoAparelho = (consumoMensal * 0.75)
    print(f"O valor estimado para o consumo mensal do aparelho será de: R${precoDoAparelho}")
else:
    print("Ok, encerrando.")