import requests
import streamlit as st
from dotenv import load_dotenv
import os
import json


# Récupération du mot de passe API.   
load_dotenv()
api_key = os.environ.get("API_PASSWORD")


# ==============================================================================>
# Fonction permettent de vérifier un input est vide.
def check_form(features:list):
    for i in features:
        if not i:
            return False
    return True 
# ==============================================================================>
def call_API_init_database(api_key=api_key):
    response = requests.post(url=f"http://127.0.0.1:8000/database_init/?api_key={api_key}")
    if response.status_code == 200:
        st.success("Données insérées avec succès.")
    else:
        st.error("Échec de l'insertion des données.")
# ==============================================================================>
def call_API_insert_data(list_data:list, api_key=api_key):
    data = {index: valeur for index, valeur in enumerate(list_data)}    
    response = requests.post(url=f"http://127.0.0.1:8000/insert_data_db/?api_key={api_key}", json=data)
    if response.status_code == 200:
        st.success("Données insérées avec succès.")
    else:
        st.error("Échec de l'insertion des données.")
# ==============================================================================>
def call_API_preprocessing(list_data:list, api_key=api_key):
    data = {index: valeur for index, valeur in enumerate(list_data)}    
    response = requests.post(url=f"http://127.0.0.1:8000/preprocess/?api_key={api_key}", json=data)
    if response.status_code == 200:
        st.success("Données insérées avec succès.")
        return response.json()
    else:
        st.error("Échec de l'insertion des données.")
# ==============================================================================>






















