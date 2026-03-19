aparelho = input("Nome do aparelho eletrônico: ")
watts = int(input("Potência do aparelho em watts: "))
horasDia = int(input("Horas de consumo diário: "))

consumoMensal = (watts * horasDia * 30) / 1000
print(f"")
print(f"Consumo mensal estimado de {consumoMensal} ")



