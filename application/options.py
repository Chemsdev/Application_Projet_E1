# Les inputs disponibles pour les features.
values_type_job = [
    "Travailleur indépendant",
    "Employé informel",
    "Agriculture et pêche",
    "Dépendant des envois de fonds",
    "Autres revenus",
    "Employé formel - secteur privé",
    "Aucun revenu",
    "Employé formel - secteur public",
    "Dépendant du gouvernement",
    "Ne sait pas/Refuse de répondre"
]

values_niveau_education = [
    'Autre/Ne sais pas/Refuse de répondre',
    'Aucune éducation formelle',
    'Éducation primaire',
    'Éducation secondaire', 
    'Formation professionnelle/spécialisée', 
    'Éducation tertiaire', 
]

values_etat_civil = [
    'Marié(e)/Vie en couple', 
    'Veuf/Veuve', 
    'Célibataire/Jamais marié(e)',
    'Divorcé(e)/Séparé(e)', 
    'Ne sais pas'
]

values_relation_famille = [
    'Conjoint(e)', 
    'Chef de famille', 
    'Autre membre de la famille', 
    'Enfant', 
    'Parent',
    'Autres non-parents'
]


values_annee = [
    "2016",
    "2017",
    "2018"
]


values_pays = [
    'Kenya', 
    'Rwanda', 
    'Tanzania', 
    'Uganda'
]

values_group_age = [
    "Group_Age_10_20",
    "Group_Age_20_30",
    "Group_Age_30_40",
    "Group_Age_40_50",
    "Group_Age_50_60",
    "Group_Age_60_70",
    "Group_Age_70_80",
    "Group_Age_80",
]

# =============================================================================================>

# Les colonnes de la table preprocessing séparées pour l'encodage.
columns_etat_civil = {
    "etat_civil_marie_vie_en_couple": 0.0,
    "etat_civil_veuf_veuve": 0.0,
    "etat_civil_celibataire_jamais_marie": 0.0,
    "etat_civil_divorce_separe": 0.0,
    "etat_civil_ne_sais_pas": 0.0,
}

columns_type_de_job = {
    "type_de_job_travailleur_independant": 0.0,
    "type_de_job_employe_informel": 0.0,
    "type_de_job_agriculture_et_peche": 0.0,
    "type_de_job_dependant_des_envois_de_fonds":0.0,
    "type_de_job_autres_revenus": 0.0,
    "type_de_job_employe_formel_secteur_prive": 0.0,
    "type_de_job_aucun_revenu": 0.0,
    "type_de_job_employe_formel_secteur_public": 0.0,
    "type_de_job_dependant_du_gouvernement": 0.0,
    "type_de_job_ne_sait_pas_refuse_de_repondre": 0.0,
}

columns_relation_chef_famille = {
    "relation_avec_le_chef_de_famille_conjoint_e": 0.0,
    "relation_avec_le_chef_de_famille_chef_de_famille": 0.0,
    "relation_avec_le_chef_de_famille_autre_membre_de_la_famille": 0.0,
    "relation_avec_le_chef_de_famille_enfant": 0.0,
    "relation_avec_le_chef_de_famille_parent": 0.0,
    "relation_avec_le_chef_de_famille_autres_non_parents": 0.0,
}

columns_annee = {
    "annee_2016":0.0,
    "annee_2017":0.0,
    "annee_2018":0.0
}


columns_pays = {
    'pays_Kenya'    :0.0, 
    'pays_Rwanda'   :0.0, 
    'pays_Tanzania' :0.0, 
    'pays_Uganda'   :0.0
}


columns_group_age = {
    "Group_Age_10_20":0.0,
    "Group_Age_20_30":0.0,
    "Group_Age_30_40":0.0,
    "Group_Age_40_50":0.0,
    "Group_Age_50_60":0.0,
    "Group_Age_60_70":0.0,
    "Group_Age_70_80":0.0,
    "Group_Age_80"   :0.0,
}


