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
def button_css(button:str, margin_left="13px"):
    st.markdown(
        f"""
        <style>
            .stButton>button {{
                font-weight: bold;
                background-color: #014b4b; 
                color: white; 
                padding: 10px 15px; 
                border-radius: 5px; 
                width: 275px;
                margin-left:{margin_left};
            }}
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

# =============================================================>    

# Fonction permettent de change la couleur de la sidebar.
def side_bar_background():
    st.markdown("""
        <style>
            [data-testid=stSidebar] {
                background-color: #014b4b;
            }
        </style>
        """, unsafe_allow_html=True)

# =============================================================>    

# Fonction permettent de retirer la bar noir en haut de l'app.
def delete_bar_of_the_top():
    hide_decoration_bar_style = '''
    <style>
        header {visibility: hidden;}
    </style>
    '''
    st.markdown(hide_decoration_bar_style, unsafe_allow_html=True)
# =============================================================>    

# Fonction permettent d'afficher la prédictions
def css_recapitulatif(user_inputs):
    if user_inputs[2] == "Oui":
        user_inputs[2] = "Joignable au téléphone"
    else:
        user_inputs[2] = "Non joignable au téléphone"
    user_inputs[8] = f"taille de ménage, {user_inputs[8]}"
    user_inputs[9] = f"{user_inputs[9]} ans"
    
    
    # Etat civil 4
    # Niveau d'éducation -1
    # type de job 5
    
    if "Ne sais pas" in user_inputs[4]:
        user_inputs[4] = "Etat civil, non déclaré"
    
    if "Ne sais pas" in user_inputs[-1]:
        user_inputs[-1] = "Niveau d'éducation, non déclaré"
        
    if "Ne sait pas" in user_inputs[5]:
        user_inputs[5] = "Type de job, non déclaré"
    
    
    st.markdown(
        """
        <style>
            .custom-block2 {
                background: #014b4b;   
                border-radius: 10px; 
                color:#white;
                padding: 15px; 
                justify-content: center; 
                align-items: center; 
                text-align:center;
                font-weight: bold;
                width: 410px; 
                height: 475px;
                margin-left:145px;
                font-size: 18px;
            }

        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown(
        f"""
        <div class='custom-block2'>
           <h3 style="color:#d4e8e5";"text-align:center";>Votre récapitulatif</h1>
            {'<br>'.join([f'{i}<span style=color:#f4ddb1;font-size:21px;></span>' for i in user_inputs])}
            <p></p>
        </div>
        """,
        unsafe_allow_html=True
    )