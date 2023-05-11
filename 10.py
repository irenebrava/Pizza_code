def num_positivo(numero):
    while True:
        try:
            numero == float(numero)
            if float(numero) >=0:
                break
            else:
                raise ValueError("debes dar un numero entero y positivo:")
        except ValueError:
            numero = input("debes dar un numero positivo: ")
    return float(numero)
tasa = 0.055
lista_entrada = []
lista_cantidad =[]
lista_tasa =[]
lista_total=[]
precio = input("dame el precio al que le aplicaras el impuesto:  ")
while precio != "":
    cantidad = input("dame cantidad de productos:  ")
    catidad = num_positivo(cantidad)
    precio = num_positivo(precio)
    lista_entrada.append(float(precio))
    precio = input("dame el precio al que le aplicaras el impuesto:  ")

for precio in lista_entrada:
    precio_tasa = precio*tasa
    lista_tasa.append(round(precio_tasa,2))
    precio_total = (precio+precio_tasa)*num_positivo(cantidad)
    lista_total.append(round(precio_total,2))

for i in range(len(lista_entrada)):
    print("El precio original es {} el precio tasa es {} y el total es {}".format((lista_entrada[i]),(lista_tasa[i]),(lista_total[i])))
