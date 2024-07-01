def calcular_cedulas(valor):
    cedulas = [100, 50, 20, 10, 5, 2]
    resultado = {cedula: 0 for cedula in cedulas}

    if valor == 1 or valor == 3:
      return "Valor de saque não pode ser atendido com as cédulas disponíveis."

    for cedula in cedulas:
        if not(valor % cedula == 1 or valor % cedula == 3):
            if valor >= cedula:
                quantidade = valor // cedula
                resultado[cedula] = quantidade
                valor -= quantidade * cedula
        elif valor // cedula > 1: 
            if valor >= cedula:
                quantidade = (valor // cedula) - 1
                resultado[cedula] = quantidade
                valor -= quantidade * cedula

    
    if valor > 0:
      return "Valor de saque não pode ser atendido com as cédulas disponíveis."
    
    return resultado