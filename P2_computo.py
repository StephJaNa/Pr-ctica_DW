import math

def divide_vector_equitativo(vector, num_procesadores):
    n = (200)
    elementos_por_procesador = n // num_procesadores
    elementos_extra = n % num_procesadores
    
    limites = []
    inicio = 0
    
    for i in range(num_procesadores):
        fin = inicio + elementos_por_procesador
        if i < elementos_extra:
            fin += 1
        limites += [(inicio,fin)]
        inicio = fin
    
    return limites

vector = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,11,12,13,14,15,16,17,18,19,20]
num_procesadores = 7
limites = divide_vector_equitativo(vector, num_procesadores)

print("Límites por procesador:")
for i, (inicio, fin) in enumerate(limites):
    print(f"Procesador {i+1}: Desde {inicio} hasta {fin}")
