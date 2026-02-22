# 📊 Análisis Estadístico de Datos CSV

Script en Python que procesa un archivo CSV con datos numéricos y calcula estadísticas descriptivas básicas: conteo de registros, promedio, valor máximo y valor mínimo.

---

## 🚀 Características Principales

- **Sin dependencias externas:** Usa únicamente módulos de la biblioteca estándar de Python (`csv` y `statistics`)
- **Tolerante a errores:** Ignora filas con datos inválidos o faltantes sin interrumpir la ejecución
- **Compatible entre plataformas:** Lectura con `encoding='utf-8'` para evitar problemas en Windows, Linux y macOS
- **Acceso por nombre de columna:** Lee el CSV como diccionario, permitiendo extender el análisis a otras columnas fácilmente

---

## ⚙️ Requisitos Previos

- **Python:** Versión 3.6 o superior
- **Dependencias externas:** Ninguna

---

## 📂 Estructura del Repositorio

```
analisis-csv/
├── analisis_csv.py   # Script principal con la función de análisis
└── datos.csv         # Archivo de ejemplo con los datos a procesar
```

---

## 📄 Estructura del archivo CSV esperada

El script asume que el CSV tiene encabezado y una columna llamada **`Valor`** con datos numéricos:

```csv
Valor
10.5
23.8
15.2
...
```

---

## 🛠️ Cómo ejecutar

**1. Clona o descarga** este repositorio:
```bash
git clone https://github.com/tuusuario/analisis-csv.git
cd analisis-csv
```

**2. Asegúrate** de que `datos.csv` esté en la misma carpeta que el script (o modifica la ruta en la última línea del código).

**3. Ejecuta el script:**
```bash
python analisis_csv.py
```

---

## 📋 Ejemplo de salida

```
Registros: 15
Promedio: 42.67
Máx: 98.3
Mín: 12.1
```

---

## 🔍 Funcionamiento interno

1. **Apertura del archivo** con `encoding='utf-8'` para compatibilidad entre sistemas operativos
2. **Lectura** del CSV como diccionario para acceder a columnas por nombre
3. **Conversión** de cada valor de la columna `'Valor'` a `float`
4. **Cálculo** de estadísticas con `statistics.mean()`, `max()` y `min()`
5. **Manejo de errores** en dos niveles:
   - A nivel de fila: ignora entradas no numéricas o con columna faltante
   - A nivel de archivo: captura errores de archivo no encontrado o formato CSV inválido

---

## ⚠️ Posibles errores y soluciones

| Error | Causa probable | Solución |
|-------|----------------|----------|
| `FileNotFoundError` | El archivo `datos.csv` no está en la carpeta | Verifica la ubicación o copia el archivo |
| `No hay datos numéricos válidos` | El archivo está vacío o sin números | Revisa que haya datos en la columna `Valor` |
| Resultados incorrectos | La columna no se llama exactamente `Valor` | Ajusta el nombre en el CSV o en el código |

---

## 🎨 Personalización

Para analizar una columna distinta, modifica esta línea en el código:

```python
datos.append(float(row['Valor']))  # Cambia 'Valor' por el nombre de tu columna
```

---

## 📝 Notas Importantes

1. El script procesa **únicamente** la columna `Valor`; el resto de columnas del CSV son ignoradas
2. Las filas con valores no convertibles a número se omiten **silenciosamente** (sin advertencia en consola)
3. Si el archivo CSV está completamente vacío o sin datos válidos, el script lo notifica y termina sin errores

---

## 👥 Autor
**Ramírez Lozano Gael Martín**

**Fecha:** Febrero 2026