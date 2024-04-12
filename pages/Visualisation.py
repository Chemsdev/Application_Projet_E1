# Les librairies principaux
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

from front         import *
from functions     import *



# Prépaeation des données pour la visualisation.
def prepare_data_to_viz(data):
    data['Group Age'] = pd.cut(data['age'],
                            bins=[10, 20, 30, 40, 50, 60, 70, 80, np.inf],
                            labels=['10-20', '20-30', '30-40', '40-50', '50-60', '60-70', '70-80', '80+'])
    mapping = {
        'Married/Living together': 'Marié(e)', 
        'Widowed': 'Veuf/Veuve',  
        'Single/Never Married': 'Célibataire',
        'Divorced/Seperated': 'Divorcé(e)',
        "Don't know": 'Ne sais pas'  
    }
    data['etat_civil'] = data['etat_civil'].replace(mapping)
    return data

# Fonction permettent d'accélerer l'affichage de la données.
def save_csv_or_get_data():
    folder = os.listdir()  
    if 'data.csv' not in folder:
        data = call_API_get_data()
        data = prepare_data_to_viz(data)
        data.to_csv('data.csv', index=False, encoding='utf-8')
    else:
        data = pd.read_csv("data.csv")
    return data

# Fonction permettent d'apporter du CSS au selectbox.
def selectbox_css():
    st.markdown("""
        <style>
            .stSelectbox div[data-baseweb="select"] > div:first-child {
                background-color: #014b4b;
                text-color:#d4e8e5;
            }
        </style>
    """, unsafe_allow_html=True)


def legend_css(classe_0="Refusé", classe_1="Accepté"):
    css = """
    <style>
    .legend {
        display: flex;
        justify-content: center;
        list-style: none;
        padding: 0;
        margin-right:390px;
    }

    .legend-item {
        display: flex;
        align-items: center;
        margin-right: 20px;
    }

    .color-block {
        width: 30px;
        height: 20px;
        margin-right: 5px;
    }

    .yes {
        color: black;
        font-weight: bold; 
    }

    .no {
        color: black;
        font-weight: bold;
    }
    </style>
    """

    # Affichage du code CSS sur Streamlit
    st.markdown(css, unsafe_allow_html=True)

    # Affichage de la légende
    st.markdown(f"""
    <ul class="legend">
        <li class="legend-item"><div class="color-block" style="background-color: #014b4b;"></div><div class="yes">{classe_0}</div></li>
        <li class="legend-item"><div class="color-block" style="background-color: #d4e8e5;"></div><div class="no">{classe_1}</div></li>
    </ul>
    """, unsafe_allow_html=True)

# Fonction permettent d'afficher des countplot.
def count_plot(y: str, hue: str, colors: str, data, figsize:list, font_size=18):
    legend_css()
    plt.rcParams.update({'font.size': font_size})  
    fig = plt.figure(figsize=(figsize[0], figsize[1])) 
    ax = sns.countplot(data=data, y=y, hue=hue, palette=sns.color_palette(colors))
    fig.set_facecolor('none')
    plt.xlabel('', fontsize=18)  
    plt.ylabel('', fontsize=18)  
    plt.box(False)
    ax.legend_.remove()
    return fig

# =================================================================================================================================>

def visualisation():
    set_background(png_file="background_2.jpg")
    css_texte(color="#014b4b", size="43px", texte="Analyse des données")
    css_texte(color="#014b4b", size="25px", texte="Inclusion Financière")
    side_bar_background()
    selectbox_css()
    
    
    # Récupération des données. 
    data = save_csv_or_get_data()

    # Définir les options pour votre selectbox
    selected_option =  st.selectbox("**Choisissez une caractéristique**", ["Sexe", "Age", "Pays", "Année", "Etat civique", "Niveau d'éducation", "Type de job"])
    st.title("")
    st.title("")   
    

    # Graphique concernant l'ouverture de compte par âge.
    if selected_option == "Age":   
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par âge")
        st.title("")
        b_currentprovider = count_plot(
            y="Group Age", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[14,12]
        )
        st.pyplot(b_currentprovider)
    
    # # Graphique concernant l'ouverture de compte par pays.
    if selected_option == "Pays":   
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par pays")
        st.title("")
        b_currentprovider = count_plot(
            y="pays", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[14,7]
        )
        st.pyplot(b_currentprovider)
    
    # # Graphique concernant l'ouverture de compte par année.
    if selected_option == "Année":  
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par année")
        st.title("")
        b_currentprovider = count_plot(
            y="annee", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[14,5],
            font_size = 15
        )
        st.pyplot(b_currentprovider)
    
    # # Graphique concernant l'ouverture de compte par etat civique.
    if selected_option == "Etat civique":  
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par état civique")
        st.title("")
        b_currentprovider = count_plot(
            y="etat_civil", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[25,15],
            font_size = 25
        )
        st.pyplot(b_currentprovider)
        
        
    if selected_option == "Niveau d'éducation":  
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par niveau d'éducation")
        st.title("")
        b_currentprovider = count_plot(
            y="niveau_education", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[28,23],
            font_size = 33
        )
        st.pyplot(b_currentprovider)
    
        
    if selected_option == "Type de job": 
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par type de job")
        st.title("")
        b_currentprovider = count_plot(
            y="type_de_job", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[25,23],
            font_size = 33
            
        )
        st.pyplot(b_currentprovider)
        
    
    if selected_option == "Sexe": 
        css_texte(color="#014b4b", size="25px", texte="Autorisation à l'ouverture d'un compte par sexe")
        st.title("")
        b_currentprovider = count_plot(
            y="sexe", 
            hue="compte_bancaire", 
            colors=['#d4e8e5','#014b4b'],
            data=data,
            figsize=[12,3],
            font_size = 15
        )
        st.pyplot(b_currentprovider)
    
    
    
        

visualisation()
