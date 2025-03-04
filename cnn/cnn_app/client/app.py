import streamlit as st
import requests

from config import API_URL

# Titre de l'application
st.title("📤 Upload d'image et envoi vers une API")

# Formulaire de dépôt de fichier
with st.form("upload_form"):
    uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
    submit_button = st.form_submit_button("Envoyer")

# Si le formulaire est soumis
if submit_button:
    if uploaded_file is not None:
        # Affiche l'image uploadée
        st.image(uploaded_file, caption="Image envoyée", use_column_width=True)
        
        # Prépare le fichier pour l'envoi à l'API
        files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

        # Envoie la requête POST à l'API
        try:
            response = requests.post(API_URL, files=files)
            response.raise_for_status()  # Lève une exception si code HTTP d'erreur

            # Affiche la réponse de l'API
            st.success("✅ Réponse de l'API :")
            st.json(response.json())

        except requests.exceptions.RequestException as e:
            st.error(f"❌ Erreur lors de la communication avec l'API : {e}")
    else:
        st.warning("⚠️ Veuillez sélectionner une image avant d'envoyer.")
