import pandas as pd

# Load the excel file to check its content
data = pd.read_excel('G:\\Mi unidad\\Anelly\\data\\data.xlsx')
#data.head()

# Definir el mapeo de texto a número para la columna 'Edad'
mapeo_edad = {
    'Menor de 18 años': 1,
    '18 - 24 años': 2,
    '25 - 34 años': 3,
    '35 - 44 años': 4,
    '45 - 54 años': 5,
    '55 - 64 años': 6,
    '65 años o más': 7
}
mapeo_genero = {
    'Masculino': 1,
    'Femenino': 2,
    'Prefiero no decir': 3
    }
mapeo_ocapacion = {
    'Estudiante': 1,
    'Empleado(a) tiempo completo': 2,
    'Empleado(a) tiempo parcial': 3,
    'Empresario(a)/Autónomo(a)': 4,
    'Desempleado(a)': 5,
    'Jubilado(a)': 6,
    'Docente': 7,
    }

mapeo_ind22 = {
    'Descuentos por compra.': 1,
    'Programas de fidelización.': 2,
    'Un producto gratis por la compra de otro producto del menú.': 3,
    'Descuentos por referir a nuevos clientes.': 4,
    'Beneficios por fechas especiales (cumpleaños, aniversarios, etc.)': 5,

    }

mapeo_ind23 = {
    'Redes sociales.': 1,
    'Sitio web de Coffee Time.': 2,
    'Email.': 3,
    'Aplicación móvil de Coffee Time.': 4,
    'Publicidad en medios tradicionales (periódicos, revistas).': 5,
    'Publicidad exterior (vallas publicitarias, carteles).': 6,
    'Eventos en la cafetería.': 7,
    'Todas las opciones': 8,
    }
mapeo_ind24 = {
    'Facebook': 1,
    'Instagram': 2,
    'TikTok': 3,
    'X (anteriormente conocido como Twitter)': 4,
    'Todas las redes sociales' : 5,
    'WhatsApp' : 5,
   
    }
# Elimina los espacios iniciales y finales de los nombres de columna
data.columns = data.columns.str.strip()
data['ind24'] = data['ind24'].str.strip()
# Print the cleaned column names to confirm the change
print(data.columns)
# Reemplazar los valores en la columna 'Edad'

data['Edad'] = data['Edad'].replace(mapeo_edad)
data['Sexo'] = data['Sexo'].replace(mapeo_genero)
data['Ocupación'] = data['Ocupación'].replace(mapeo_ocapacion)
data['ind22'] = data['ind22'].replace(mapeo_ind22)
data['ind23'] = data['ind23'].replace(mapeo_ind23)
data['ind24'] = data['ind24'].replace(mapeo_ind24)
# variables categoricas moda
# Calculamos la moda de la columna 'Ocupación'
moda_ocupacion = data['Ocupación'].mode()[0]
# Reemplazamos los NaN en la columna 'Ocupación' con la moda
data['Ocupación'].fillna(moda_ocupacion, inplace=True )
moda_sexo = data['Sexo'].mode()[0] 
data['Sexo'].fillna(moda_sexo, inplace=True)
descripcion = data.describe()


# Lista de las columnas numéricas específicas variables
columnas_numericas = ['ind4', 'ind5', 'ind6', 'ind7', 'ind8', 'ind9', 'ind10', 
                      'ind11', 'ind12', 'ind13', 'ind14', 'ind15', 'ind16', 
                      'ind17', 'ind18', 'ind19', 'ind20', 'ind21', 'ind22', 
                      'ind23', 'ind24']
# Imputar la mediana para cada columna numérica y reemplazar NaN
for columna in columnas_numericas:
    #Calcula la mediana y redondea al entero más cercano
    mediana = round(data[columna].median()) 
    data[columna].fillna(mediana, inplace=True)

data.to_excel('G:\\Mi unidad\\Anelly\\data\\data_procesado.xlsx', index=False)