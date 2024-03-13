import streamlit as st
from front import *
from options import *
from functions import *
from preprocessing import *

def main():
    
    formulaire_css()       
    css_texte(color="#014b4b", size="43px", texte="Inclusion Financière")
    css_texte(color="#014b4b", size="25px", texte="Évaluez votre éligibilité à l'ouverture d'un compte !")
    
    st.title("") 

    end_form = False
    col1, col2 = st.columns(2)
    set_background(png_file="background.jpg")
    
    # Formulaire Fonction lambda 1. 
    with col1:      
        css_texte(color="#d4e8e5", size="23px", texte="Informations personnelles")
        st.title("")
        etat_civil       = st.selectbox("**Etat civil**", values_etat_civil ,key=4)
        age              = st.selectbox("**Age**", [i for i in range(1, 115)], key=9)
        sexe             = st.selectbox("**Sexe**", ["Homme","Femme"], key=123)
        pays             = st.selectbox("**Pays**",(values_pays), key=3)
        relation_famille = st.selectbox("**Relation familiale**", values_relation_famille, key=6)
        taille_menage    = st.selectbox("**Taille du ménage**", [i for i in range(1,15)], key=8)
        
        
    with col2:
        css_texte(color="#d4e8e5", size="23px", texte="Détails supplémentaires")
        st.title("")
        niveau_education     = st.selectbox("**Niveau d'éducation**", values_niveau_education, key=10)
        type_de_job          = st.selectbox("**Type de job**", values_type_job, key=5)
        acces_telephone      = st.selectbox("**Accès au téléphone**",["Oui", "Non"], key=2)
        type_de_localisation = st.selectbox("**Type de localisation**", ("Urban", "Rural"), key=1)
        annee                = st.selectbox("**Année**", values_annee, key=7)
    
    
    if button_css(button='Tester mon égibiliter'):
    
        # Toutes les features dans une liste
        features = [
            sexe,
            type_de_localisation, 
            acces_telephone,
            pays, 
            age,
            etat_civil,
            type_de_job, 
            relation_famille,
            annee,
            taille_menage,
            age,
            niveau_education,
        ]
        
        # Vérification si tous les champs sont remplis.
        # if check_form(features=features):
        preprocessing(features=features)
            
        #     # TODO : Preprocessing, Insertion des données, Modeling...
        #     send_data(features=features)
        #     end_form = True
            
            
            
        # else:
        #     st.title("")
        #     css_texte(color="#003f62", size="23px", texte="Veuillez remplir tous le formulaire !")
        
        
        
        
        
        
        
    # ================================================== Prediction ==================================================
    
    if end_form:
        st.title("")
        css_texte(color="#AA4A44", size="23px", texte="Désolé, vous ne pouvez pas ouvrir de compte chez nous...")
        css_predictions(prediction="NON ELIGIBLE", color="#AA4A44")
        st.title("")
        css_texte(color="#014b4b", size="23px", texte="Bonne nouvelle ! vous pouvez ouvrir un compte chez nous")
        css_predictions(prediction="ELIGIBLE",     color="#014b4b")
                


main()