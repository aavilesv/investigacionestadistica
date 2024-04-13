import pandas as pd

# Cargar los datos desde la ruta especificada
data = pd.read_excel('G:\\Mi unidad\\Anelly\\data\\data_procesado.xlsx')

# Muestreo con reemplazo para aumentar el conjunto de datos
data_augmented = data.sample(n=100, replace=True, random_state=42)
