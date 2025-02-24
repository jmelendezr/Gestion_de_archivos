import csv

def compras_pais(archivo, pais):
    conteo = 0
    with open(archivo, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        next(reader)
        for row in reader:
            if row[7] == pais:  # Índice de la columna 'pais'
                conteo += 1
    return conteo

# Solicitar al usuario el país
archivo = "C:/Users/Estudiante/Documents/Nueva carpeta/SalesJan2009.csv"
pais = input("Ingrese el nombre del país: ")

# Contar transacciones en el país especificado
conteo_transacciones = compras_pais(archivo, pais)

# Mostrar resultado
print(f"Número de transacciones en {pais}: {conteo_transacciones}")