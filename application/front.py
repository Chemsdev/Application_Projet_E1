import streamlit as st 
import base64


# =============================================================>

# CSS du formuaire. 
def formulaire_css():
    css="""
    <style>
        [data-testid="column"] {
            background: #014b4b;            
            box-shadow: rgb(0 0 0 / 20%) 0px 2px 1px -1px, rgb(0 0 0 / 14%) 0px 1px 1px 0px, rgb(0 0 0 / 12%) 0px 3px 5px 0px;
            border-radius: 10px;
            padding: 3%;
            width:80px;
            display: flex;
            # justify-content: center;
            # align-items: center;
            text-align:center;
            transition: background-color 0.3s ease; 
        }
        
        # [data-testid="column"]:hover {
        #         background-color: #d4e8e5; /* Nouvelle couleur de fond au survol */
        #         cursor: pointer; /* Curseur de la main pour indiquer la cliquabilité */
        #     }
    </style>
    """
    st.write(css, unsafe_allow_html=True)

# =============================================================>

# Fonction pour charger une image.
def get_base64(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()

# =============================================================>

# Fonction pour mettre une image en background.
def set_background(png_file):
    bin_str = get_base64(png_file)
    page_bg_img = '''
    <style>
    .stApp {
        background-image: url("data:image/png;base64,%s");
        background-size: cover;
    }
    </style>
    ''' % bin_str
    st.markdown(page_bg_img, unsafe_allow_html=True)
    
# =============================================================>

# Fonction pour ajouter du CSS au bouton.
def button_css(button:str):
    st.markdown(
        """
        <style>
            .stButton>button {
                font-weight: bold;
                background-color: #014b4b; 
                color: white; 
                padding: 10px 15px; 
                border-radius: 5px; 
                width: 275px;
                margin-left:13px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    # Utiliser les boutons personnalisés
    button2_clicked = st.button(f"**{button}**", key=button)
    return button2_clicked

# =============================================================>

# Permet d'apporter du CSS au texte/titre.
def css_texte(color:str, size:str, texte:str, font_family=""):
    new_title  = f'<h3 style="color:{color}; font-size: {size}; font-family:{font_family}; text-align:center"><b>{texte}</b></h3>'
    st.markdown(new_title, unsafe_allow_html=True)
    
# =============================================================>

# Fonction permettent d'afficher la prédictions
def css_predictions(prediction, color:str):
    st.markdown(
        f"""
        <style>
            .custom-block {{
                background-color: {color}; 
                color: white; 
                padding: 20px; 
                border-radius: 10px; 
                width: 700px; 
                height: 150px;
                display: flex; 
                justify-content: center; 
                align-items: center; 
                font-size: 60px;
                box-shadow: 0 0 20px 0 rgba(0, 0, 0, 0.2), 0 5px 5px 0 rgba(0, 0, 0, 0.24);  
                transition: background-color 0.3s ease; 
            }}
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(f"<div class='custom-block'>{prediction}</div>", unsafe_allow_html=True)