valor_litro = float(input("digite o valor do litro do combustivel: "))
valor_abastecido = float(input("digite o valor que você deseja abastecer: "))
total_litros =  valor_abastecido / valor_litro
print("o valor total de litros é: {:.2f}".format(total_litros))
