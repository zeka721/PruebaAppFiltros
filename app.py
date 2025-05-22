import pandas as pd
import streamlit as st

# Cargar datos desde Google Sheets
sheet_id = "1Z-e0SAGtPCBets0qKIGI29WKsE98NRnkfrcDkBPayoA"
gid = "0"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/export?format=csv&gid={gid}"

@st.cache_data
def cargar_datos():
    return pd.read_csv(url)

df = cargar_datos()

st.title("🔎 Filtro de datos desde Google Sheets")

# 🔍 Filtros interactivos
st.subheader("🔍 Filtrar datos")

# Filtrar por nombre
nombre = st.text_input("Filtrar por nombre:")

# Filtrar por ciudad
ciudades = [""] + sorted(df['CIUDAD'].dropna().unique().tolist())
ciudad = st.selectbox("Filtrar por ciudad:", ciudades)

# Filtrar por rango de edad
edad_min = int(df['EDAD'].min())
edad_max = int(df['EDAD'].max())
edad = st.slider("Filtrar por edad:", min_value=edad_min, max_value=edad_max, value=(edad_min, edad_max))

# Aplicar filtros
df_filtrado = df.copy()

if nombre:
    df_filtrado = df_filtrado[df_filtrado['NOMBRE'].str.contains(nombre, case=False, na=False)]

if ciudad:
    df_filtrado = df_filtrado[df_filtrado['CIUDAD'] == ciudad]

df_filtrado = df_filtrado[(df_filtrado['EDAD'] >= edad[0]) & (df_filtrado['EDAD'] <= edad[1])]

# ✅ Mostrar resultados filtrados
st.subheader("✅ Resultados")
st.dataframe(df_filtrado)
