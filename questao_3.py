inicial = int(input("digite o km inicial do seu percurso: "))
final = int(input("digite o km final do seu percurso: "))
total_km = final - inicial
km_por_l = float(input("digite quantos km por litro o seu carro faz: "))
media = total_km / km_por_l
print("a media que seu carro fez no percurso foi: {:.2f}".format(media))
