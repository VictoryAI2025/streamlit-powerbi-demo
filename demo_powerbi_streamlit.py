
import streamlit as st
import pandas as pd
import io

st.set_page_config(page_title="Mini Power BI", layout="wide")

st.title("🧠 Analiza tus datos de Forma Interactiva")

# Cargar archivo
uploaded_file = st.file_uploader("📂 Sube tu archivo CSV", type=["csv"])

if uploaded_file:
    # Leer archivo
    df = pd.read_csv(uploaded_file)
    st.subheader("📋 Vista previa editable de los datos")
    edited_df = st.data_editor(df, num_rows="dynamic", use_container_width=True)

    st.markdown("---")

    st.subheader("🧮 Crear nueva columna")
    new_col_name = st.text_input("Nombre de la nueva columna")
    new_col_formula = st.text_input("Fórmula (usa nombres de columnas, ej: Edad * 2 + Ingresos_Mensuales / 1000)")

    if new_col_name and new_col_formula:
        try:
            edited_df[new_col_name] = eval(new_col_formula, {}, edited_df.to_dict(orient="series"))
            st.success(f"✅ Columna '{new_col_name}' creada exitosamente")
        except Exception as e:
            st.error(f"❌ Error al evaluar fórmula: {e}")

    st.markdown("---")
    st.subheader("📈 Datos listos para análisis")
    st.dataframe(edited_df, use_container_width=True)
    st.download_button("⬇️ Descargar CSV editado", edited_df.to_csv(index=False), "datos_editados.csv", "text/csv")

else:
    st.info("Por favor, sube un archivo CSV para comenzar.")
