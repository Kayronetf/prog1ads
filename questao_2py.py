tempo_banho = int(input("quanto tempo demora seu banho? "))
litros_gastos = 9 * tempo_banho
total_de_banhos = 1000 / litros_gastos
print("o total de banhos para consumir 1000 litros de agua é: {:.2f}".format(total_de_banhos))
