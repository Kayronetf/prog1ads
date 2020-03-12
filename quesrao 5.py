divida = float(input("digite o valor da divida: "))
atraso = int(input("digite quantos dias em atraso está: "))
multa = float(input("digite quanto será cobrado a multa por dia: "))
total = divida + atraso * multa
print("o valor total a ser pago será: {}".format(total))
