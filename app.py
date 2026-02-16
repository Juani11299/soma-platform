import streamlit as st
import pandas as pd

st.set_page_config(page_title="SOMA")

# --- LOGIN SIMPLE ---
if "autenticado" not in st.session_state:
    st.session_state.autenticado = False

if not st.session_state.autenticado:
    st.title("🔑 SOMA - Acceso")
    pwd = st.text_input("Contraseña:", type="password")
    if st.button("Entrar"):
        if pwd == "Soma2026":
            st.session_state.autenticado = True
            st.rerun()
        else:
            st.error("Incorrecto")
    st.stop()

# --- SI ENTRA ---
st.title("✅ ¡SOMA ESTÁ ONLINE!")
st.success("La conexión funciona. Ahora podemos mejorar el diseño.")
st.write("Bienvenido al panel de control.")
