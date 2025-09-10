from prophet import Prophet
import pandas as pd
import streamlit as st

def predict_emissions(df_completo, pais_seleccionado, metrica, periodos_prediccion=5):
  
    #pais para realizar la predicción (Australia por defecto)
    df_pais = df_completo[df_completo['country'] == pais_seleccionado].copy() 

    #argumento metrica para la predicción
    df_pais = df_pais.rename(columns={'year': 'ds', metrica: 'y'})
    df_pais['ds'] = pd.to_datetime(df_pais['ds'], format='%Y')

    #modelo de predicción
    modelo = Prophet(daily_seasonality=True)
    modelo.fit(df_pais)

    #crea un DataFrame que contiene las fechas para las cuales se realizarán las predicciones
    future = modelo.make_future_dataframe(periods=periodos_prediccion, freq='Y')
    forecast = modelo.predict(future)

    #devuelve forecast que tiene las predicciones
    return forecast



