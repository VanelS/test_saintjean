import streamlit as st
import requests
import json

# Titre de l'application
st.title("Prédiction de survie Titanic")

# Créer un formulaire pour saisir les données du passager
st.header("Entrez les informations du passager")

# Saisie des données
Pclass = st.selectbox("Classe du passager (Pclass)", [1, 2, 3], format_func=lambda x: f"Classe {x}")
Sex = st.selectbox("Sexe", [0, 1], format_func=lambda x: "Homme" if x == 0 else "Femme")
Age = st.slider("Âge", 0, 100, 25)
Fare = st.slider("Prix du billet", 0, 550, 50)
Embarked = st.selectbox("Port d'embarquement", [0, 1, 2], format_func=lambda x: ["Cherbourg", "Queenstown", "Southampton"][x])

# Créer un bouton pour soumettre les données
if st.button("Prédire la survie"):
    # Créer les données du passager sous forme de dictionnaire
    passenger_data = {
        "Pclass": Pclass,
        "Sex": Sex,
        "Age": Age,
        "Fare": Fare,
        "Embarked": Embarked
    }

    # Envoyer une requête POST à l'API pour faire une prédiction
    response = requests.post("http://127.0.0.1:8000/predict/", json=passenger_data)

    # Si la réponse est réussie
    if response.status_code == 200:
        result = response.json()
        # Afficher le résultat
        st.success(f"Résultat : {result['prediction']}")
    else:
        st.error("Erreur dans la requête à l'API")
