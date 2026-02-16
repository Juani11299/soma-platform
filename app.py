import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# Configuración básica
st.set_page_config(page_title="SOMA - Ivolution", layout="wide")

# --- LOGIN ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔑 SOMA - Acceso")
    pwd = st.text_input("Contraseña Maestro", type="password")
    if st.button("Ingresar"):
        if pwd == "Soma2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Contraseña incorrecta")
    st.stop()

# --- APP PRINCIPAL (Lo que funcionaba) ---
st.title("🧬 PLATAFORMA SOMA")
st.write("Bienvenido al panel de control de datos.")

# Sección de Carga de Datos
st.header("📂 Carga de Archivos")
uploaded_file = st.file_uploader("Sube tu archivo CSV", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write("Vista previa de datos:", df.head())
    
    # Si el archivo tiene columnas para graficar
    if 'fecha' in df.columns and 'Ratio' in df.columns:
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=df['fecha'], y=df['Ratio'], mode='lines+markers', name='Ratio A:C'))
        st.plotly_chart(fig, use_container_width=True)
    else:
        st.info("Sube un archivo con columnas 'fecha' y 'Ratio' para ver gráficos.")
        