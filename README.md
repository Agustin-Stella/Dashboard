# 📊 Dashboard con Streamlit

Este proyecto es una aplicación web interactiva construida con Streamlit que permite visualizar y explorar datos de CO2 de forma sencilla.  

---

## 🚀 Requisitos previos

Asegúrate de tener instalado:

- [Python 3.12.10](https://www.python.org/downloads/)
- [pip](https://pip.pypa.io/en/stable/installation/)

---

## ⚙️ Instalación y ejecución

1- Clonar el repositorio
   
   git clone https://github.com/Agustin-Stella/Dashboard.git

   cd Dashboard

2- Crear y activar entorno 

   macOS/Linux:

   python -m venv entorno

   source entorno/bin/activate


   Windows:

   python -m venv entorno

   entorno\Scripts\activate

3- Instalar dependencias 

   pip install -r requirements.txt

4- Ejecutar la aplicación

streamlit run app.py


✨ Características

Visualización de datos interactiva (CO2)

Interfaz simple e intuitiva 🖥️

Integración rápida con datasets propios 📊


📝 Funcionalidades

Este Dashboard está diseñado para que sea intuitivo.

Filtros interactivos:
                     Selección de año: Utiliza una barra para ver las emisiones en un año especifico.

                     Selección de Pais: Elige uno o varios paises para analizar y comparar.

                     Selección de métrica: Alterna entre "Emisiones de CO2 (toneladas)" (emisiones totales por país) y "Emisiones de CO2 per cápita" (emisiones por persona), lo que ofrece diferentes perspectivas del impacto.

Inteligencia Artificial Predictiva: 
El dashboard incluye una sección de predicción que utiliza un modelo de machine learning (Prophet) para pronosticar futuras emisiones.

                  Predicción por país: Selecciona un país y el modelo proyectará su evolución de emisiones a futuro, incluyendo un rango de confianza.

Visualización de Datos: Se generan tres tipos de gráficos para ayudarte a entender la información (Y se le puede agregar el grafico de Predicción con IA):

Gráfico de Barras: Compara las emisiones entre los países seleccionados en un año específico.

Gráfico de Líneas: Muestra la evolución histórica de las emisiones a lo largo del tiempo.

Mapa de Coropletas: Visualiza las emisiones de CO2 directamente sobre un mapa mundial, lo que permite una comprensión geográfica de los datos.


🚀 Cómo Usar el Dashboard
Explorar datos históricos: Usa los filtros en la barra lateral para seleccionar el año, los países y la métrica de interés. Los gráficos principales se actualizarán automáticamente.

Generar predicciones: 
Elige un país y haz clic en el botón "Generar Predicción". El dashboard te mostrará un gráfico de líneas con la tendencia futura esperada y su rango de confianza.

📈 Resultado Esperado
El objetivo del proyecto es proporcionar una forma clara y visual de entender los datos de emisiones de CO2. Al interactuar con los filtros y la IA, puedes obtener las siguientes ideas:

Análisis Comparativo: Compara las emisiones de diferentes países y observa las variaciones en los niveles de contaminación.

Análisis Temporal: Identifica si las emisiones de un país han aumentado o disminuido con el tiempo.

Visualización Geográfica: Observa rápidamente qué regiones del mundo tienen mayores o menores emisiones de CO2.

Proyección a Futuro: Obtén una idea de las posibles tendencias de las emisiones a futuro, lo cual es útil para la toma de decisiones.


