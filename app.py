import streamlit as st
import pandas as pd
import plotly.graph_objects as go

# 1. Configuración de página (Esto ayuda con el tema claro)
st.set_page_config(page_title="SOMA - Ivolution", layout="wide")

# --- LOGIN (Simplificado para el ejemplo) ---
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

# --- NAVEGACIÓN LATERAL ---
st.sidebar.title("🧬 IVOLUTION SOMA")
menu = st.sidebar.selectbox("Ir a:", [
    "🏠 Inicio", 
    "📊 Análisis de Datos", 
    "📂 Gestión de Datos", 
    "📝 Blog", 
    "🎓 Capacitaciones", 
    "🏋️ Planes"
])

# --- LÓGICA DE MÓDULOS ---

if menu == "🏠 Inicio":
    st.title("Bienvenido al Laboratorio SOMA")
    st.write("Selecciona una sección en el menú lateral para comenzar.")

elif menu == "📊 Análisis de Datos":
    st.header("📊 Análisis de Rendimiento y Fatiga")
    # Aquí va tu código de ACWR y Plotly que vimos en la captura
    st.info("Módulo configurado para análisis de CMJ y Carga Aguda/Crónica.")

elif menu == "📂 Gestión de Datos":
    st.header("📂 Carga de Archivos")
    archivo = st.file_uploader("Sube el CSV de la sesión", type=['csv'])
    if archivo:
        df = pd.read_csv(archivo)
        st.write("Datos detectados:", df.head())

elif menu == "📝 Blog":
    st.header("📝 Blog de Ciencia y Deporte")
    st.markdown("### Últimas entradas")
    st.write("- Cómo interpretar las fases del CMJ [cite: 2026-02-08]")
    st.write("- El uso del sRPE en deportes de equipo [cite: 2026-02-12]")

elif menu == "🎓 Capacitaciones":
    st.header("🎓 Academia Ivolution")
    st.info("Próximamente: Cursos sobre Biomecánica aplicada.")

elif menu == "🏋️ Planes":
    st.header("🏋️ Planes de Entrenamiento")
    st.write("Aquí podrás visualizar las rutinas programadas.")