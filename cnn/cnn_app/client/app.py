import streamlit as st
import requests

# 📌 Configuration des URLs de l'API
API_UPLOAD_URL = "http://127.0.0.1:8081/predictions/satelite/"  # URL pour l'envoi des images
API_PREDICTIONS_URL = "http://127.0.0.1:8081/predictions/"  # URL pour récupérer les prédictions

# 🏷️ Titre de l'application
st.title("🛰️ Application CNN - Classification d'Images Satellites")

# 📌 Ajout de la **sidebar** pour la navigation
st.sidebar.title("🔍 Navigation")
menu = st.sidebar.radio("Navigation", ["📤 Upload d'image", "📋 Voir les prédictions"])

# 📌 **Page : Upload d'image**
if menu == "📤 Upload d'image":
    st.header("📤 Upload d'une image et envoi vers l'API")

    # 📂 Formulaire de dépôt de fichier
    with st.form("upload_form"):
        uploaded_file = st.file_uploader("Choisissez une image", type=["jpg", "jpeg", "png"])
        submit_button = st.form_submit_button("Envoyer")

    # 🔄 Si le formulaire est soumis
    if submit_button:
        if uploaded_file is not None:
            # 🖼️ Afficher l'image uploadée
            st.image(uploaded_file, caption="Image envoyée", use_column_width=True)

            # 📤 Préparer le fichier pour l'envoi à l'API
            files = {"file": (uploaded_file.name, uploaded_file, uploaded_file.type)}

            # 🚀 Envoie la requête POST à l'API
            try:
                response = requests.post(API_UPLOAD_URL, files=files)
                response.raise_for_status()  # Vérifie si l'API retourne une erreur HTTP

                # ✅ Affiche la réponse de l'API
                st.success("✅ Réponse de l'API :")
                st.json(response.json())

            except requests.exceptions.RequestException as e:
                st.error(f"❌ Erreur lors de la communication avec l'API : {e}")
        else:
            st.warning("⚠️ Veuillez sélectionner une image avant d'envoyer.")

# 📌 **Page : Voir les prédictions enregistrées**
elif menu == "📋 Voir les prédictions":
    st.header("📋 Liste des prédictions enregistrées")

    # 📡 Récupérer les prédictions depuis l'API
    try:
        response = requests.get(API_PREDICTIONS_URL)
        response.raise_for_status()
        predictions = response.json()

        # Vérifier s'il y a des prédictions
        if predictions:
            for prediction in predictions:
                with st.expander(f"📌 Prédiction {prediction['id']}"):
                    st.write(prediction["image"])
                    st.write(f"🔹 **Label prédit** : {prediction['label']}")
                    st.write(f"📝 **Commentaire** : {prediction['commentaire']}")
                    st.write(f"🛠️ **Modèle utilisé** : {prediction['modele']}")
        else:
            st.info("Aucune prédiction enregistrée pour le moment.")
    
    except requests.exceptions.RequestException as e:
        st.error(f"❌ Erreur lors de la récupération des prédictions : {e}")
