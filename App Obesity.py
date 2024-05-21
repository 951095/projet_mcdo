import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt
import seaborn as sns

# Charger le modèle et les encodeurs
model = joblib.load('best_random_forest_model.pkl')
label_encoders = joblib.load('label_encoders.pkl')

# Charger les données pour les graphiques
data = pd.read_csv("ObesityDataSet_raw_and_data_sinthetic.csv")

# Sélectionner uniquement les caractéristiques nécessaires
X = data[["Gender", "Age", "Height", "SMOKE", "family_history_with_overweight", "FAVC", "MTRANS"]]
y = data["NObeyesdad"]

# Encoder les variables catégorielles pour correspondre au modèle formé
for column in X.select_dtypes(include=['object']).columns:
    X[column] = label_encoders[column].transform(X[column])

# Streamlit app
st.title("Prédiction de l'Obésité")

# Menu latéral pour la sélection de la page
page = st.sidebar.selectbox('Sélectionner une page', ['Prédiction', 'Graphiques'])

# Page des graphiques
if page == 'Graphiques':
    st.header('Graphiques')
    
    
    # Slider pour sélectionner le nombre de bins
    num_bins = st.slider("Nombre de Bins", min_value=5, max_value=50, value=30)

    # Description évolutive en fonction de la valeur du slider
    st.write(f"Affichage de la distribution de l'âge avec {num_bins} bins :")

    # Distribution de l'âge
    plt.figure(figsize=(10, 6))
    sns.histplot(data['Age'], bins=num_bins, kde=True)
    plt.title('Distribution de l\'Âge')
    st.pyplot(plt)


    # Boxplot de la taille par niveau d'obésité
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='NObeyesdad', y='Height', data=data)
    plt.title('Taille par Niveau d\'Obésité')
    plt.xticks(rotation=45)
    st.pyplot(plt)

    # Bar plot du tabagisme par niveau d'obésité (en pourcentage)
    plt.figure(figsize=(10, 6))
    smoke_obesity = data.groupby(['SMOKE', 'NObeyesdad']).size().unstack()
    smoke_obesity_percentage = smoke_obesity.div(smoke_obesity.sum(axis=1), axis=0) * 100
    smoke_obesity_percentage.plot(kind='bar', stacked=True)
    plt.title('Tabagisme par Niveau d\'Obésité (en pourcentage)')
    plt.xlabel('Tabagisme')
    plt.ylabel('Pourcentage')
    plt.xticks(rotation=45)
    plt.legend(title='Niveau d\'Obésité')
    plt.tight_layout()
    st.pyplot(plt)

    # Bar plot du mode de transport par niveau d'obésité (en pourcentage)
    plt.figure(figsize=(10, 6))
    mtrans_obesity = data.groupby(['MTRANS', 'NObeyesdad']).size().unstack()
    mtrans_obesity_percentage = mtrans_obesity.div(mtrans_obesity.sum(axis=1), axis=0) * 100
    mtrans_obesity_percentage.plot(kind='bar', stacked=True)
    plt.title('Mode de Transport par Niveau d\'Obésité (en pourcentage)')
    plt.xlabel('Mode de Transport')
    plt.ylabel('Pourcentage')
    plt.xticks(rotation=45)
    plt.legend(title='Niveau d\'Obésité')
    plt.tight_layout()
    st.pyplot(plt)

    # Distribution de la taille par genre et par niveau d'obésité
    plt.figure(figsize=(12, 6))
    sns.boxplot(x='Gender', y='Height', hue='NObeyesdad', data=data)
    plt.title('Distribution de la Taille par Genre et par Niveau d\'Obésité')
    plt.xlabel('Genre')
    plt.ylabel('Taille (cm)')
    plt.xticks(rotation=45)
    plt.legend(title='Niveau d\'Obésité')
    plt.tight_layout()
    st.pyplot(plt)
    
    # Exclure les colonnes non numériques du DataFrame pour le calcul des corrélations
    numeric_data = data.select_dtypes(include=['float64', 'int64'])
    
    # Heatmap des corrélations entre caractéristiques
    plt.figure(figsize=(10, 8))
    sns.heatmap(numeric_data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Heatmap des Corrélations entre Caractéristiques')
    plt.tight_layout()
    st.pyplot(plt)

    # Répartition des niveaux d'obésité
    plt.figure(figsize=(8, 6))
    data['NObeyesdad'].value_counts().plot(kind='bar')
    plt.title('Répartition des Niveaux d\'Obésité')
    plt.xlabel('Niveau d\'Obésité')
    plt.ylabel('Nombre d\'Individus')
    plt.xticks(rotation=45)
    plt.tight_layout()
    st.pyplot(plt)

    # Répartition des facteurs de risque
    fig, axes = plt.subplots(2, 2, figsize=(12, 10), sharey=True)
    for i, column in enumerate(['FAVC', 'SMOKE', 'family_history_with_overweight', 'MTRANS']):
        sns.countplot(x=column, hue='NObeyesdad', data=data, ax=axes[i//2, i%2])
        axes[i//2, i%2].set_title(f'Répartition de {column} par Niveau d\'Obésité')
        axes[i//2, i%2].set_xlabel(column)
        axes[i//2, i%2].set_ylabel('Nombre d\'Individus')
        axes[i//2, i%2].legend(title='Niveau d\'Obésité')
    plt.tight_layout()
    st.pyplot(fig)


# Page de prédiction
elif page == 'Prédiction':
    st.header('Prédiction de l\'Obésité')
    
    # Collecte des entrées utilisateur pour la prédiction
    gender = st.selectbox('Genre', ['Male', 'Female'])
    age = st.slider('Âge', 1, 100, 20)
    height = st.slider('Taille (en cm)', 100, 220, 110)
    smoke = st.selectbox('Fume', ['yes', 'no'])
    family_history = st.selectbox('Antécédents familiaux d\'obésité', ['yes', 'no'])
    favc = st.selectbox('Fréquence de consommation de nourriture hypercalorique (FAVC)', ['yes', 'no'])
    mtrans = st.selectbox('Mode de Transport (MTRANS)', ['Automobile', 'Motorbike', 'Bike', 'Public_Transportation', 'Walking'])

    # Convertir les entrées utilisateur
    gender = label_encoders['Gender'].transform([gender])[0]
    smoke = label_encoders['SMOKE'].transform([smoke])[0]
    family_history = label_encoders['family_history_with_overweight'].transform([family_history])[0]
    favc = label_encoders['FAVC'].transform([favc])[0]
    mtrans = label_encoders['MTRANS'].transform([mtrans])[0]

    if st.button('Prédire'):
        # Création d'un DataFrame avec les entrées utilisateur pour correspondre à l'entraînement du modèle
        input_data = pd.DataFrame([[gender, age, height, smoke, family_history, favc, mtrans]], 
                                  columns=['Gender', 'Age', 'Height', 'SMOKE', 'family_history_with_overweight', 'FAVC', 'MTRANS'])

        # Prédiction
        prediction = model.predict(input_data)
        st.write(f"Prédiction de l'obésité: {prediction[0]}")