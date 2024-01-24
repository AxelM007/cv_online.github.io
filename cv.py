from pathlib import Path

import streamlit as st
from PIL import Image


# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()

# --- PATH SETTINGS ---
css_file    = current_dir / "styles" / "main.css"
resume_file = current_dir / "utils" / "Curriculum_2.pdf"
profile_pic = current_dir / "utils" / "profile-pic.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Currículum | Pedro Axel Méndez López"
PAGE_ICON = ":wave:"
NAME = "Pedro Axel Méndez López"
DESCRIPTION = """
Soy un estudiante recien egresado en la licenciatura de actuaría con solidos conocimientos en el área de estadística y probabilidad, adicional a eso, tengo conocimientos 
en código y machine learning, poseo un dominio básico en software tal como lo es python, R studio, Excel (visual basic), y MySQL para realizar consultas y la
creación de bases de datos
"""
EMAIL = "axelmendezlopez@ciencias.unam.mx"
SOCIAL_MEDIA = {
    "LinkedIn": "www.linkedin.com/in/pedro-axel-méndez-lópez-2b695a27a",
    "GitHub": "https://github.com/AxelM007",
}
#### notas y ejercicios 
PROJECTS = {
    "🏆 Predicción de partidos de fútbol (Modelo Poisson)": "https://github.com/NataelM/soccer_model",
    "🏆 Notas de Web Scrapping con python": "https://github.com/NataelM/web_scrapping_python",
    "🏆 Notas de Análisis Multivariado": "https://github.com/NataelM/multi_notebooks",
    "🏆 Notas de Deep Learning": "https://github.com/NataelM/deep_learning_clase",
    "🏆 Notas de Series de Tiempo": "https://github.com/NataelM/Series_de_tiempo",
    "🏆 Mini proyecto de regresión lineal multiple bayesiana (con R)": "https://github.com/NataelM/Bayesian_linear_multiple",
}


st.set_page_config(page_title = PAGE_TITLE, 
                   page_icon = PAGE_ICON
                   )


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    st.write(DESCRIPTION)
    st.download_button(
        label=" 📄 Descargar CV",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)


# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[{platform}]({link})")


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experiencia & Cualificaciones")
st.write(
    """
- ✔️ 1 semestre como profesor de adjunto en la UNAM en la materia de probabilidad (con código en R).
- ✔️ Manejo de matemáticas y estadística de nivel avanzado para la modelación de problemas.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("Hard Skills")
st.write(
    """
- 👩‍💻 Software: Python, SPARK, SQL, R, Git/Git-Hub, Databricks, Dataiku,Office
- 📚 Conocimiento: - Machine lerning:
                        - Supervisado
                        - No supervisado
                        - Semi-supervisado
                   - Redes Neuronales
                       - NLP
                       - LLM
                       - Embeddings
                       - Langchain
                   - Series de tiempo
                       - Técncias de suavizamientos
                       - Modelos ARIMA
                       - Modelos ARCH
"""
)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("Experiencia")
st.write("---")

# --- JOB 1
st.write("🚧", "**Científico de Datos Sr. | Grupo Salinas**")
st.write("09/2022 - Present")
st.write(
    """
- ► Gestión, orientación y propuestas en el desarrollo de modelos LLM para casuísticas en auditoría.
- ► Desarrollo de modelo de CHURN en telecomunicaciones.
- ► Evaluación de proveedores de software analítico para la productivización de desarrollos.
- ► Evaluación de candidatos en Ciencia de Datos.
- ► Desarrollo e implementación de Algoritmos de Boosting y rasgadura para la detección temprana de
    clientes potencialmente defraudadores y entregable en streamlit al usuario final.
- ► Desarrollo e implementación de algoritmos semi-supervisados para la detección de cambios
    de domicilio.
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Científico de Datos | Axity-WalMart**")
st.write("09/2021 - 09/2022")
st.write(
    """
- ► Desarrollo, manejo y transformación de datos de retail a nivel nacional para el alertamiento
    oportuno en la caída de ventas (con pySpark) y uso de algoritmos supervisados de clasificación
    para pronosticar un incremento o decremento en las ventas.
    Además de hacer prescripción sobre el comportamiento de ventas mediante correlaciones parciales.
"""
)

# --- JOB 3
st.write('\n')
st.write("🚧", "**Consultor Analítico | C3 Analitycal Solutions**")
st.write("07/2020 - 09/2021")
st.write(
    """
- ► Estructura de datos, lay-out de tablas y diseño de diagramas entidad relación para el cálculo
    de reservas según IFRS-9.
- ► Propuesta de soluciones analíticas en el sector asegurador automovilístico para eficientear
    y aumentar las ventas en pólizas.
"""
)


# --- Projects & Accomplishments ---
st.write('\n')
st.subheader("Notas y ejercicios.")
st.write("---")
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")
