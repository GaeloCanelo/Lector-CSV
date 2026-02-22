import csv
import statistics

def analizar_csv(path):
    """Lee un archivo CSV y calcula estadísticas básicas de la columna 'Valor'."""
    datos = []
    
    try:
        # Se define explícitamente el encoding para evitar errores en Windows/Linux
        with open(path, encoding='utf-8') as f:
            reader = csv.DictReader(f)
            for row in reader:
                try:
                    datos.append(float(row['Valor']))
                except (ValueError, KeyError):
                    # Ignora silenciosamente filas sin números o si la columna falta
                    continue
                    
        if not datos:
            print("No hay datos numéricos válidos para procesar.")
            return

        n = len(datos)
        print(f"Registros: {n}")
        print(f"Promedio: {statistics.mean(datos):.2f}")
        print(f"Máx: {max(datos)}")
        print(f"Mín: {min(datos)}")
        
    except FileNotFoundError:
        print(f"Error: No encuentro el archivo '{path}'")
    except csv.Error as e:
        print(f"Error procesando el formato CSV: {e}")

if __name__ == "__main__":
    analizar_csv('datos.csv')