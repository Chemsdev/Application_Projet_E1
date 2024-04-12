from functions import *
from front import *
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pages.Visualisation import *





# ===================================================================>

# Fonction permettent d'accélerer l'affichage des performances.
def save_csv_or_get_data_performance():
    folder = os.listdir()  
    if 'performance.csv' not in folder:
        data = call_API_get_data_performance()
        data.to_csv('performance.csv', index=False, encoding='utf-8')
    else:
        data = pd.read_csv("performance.csv")
    return data

# ===================================================================>

# Fonction permettent de comparer les performances du modèles dans le temps.
def barplot_performance(selected_metric: str, data):
    st.title("")
    legend_css(classe_0="Refusé", classe_1="Accepté")
    st.title("")
    fig = plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Model', y=selected_metric, hue='Classe', data=data, palette=sns.color_palette(["#d4e8e5", "#014b4b"]))
    plt.xlabel(None)
    plt.ylabel(None)
    fig.set_facecolor('none')
    plt.tight_layout()
    plt.box(False)
    plt.xticks(fontsize=13)
    plt.yticks(fontsize=13)
    ax.legend_.remove()
    st.pyplot(plt)
    st.title("")

# ===================================================================>

# Fonction permettent d'afficher les performances du modèles (métriques)
def show_metrics_performance(data, classe: int):
    
    if "Refusé" in classe:
        classe = 0
    else:
        classe = 1
    
    css_texte(color="#014b4b", size="20px", texte=f"Métriques et Support")
    data["Model"] = data["Model"].astype(str)
    performance_year2016           = data[(data["Model"] == "2016") & (data["Classe"] == classe)]
    performance_year2016_2017      = data[(data["Model"] == "2017") & (data["Classe"] == classe)]
    performance_year2016_2017_2018 = data[(data["Model"] == "2018") & (data["Classe"] == classe)]
    
    formulaire_css()       
    col1, col2, col3 = st.columns(3)
    for performance, column in zip([performance_year2016, performance_year2016_2017, performance_year2016_2017_2018], [col1, col2, col3]):
        with column:
            css_texte(color="white",   size="20px", texte=f"Modèle {performance['Model'].values[0]}")
            css_texte(color="#d4e8e5", size="20px", texte=f"Recall    : {performance['recall'].values[0]} ")
            css_texte(color="#d4e8e5", size="20px", texte=f"Precision : {performance['precision'].values[0]} ")
            css_texte(color="#d4e8e5", size="20px", texte=f"F1 Score  : {performance['f1score'].values[0]} ")
    formulaire_css()       
    col1, col2, col3 = st.columns(3)
    
    for performance, column in zip([performance_year2016, performance_year2016_2017, performance_year2016_2017_2018], [col1, col2, col3]):
        with column:
            st.write()
            css_texte(color="#d4e8e5", size="20px", texte=f"{performance['support'].values[0]} ")
# ===================================================================>


def monitoring():
    set_background(png_file="background_2.jpg")
    side_bar_background()
    selectbox_css()
    

    # Récupération des données de performances.
    performance = save_csv_or_get_data_performance()

    # Titre de la page.
    css_texte(color="#014b4b", size="25px", texte="Evolution du modèle")
    
    # L'utilisateur choisit une métrique.
    selected_metric = st.selectbox('**Veuillez choisir la métrique**', ['precision', 'recall', 'f1score'])
    
    # Visualisation.
    barplot_performance(selected_metric=selected_metric, data=performance)
    classe = st.selectbox("**Veuillez choisir une classe**", ["Refusé", "Accepté"])
    st.title("")
    show_metrics_performance(data=performance, classe=classe)
    st.title("")
    


   
   
monitoring()