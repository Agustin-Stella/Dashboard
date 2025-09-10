import pandas as pd
import streamlit as st
import plotly.express as px 
from modelo import predict_emissions  


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
st.title("📊Analisis de CO2 por país📊")
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

st.header("Predicción de emisiones")

pais_prediccion=st.selectbox(
    "Pais para predecir",
    lista_paises
)

if st.button("Generar predicción"):
    with st.spinner("Generando predicción..."):
         #obtiene el nombre de la metrica
         nombre_columna_prediccion = columnas_map[metrica_seleccion] 
         #llama la funcion
         forecast=predict_emissions(df_sin_nulos, pais_prediccion, nombre_columna_prediccion)

         #crea el grafico
         fig_prediccion = px.line(
            forecast, #prediccion
            x='ds', #año
            y='yhat', #prediccion
            title=f'Predicción de Emisiones de {metrica_seleccion} para {pais_prediccion}'
        )
         #agrega linea al grafico para mostrar linea inferior y superior como un intervalo de confianza y muestra el grafico
         fig_prediccion.add_scatter(x=forecast['ds'], y=forecast['yhat_lower'],name='Límite Inferior')
         fig_prediccion.add_scatter(x=forecast['ds'], y=forecast['yhat_upper'],name='Límite Superior')
         st.plotly_chart(fig_prediccion, use_container_width=True)

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
        title=f'📊Emisiones de {metrica_seleccion} en {seleccionar_año}📊'
    )
    st.plotly_chart(fig, use_container_width=True)

#segunda figura
    fig_lineas = px.line(
        df_filtrado_paises,
        x='year',
        y=nombre_columna,
        color='country',
        title=f'📈Evolución de {metrica_seleccion} a lo largo del tiempo📈'
    ) 
    st.plotly_chart(fig_lineas, use_container_width=True)

    st.markdown("---")
    st.subheader(f'🌍Emisiones de {metrica_seleccion} por pais en el año {seleccionar_año}🌍')

#filtros para tercera figura
    df_filtrado_año_mapa = df_sin_nulos[df_sin_nulos['year'] == seleccionar_año] 
    df_para_mapa = df_filtrado_año_mapa[df_filtrado_año_mapa['country'].isin(paises)]
#tercera figura
    if 'iso_code' in df_para_mapa:
        fig_mapa = px.choropleth(
        df_para_mapa,
        locations='iso_code',
        color=nombre_columna,
        hover_name='country',
        color_continuous_scale=px.colors.sequential.Plasma,
        title=f'Mapa de Emisiones de {metrica_seleccion} en {seleccionar_año}'
    )

        st.plotly_chart(fig_mapa, use_container_width=True)
    else:
        st.info("Error al cargar el archivo de datos.")
else:
      st.info("Selecciona uno o más países para ver su evolución histórica (Barra lateral)")







