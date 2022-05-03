usuario=str(input("Ingrese usuario:"))
cantidad=int(input("Ingrese el monto a ingresar a su CDT:"))
porcentaje_interes=0.03
porcentaje_perder=0.02
tiempo=int(input("Ingrese la cantidad en meses para su CDT:"))
valor_intereses=(cantidad*porcentaje_interes*tiempo)/12
valor_perder=cantidad*porcentaje_perder


if(tiempo>2):
    valor_total=valor_intereses + cantidad
    print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor_total}")
else:
        valor_total=cantidad-valor_perder
        print(f"Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {cantidad} para un tiempo de {tiempo} meses es: {valor_total}")
