
def CDT(usuario:str,capital:int,tiempo:int):
    if(tiempo>2):
        porcentaje_interes=0.03
        valor_intereses=(capital*porcentaje_interes*tiempo)/12
        valor_total=valor_intereses + capital
    
    else:
        porcentaje_perder=0.02
        valor_perder=capital*porcentaje_perder
        valor_total=capital-valor_perder
        
    
    return f'Para el usuario {usuario} La cantidad de dinero a recibir, según el monto inicial {capital} para un tiempo de {tiempo} meses es: {valor_total}'
