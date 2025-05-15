import streamlit as st
from PIL import Image, ImageEnhance
import img2pdf
import io

st.set_page_config(page_title="Escáner Inteligente 📸")

st.title("Escáner Inteligente")
st.subheader("📸 Sube una foto del documento")

uploaded_file = st.file_uploader("Elige una imagen", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="Original", use_container_width=True)

    # Mejora de brillo y contraste
    enhancer = ImageEnhance.Contrast(image)
    enhanced_image = enhancer.enhance(2.0)

    st.image(enhanced_image, caption="Imagen mejorada", use_container_width=True)

    # Conversión a PDF
    pdf_bytes = io.BytesIO()
    enhanced_image.convert('RGB').save(pdf_bytes, format='PDF')
    st.download_button("📄 Descargar como PDF", pdf_bytes.getvalue(), "documento.pdf", "application/pdf")
