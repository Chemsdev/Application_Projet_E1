import pandas as pd
from tools import *
import streamlit as st

from options import *


# Fonction permettent de vérifier un input est vide.
def check_form(features:list):
    for i in features:
        if not i:
            return False
    return True 


# Fonction permettent d'insérer les données saisit dans la table raw_data.
def send_data(features):
    # Connexion à la base de données.
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    columns_table = [
        "compte_bancaire",
        "pays",
        "annee",
        "type_de_localisation",
        "acces_au_telephone",
        "taille_du_menage",
        "age",
        "sexe",
        "relation_avec_le_chef_de_famille",
        "etat_civil",
        "niveau_education",
        "type_de_job"
    ]

    data = {}
    for column, feature in zip(columns_table, features):
        data[column] = feature
    data = pd.DataFrame([data])
    st.title(type(data))
    data.to_sql("raw_data", index=False, con=engine_azure, if_exists="append")
    st.write(data.dtypes)
    engine_azure.close()


