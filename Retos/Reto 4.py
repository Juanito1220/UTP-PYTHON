def ordenes(rutinaContable):
    print("----------------- Inicio Registro diario --------------------------")

    for i in rutinaContable:

        tuplas= []

        for j in i:

            if isinstance(j, int):
                n_factura = j
            else:
                suma_tupla = j[1]*j[2]
                tuplas.append(suma_tupla)

            suma_total_tuplas = round(sum(tuplas),2)

            if suma_total_tuplas<600000:
              suma_total_tuplas+=25000

        print(f"La factura {n_factura} tiene un total en pesos de {suma_total_tuplas}")

    print('----------------- Fin Registro diario -----------------------------')


rutinaContable =[
 [1201, ("5464", 4, 25842.99), ("7854",18,23254.99), ("8521", 9, 48951.95)],
 [1202, ("8756", 3, 115362.58),("1112",18,2354.99)],
 [1203, ("2547", 1, 125698.20), ("2635", 2, 135645.20), ("1254", 1, 13645.20),("9965", 5, 1645.20)],
 [1204, ("9635", 7, 11.99), ("7733",11,18.99), ("88112", 5, 390.95)]
]

ordenes(rutinaContable)