from tools import *




# ===================================================================================================>

# Création de la table raw_data
def create_table_raw_data():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS raw_data (
                id_raw INT AUTO_INCREMENT PRIMARY KEY,
                compte_bancaire VARCHAR(10),
                pays VARCHAR(50),
                annee INT,
                type_de_localisation VARCHAR(50),
                acces_au_telephone VARCHAR(10),
                taille_du_menage INT,
                age INT,
                sexe VARCHAR(10),
                relation_avec_le_chef_de_famille VARCHAR(50),
                etat_civil VARCHAR(50),
                niveau_education VARCHAR(50),
                type_de_job VARCHAR(50)
            )
        """)
    engine_azure.close()
    print('Table raw_data créée avec succès !')
    
# ===================================================================================================>

# Création de la table preprocessing
def create_table_preprocessing():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS preprocessing (
                id_features INT AUTO_INCREMENT PRIMARY KEY,
                type_de_localisation FLOAT,
                acces_au_telephone FLOAT,
                
                pays_Kenya FLOAT,
                pays_Rwanda FLOAT,
                pays_Tanzania FLOAT,
                pays_Uganda FLOAT,

                Group_Age_10_20 FLOAT,
                Group_Age_20_30 FLOAT,
                Group_Age_30_40 FLOAT,
                Group_Age_40_50 FLOAT,
                Group_Age_50_60 FLOAT,
                Group_Age_60_70 FLOAT,
                Group_Age_70_80 FLOAT,
                Group_Age_80 FLOAT,
                
                etat_civil_marie_vie_en_couple FLOAT,
                etat_civil_veuf_veuve FLOAT,
                etat_civil_celibataire_jamais_marie FLOAT,
                etat_civil_divorce_separe FLOAT,
                etat_civil_ne_sais_pas FLOAT,

                type_de_job_travailleur_independant FLOAT,
                type_de_job_employe_informel FLOAT,
                type_de_job_agriculture_et_peche FLOAT,
                type_de_job_dependant_des_envois_de_fonds FLOAT,
                type_de_job_autres_revenus FLOAT,
                type_de_job_employe_formel_secteur_prive FLOAT,
                type_de_job_aucun_revenu FLOAT,
                type_de_job_employe_formel_secteur_public FLOAT,
                type_de_job_dependant_du_gouvernement FLOAT,
                type_de_job_ne_sait_pas_refuse_de_repondre FLOAT,

                relation_avec_le_chef_de_famille_conjoint_e FLOAT,
                relation_avec_le_chef_de_famille_chef_de_famille FLOAT,
                relation_avec_le_chef_de_famille_autre_membre_de_la_famille FLOAT,
                relation_avec_le_chef_de_famille_enfant FLOAT,
                relation_avec_le_chef_de_famille_parent FLOAT,
                relation_avec_le_chef_de_famille_autres_non_parents FLOAT,
                
                annee_2016 FLOAT,
                annee_2017 FLOAT,
                annee_2018 FLOAT,
                
                taille_du_menage INT,
                age INT,
                niveau_education_encode FLOAT
            )
        """)
    engine_azure.close()
    print('Table preprocessing créée avec succès !')

# ===================================================================================================>

# Fonction permettent de créer la table prédiction.
def create_table_prediction():
    config = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)
    
    with engine_azure.connect() as connection:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS raw_data (
                id_pred INT AUTO_INCREMENT PRIMARY KEY,
                id_features INT,
                prediction VARCHAR(50),
            )
        """)
    engine_azure.close()
    print('Table raw_data créée avec succès !')
    
# ===================================================================================================>

# Fonction permettent d'insérer la données brut.
def raw_data_init():
    
    # Création de la table raw_data
    create_table_raw_data()
    
    # Imporatation de la données brut.
    raw_data = pd.read_csv("data.csv")
    
    # Traduction des colonnes.
    raw_data = raw_data.rename(columns={
        'country': 'pays',
        'year': 'annee',
        'bank_account':'compte_bancaire',
        'location_type': 'type_de_localisation', 
        'cellphone_access': 'acces_au_telephone', 
        'household_size': 'taille_du_menage', 
        'age_of_respondent': 'age',
        'gender_of_respondent': 'sexe',
        'relationship_with_head':'relation_avec_le_chef_de_famille',
        'marital_status':'etat_civil', 
        'education_level':'niveau_education',
        'job_type':'type_de_job', 
    })

    # Connexion à la base de données.
    config       = set_confg(liste_connexion=AZURE_INCLUSION)
    engine_azure = connect_mysql(config=config)

    # Injection de la données brut.
    raw_data.to_sql("raw_data", index=False, con=engine_azure, if_exists="append")

    # Fermeture de la connexion.
    engine_azure.close()




# raw_data_init()
# create_table_preprocessing()