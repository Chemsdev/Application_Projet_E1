import streamlit as st
from front import *
from options import *

def main():
    
    formulaire_css()       
    css_texte(color="#014b4b", size="43px", texte="Inclusion Financière")
    css_texte(color="#014b4b", size="25px", texte="Évaluez votre éligibilité à l'ouverture d'un compte !")
    
    st.title("") 

    col1, col2 = st.columns(2)
    set_background(png_file="test.jpg")
    
    # Formulaire Fonction lambda 1. 
    with col1:      
        css_texte(color="#d4e8e5", size="23px", texte="Informations personnelles")
        st.title("")
        feature_1 = st.selectbox("**Etat civil**",etat_civil ,key=4)
        feature_1 = st.text_input("**Age**", key=9)
        feature_1 = st.selectbox("**Sexe**", ["Homme","Femme"], key=123)
        feature_1 = st.selectbox("**Pays**",('Kenya', 'Rwanda', 'Tanzania', 'Uganda'), key=3)
        feature_1 = st.selectbox("**Relation familiale**", relation_famille, key=6)
        feature_1 = st.text_input("**Taille du ménage**", key=8)
        
        
    with col2:
        css_texte(color="#d4e8e5", size="23px", texte="Détails supplémentaires")
        st.title('')
        feature_1 = st.selectbox("**Niveau d'éducation**", niveau_education, key=10)
        feature_1 = st.selectbox("**Type de job**", typejob, key=5)
        feature_1 = st.selectbox("**Accès au téléphone**",["Oui", "Non"], key=2)
        feature_1 = st.selectbox("**Type de location**", ("Urban", "Rural"), key=1)
        feature_1 = st.selectbox("**Année**", ["2018", "2016", "2017"], key=7)
    
    if button_css(button='Tester mon égibiliter'):
        st.title("")
        css_texte(color="#AA4A44", size="23px", texte="Désolé, vous ne pouvez pas ouvrir de compte chez nous...")
        css_predictions(prediction="NON ELIGIBLE", color="#AA4A44")
    else:
        st.title("")
        css_texte(color="#014b4b", size="23px", texte="Bonne nouvelle ! vous pouvez ouvrir un compte chez nous")
        css_predictions(prediction="ELIGIBLE",     color="#014b4b")
                


main()