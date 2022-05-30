def cliente(informacion:dict)->dict:
    cli_nombre = informacion["nombre"]
    cli_edad = informacion["edad"]
    cli_ingreso = informacion["primer_ingreso"]



    if cli_edad >18:
        atraccion = 'X-Treme'
        apto=True
        if cli_ingreso ==True:
           total_boleta = 20000 -(20000*0.05)
        else:
           total_boleta= 20000

    elif cli_edad >=15 and cli_edad <= 18:
        atraccion = 'Carros chocones'
        apto=True
        if cli_ingreso ==True:
           total_boleta= 5000 -(5000 * 0.07)
        else:
           total_boleta = 5000

    elif cli_edad >=7 and cli_edad <15:
        atraccion = 'Sillas voladoras'
        apto=True
        if cli_ingreso ==True:
           total_boleta= 10000 -(10000 * 0.05)
        else:
           total_boleta= 10000
    else:
        atraccion = 'N/A'
        apto=False
        total_boleta = 'N/A'



    diccionario = {
    'nombre': cli_nombre,
    'edad': cli_edad,
    'atraccion':atraccion,
    'apto': apto,
    'primer_ingreso': cli_ingreso,
    'total_boleta': total_boleta
    }

    return diccionario




informacion={
'nombre': 'Johana Fernandez', 
'edad': 20, 
'primer_ingreso': True, 
}

print(cliente(informacion))



informacion={
'nombre': 'Johana Fernandez', 
'edad': 20, 
'primer_ingreso': False, 
}

print(cliente(informacion))



informacion={
'nombre': 'Gloria Suarez', 
'edad': 3, 
'primer_ingreso': True, 
}

print(cliente(informacion))

informacion={
'nombre': 'Tatiana Suarez', 
'edad': 17, 
'primer_ingreso': True, 
}

print(cliente(informacion))


informacion={
'nombre': 'Tatiana Suarez', 
'edad': 17, 
'primer_ingreso': False, 
}

print(cliente(informacion))


informacion={
'nombre': 'Tatiana Ruiz', 
'edad': 8, 
'primer_ingreso': True, 
}

print(cliente(informacion))


informacion={
'nombre': 'Tatiana Ruiz', 
'edad': 8, 
'primer_ingreso': False, 
}

print(cliente(informacion))


