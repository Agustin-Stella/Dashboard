import pandas as pd
import streamlit as st
import plotly.express as px 


@st.cache_data

def load_data():
 df = pd.read_csv("data.csv")
 df_sin_nulos = df.dropna()
 return df_sin_nulos
df_sin_nulos = load_data()

st.set_page_config(
    page_title="Dashboard CO2",
    layout="wide",
    page_icon="📊"
)
 
#mapeo de columnas
columnas_map = {
    'Emisiones de CO2 (toneadas)': 'co2',
    'Emisiones de CO2 per cápita': 'co2_per_capita' 
}

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




#seleccion de metricas
    metrica_seleccion = st.radio("Selecciona la métrica:", list(columnas_map.keys()))


#primer figura
if paises:
    
#filtro dataframe
    df_filtrado_paises = df_sin_nulos[df_sin_nulos['country'].isin(paises)]
    
    nombre_columna = columnas_map[metrica_seleccion]

    
    df_filtrado_año = df_filtrado_paises[df_filtrado_paises['year'] == seleccionar_año]
    df_filtrado_ordenado = df_filtrado_año.sort_values(by=nombre_columna, ascending=False)


#primer figura    
    fig = px.bar(
        df_filtrado_ordenado,
        x='country',
        y=nombre_columna,
        title=f'Emisiones de {metrica_seleccion} en {seleccionar_año}'
    )
    st.plotly_chart(fig, use_container_width=True)

#segunda figura
    fig_lineas = px.line(
        df_filtrado_paises,
        x='year',
        y=nombre_columna,
        color='country',
        title=f'Evolución de {metrica_seleccion} a lo largo del tiempo'
    ) 
    st.plotly_chart(fig_lineas, use_container_width=True)

else:
      st.info("Selecciona uno o más países para ver su evolución histórica (Barra lateral)")








