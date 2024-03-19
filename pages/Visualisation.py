# Les librairies principaux
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from front         import *
from functions     import *

# Fonction permettent d'afficher des countplot.
def count_plot(y: str, hue: str, colors: str, data):
    plt.rcParams.update({'font.size': 16})  
    fig = plt.figure(figsize=(15, 11))
    data['Group Age'] = pd.cut(data['age'],
                               bins=[10, 20, 30, 40, 50, 60, 70, 80, np.inf],
                               labels=['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+'])
    
    sns.countplot(data=data, y=y, hue=hue, palette=sns.color_palette(colors))
    fig.set_facecolor('none')
    
    plt.xlabel('')  
    plt.ylabel('')  

    plt.box(False)
    return fig


# Fonction pour afficher des fromages.
def fromage(data, labels:list, colors:list, titre:str, titre_legende:str, sexe:str):
    data_homme_femme = data.loc[data['sexe'] == sexe]
    data_yes_no = data_homme_femme["compte_bancaire"].value_counts()
    fig, ax = plt.subplots()
    wedges, texts, autotexts = ax.pie([data_yes_no[0], data_yes_no[1]], labels=None, colors=colors, autopct='%0.0f%%', shadow=True)  # Correction de l'indexation ici
    ax.set_title(titre, pad=20)
    legend = ax.legend(labels, title=titre_legende)  
    legend_frame = legend.get_frame()  
    legend_frame.set_edgecolor('#d4e8e5') 
    centre_circle = plt.Circle((0,0),0.70,fc='white')
    fig.gca().add_artist(centre_circle)
    ax.axis('equal')
    fig.set_facecolor('none')
    return fig

# =================================================================================================================================>

def visualisation():
    set_background(png_file="background_2.jpg")
    css_texte(color="#014b4b", size="43px", texte="Analyse des données")
    css_texte(color="#014b4b", size="25px", texte="Inclusion Financière")
    # delete_bar_of_the_top()
    side_bar_background()
    
    # ====================>
    
    # Récupération des données.
    st.title("")
    if button_css(button='Analyser les données', margin_left="215px"):
        data = call_API_get_data()
        data = pd.DataFrame(data)
        st.title("")
        st.title("")
        st.title("")
        

        # ====================>
        
        # Graphique concernant l'ouverture de compte pour les femmes
        css_texte(color="#014b4b", size="25px", texte="Autorisation ouverture Femme")
        fig = fromage(
            data=data,
            labels=["Non","Oui"], 
            colors=['#014b4b','#d4e8e5'], 
            titre="", 
            titre_legende="Réponse",
            sexe ="Female"
        )
        st.pyplot(fig)
        st.title("")
        st.title("")
        # ====================>
        
        # Graphique concernant l'ouverture de compte pour les hommes
        css_texte(color="#014b4b", size="25px", texte="Autorisation ouverture Homme")
        fig = fromage(
            data=data,
            labels=["Non","Oui"], 
            colors=['#014b4b','#d4e8e5'], 
            titre="", 
            titre_legende="Réponse",
            sexe ="Male"
        )
        st.pyplot(fig)
        
        # ====================>
        st.title("")
        st.title("")
        css_texte(color="#014b4b", size="25px", texte="Autorisation ouverture par groupe d'âge")
        b_currentprovider = count_plot(
            y="Group Age", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data
        )
        st.pyplot(b_currentprovider)
        
        # ====================>
        st.title("")
        st.title("")
        css_texte(color="#014b4b", size="25px", texte="Autorisation ouverture par pays")
        b_currentprovider = count_plot(
            y="pays", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data
        )
        st.pyplot(b_currentprovider)
        
        # ====================>
        st.title("")
        st.title("")
        css_texte(color="#014b4b", size="25px", texte="Autorisation ouverture par année")
        b_currentprovider = count_plot(
            y="annee", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data
        )
        st.pyplot(b_currentprovider)
        

visualisation()