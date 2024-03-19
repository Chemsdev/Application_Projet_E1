import streamlit as st
from front import *
from options import *
from functions import *
import requests

def main():
    # delete_bar_of_the_top()
    formulaire_css()       
    css_texte(color="#014b4b", size="43px", texte="Inclusion Financière")
    css_texte(color="#014b4b", size="25px", texte="Évaluez votre éligibilité à l'ouverture d'un compte !")
    st.title("") 
    end_form = False
    col1, col2 = st.columns(2)
    side_bar_background()
    set_background(png_file="background.jpg")
    
    # Formulaire.
    with col1:      
        css_texte(color="#d4e8e5", size="23px", texte="Informations personnelles")
        st.title("")
        etat_civil       = st.selectbox("**Etat civil**", values_etat_civil ,key=4)
        age              = st.selectbox("**Age**", [i for i in range(10, 99)], key=9)
        sexe             = st.selectbox("**Sexe**", ["Homme","Femme"], key=123)
        pays             = st.selectbox("**Pays**",(values_pays), key=3)
        relation_famille = st.selectbox("**Relation familiale**", values_relation_famille, key=6)
        taille_menage    = st.selectbox("**Taille du ménage**", [i for i in range(1,15)], key=8)
        
    with col2:
        css_texte(color="#d4e8e5", size="23px", texte="Détails supplémentaires")
        st.title("")
        niveau_education     = st.selectbox("**Niveau d'éducation**", values_niveau_education, key=10)
        type_de_job          = st.selectbox("**Type de job**", values_type_job, key=5)
        acces_au_telephone      = st.selectbox("**Accès au téléphone**",["Oui", "Non"], key=2)
        type_de_localisation = st.selectbox("**Type de localisation**", ("Urban", "Rural"), key=1)
        annee                = st.selectbox("**Année**", values_annee, key=7)
    
    # Bouton permettent de lancer le processus.
    if button_css(button='Tester mon égibiliter', margin_left="215px"):
    
        # Toutes les features dans une liste
        features = [
            sexe,
            type_de_localisation, 
            acces_au_telephone,
            pays, 
            etat_civil,
            type_de_job, 
            relation_famille,
            annee,
            taille_menage,
            age,
            niveau_education,
        ]
        
        # Vérification si tous les champs sont remplis.
        if check_form(features=features):
            
            # Vérification faite, fin du formulaire.
            end_form = True
            
            # Appel API
            call_API_init_database()
            call_API_insert_data(list_data=features)
            data_preprocess = call_API_preprocessing(list_data=features)
            prediction = call_API_model(data=data_preprocess)
        
        # Message demandant à l'utilisateur de remplir tous le formulaire 
        else:
            st.title("")
            css_texte(color="#003f62", size="23px", texte="Veuillez remplir tous le formulaire !")
        
    # ================================================== Prediction ==================================================

    if end_form:
        
        # Affichage récapitulatif
        css_recapitulatif(features)
        
        # Affichage de la prédiction
        if prediction == 1.0:
            st.title("")
            st.title("")
            css_texte(color="#014b4b", size="23px", texte="Bonne nouvelle ! vous pouvez ouvrir un compte chez nous")
            css_predictions(prediction="ELIGIBLE", color="#014b4b")
        else:
            st.title("")
            st.title("")
            css_texte(color="#AA4A44", size="23px", texte="Désolé, vous ne pouvez pas ouvrir de compte chez nous...")
            css_predictions(prediction="NON ELIGIBLE", color="#AA4A44")


main()
