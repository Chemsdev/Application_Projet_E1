from functions import *
from front import *
import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from pages.Visualisation import *


# Fonction permettent d'afficher les logs.
def apply_custom_css(table: str):
    log = table[table['Classe'] == 1][['LOG', 'Model']]
    
    st.markdown(
        """
        <style>
            .custom-block2 {
                background-color: #014b4b;   
                border-radius: 10px;
                color: white;
                padding: 15px;
                justify-content: center;
                align-items: center;
                width: 700px;
                height: 220px;
                font-size: 18px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Affichage du contenu avec le style personnalisé
    st.markdown(
        f"""
            <div class='custom-block2'>
                <p style="font-size:20px;color:white;font-weight: ;"> Modèle {log["Model"].values[0]} :  <span style=color:#d4e8e5;font-size:21px;>{log["LOG"].values[0]}</span></p>
                <p style="font-size:20px;color:white;font-weight: ;"> Modèle {log["Model"].values[1]} :  <span style=color:#d4e8e5;font-size:21px;>{log["LOG"].values[1]} </span></p>
                <p style="font-size:20px;color:white;font-weight: ;"> Modèle {log["Model"].values[2]} :  <span style=color:#d4e8e5;font-size:21px;>{log["LOG"].values[2]} </span></p>
                <p style="font-size:20px;color:white;font-weight: ;"> Modèle 2019 :  <span style=color:#FFCCCB;font-size:21px;>Attention ! le modèle subit une dégradation significative</span></p>
            </div>
        """,
        unsafe_allow_html=True
    )
    
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
    set_background(png_file="beige.jpg")
    side_bar_background()
    selectbox_css()
    

    # ===================== Comparaison des métriques des modèles.
    performance = save_csv_or_get_data_performance()
    css_texte(color="#014b4b", size="30px", texte="Evolution du modèle")
    selected_metric = st.selectbox('**Veuillez choisir la métrique**', ['precision', 'recall', 'f1score'])
    barplot_performance(selected_metric=selected_metric, data=performance)
    classe = st.selectbox("**Veuillez choisir une classe**", ["Refusé", "Accepté"])
    st.title("")
    
    # ===================== Visualisation des métriques du modèles.
    css_texte(color="#014b4b", size="25px", texte=f"Métriques et Support")
    show_metrics_performance(data=performance, classe=classe)
    st.title("")
    
    # ===================== Log des modèles.
    css_texte(color="#014b4b", size="25px", texte="Suivi des journaux d'évolution du modèle")
    apply_custom_css(table=performance)
    

   
   
monitoring()