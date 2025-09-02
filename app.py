import pandas as pd
import streamlit as st
import plotly.express as px 


try:
    df = pd.read_csv("data.csv")
    #print(df.isnull().sum())

    df_sin_nulos = df.dropna()
    #print(df_sin_nulos.isnull().sum())

except FileNotFoundError:
    print("Error al cargar el archivo, intenta dde nuevo")
except Exception as e:
    print(f"Ocurriò un error {e}")

st.set_page_config(
    page_title="Dashboard CO2",
    layout="wide",
    page_icon="📊"
)
 

#titulo 
st.title("Analisis de CO2 por país")
st.markdown("Explora las emisiones de CO2 por pais a lo largo del tiempo")

#barra lateral para los filtros
with st.sidebar:
    st.header("Filtros")
    
    lista_años = sorted(df_sin_nulos['year'].unique())
    seleccionar_año = st.slider(
        'Selecciona un año',
        min_value=min(lista_años),
        max_value=max(lista_años),
        value=max(lista_años)
    )



#formando lista de paises
    
    lista_paises = sorted(df_sin_nulos['country'].unique())

    paises = st.multiselect(
    'Selecciona uno o más países para analizar',
    lista_paises,
    default=[]
)



#mapeo de columnas
    columnas_map = {
    'Emisiones de CO2 (toneadas)': 'co2',
    'Emisiones de CO2 per cápita': 'co2_per_capita' 
}

#seleccion de metricas
    metrica_seleccion = st.radio("Selecciona la métrica:", list(columnas_map.keys()))


#primer figura
if paises:
    
#filtrado de años
    df_filtrado = df_sin_nulos[df_sin_nulos['year'] == seleccionar_año]

#filtrado paises
    df_filtrado = df_filtrado[df_filtrado['country'].isin(paises)]



    nombre_columna = columnas_map[metrica_seleccion]
    df_filtrado_ordenado = df_filtrado.sort_values(by=nombre_columna, ascending=False)

    fig = px.bar(
    df_filtrado_ordenado,
    x = 'country',
    y = nombre_columna,
    title=f'Emisiones de {metrica_seleccion} en {seleccionar_año}'
)



    st.plotly_chart(fig, use_container_width=True)

#segunda figura
if paises:
    df_historico_paises = df_sin_nulos[df_sin_nulos['country'].isin(paises)]
    nombre_columna = columnas_map[metrica_seleccion]

    fig_lineas = px.line(
    df_historico_paises,
    x='year',
    y=nombre_columna,
    color = 'country',
    title=f'Evolución de {metrica_seleccion} a lo largo del tiempo'
)   

    st.plotly_chart(fig_lineas, use_container_width=True)

else:
      st.info("Selecciona uno o más países para ver su evolución histórica.")








