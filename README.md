### README pour le Projet de Classification de l'Obésité

# Analyse et Classification de l'Obésité

## Description

Ce projet vise à analyser un jeu de données relatif à l'obésité et à développer un modèle d'apprentissage automatique pour classifier les individus dans différentes catégories de poids en fonction de diverses caractéristiques. Le projet inclut le prétraitement des données, l'encodage des caractéristiques, l'entraînement et l'évaluation du modèle. De plus, plusieurs visualisations sont fournies pour comprendre la distribution des données et les relations entre différentes caractéristiques.

## Jeu de Données

Le jeu de données utilisé dans ce projet est `ObesityDataSet_raw_and_data_sinthetic.csv`, qui contient les colonnes suivantes :

- `Gender` : Genre de l'individu (Female, Male)
- `Age` : Âge de l'individu
- `Height` : Taille de l'individu
- `Weight` : Poids de l'individu
- `CALC` : Fréquence de consommation d'alcool
- `FAVC` : Consommation fréquente d'aliments à haute teneur calorique
- `FCVC` : Fréquence de consommation de légumes
- `NCP` : Nombre de repas principaux
- `SCC` : Consommation de nourriture entre les repas
- `SMOKE` : Habitude de fumer
- `CH2O` : Consommation quotidienne d'eau
- `family_history_with_overweight` : Antécédents familiaux de surpoids
- `FAF` : Fréquence de l'activité physique
- `TUE` : Temps passé sur les appareils technologiques
- `CAEC` : Consommation de nourriture en dehors de la maison
- `MTRANS` : Mode de transport
- `NObeyesdad` : Niveau d'obésité (variable cible)

## Structure du Projet

- `data/` : Contient le fichier du jeu de données.
- `notebooks/` : Contient des notebooks Jupyter pour l'analyse des données, la visualisation et l'entraînement du modèle.
- `src/` : Contient des scripts Python pour le prétraitement des données, l'encodage des caractéristiques et l'entraînement du modèle.
- `models/` : Contient les modèles entraînés et les encodeurs.
- `README.md` : Description du projet et instructions de configuration.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votreutilisateur/obesity-analysis.git
    cd obesity-analysis
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Installez les paquets requis :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

### Prétraitement des Données et Entraînement du Modèle

Exécutez le script Python pour prétraiter les données et entraîner le modèle :
```sh
python src/train_model.py
```

### Visualisation

Exécutez le script de visualisation pour générer divers graphiques :
```sh
python src/visualize_data.py
```

### Notebooks d'Exemple

Explorez les notebooks Jupyter pour une analyse détaillée et des explications étape par étape :
```sh
jupyter notebook notebooks/
```

## Visualisations

Le projet inclut les visualisations suivantes :

1. **Répartition des Classes** : Répartition des différentes catégories de poids.
2. **Répartition des Genres** : Répartition des genres dans le jeu de données.
3. **Histogramme de l'Âge** : Distribution des âges dans le jeu de données.
4. **Distribution de la Taille** : Distribution des tailles dans le jeu de données.
5. **Habitude de Fumer** : Répartition des habitudes de tabagisme.
6. **Antécédents Familiaux de Surpoids** : Répartition des antécédents familiaux de surpoids.
7. **Consommation de Fast Food** : Répartition de la consommation de fast food.
8. **Distribution du Poids par Tranche d'Âge** : Poids moyen par tranche d'âge.
9. **Diagramme en Soleil** : Répartition des catégories de poids par genre.

## Résultats

Le modèle `RandomForestClassifier` a été entraîné avec les hyperparamètres suivants :

- `n_estimators` : 200
- `max_depth` : None
- `min_samples_split` : 5
- `min_samples_leaf` : 1

### Performance du Modèle

- **Précision** : 0.95
- **Rapport de Classification** :
    ```
                         precision    recall  f1-score   support

    Insufficient_Weight       1.00      0.96      0.98        56
          Normal_Weight       0.88      0.92      0.90        62
         Obesity_Type_I       0.99      0.96      0.97        78
        Obesity_Type_II       0.97      0.98      0.97        58
       Obesity_Type_III       1.00      1.00      1.00        63
     Overweight_Level_I       0.86      0.88      0.87        56
    Overweight_Level_II       0.98      0.96      0.97        50

               accuracy                           0.95       423
              macro avg       0.95      0.95      0.95       423
           weighted avg       0.95      0.95      0.95       423
    ```

## Contribution

N'hésitez pas à forker ce dépôt et à contribuer en soumettant une pull request. Veuillez vous assurer que vos modifications sont bien documentées et incluent les tests nécessaires.

## Licence

Ce projet est sous licence MIT. Voir le fichier [LICENSE](LICENSE) pour plus de détails.

## Remerciements

Merci aux créateurs du jeu de données et à tous les contributeurs des bibliothèques open-source utilisées dans ce projet.

---

N'hésitez pas à personnaliser ce README pour l'adapter aux détails spécifiques et aux exigences de votre projet.### README pour le Projet de Classification de l'Obésité

# Analyse et Classification de l'Obésité

## Description

Ce projet vise à analyser un jeu de données relatif à l'obésité et à développer un modèle d'apprentissage automatique pour classifier les individus dans différentes catégories de poids en fonction de diverses caractéristiques. Le projet inclut le prétraitement des données, l'encodage des caractéristiques, l'entraînement et l'évaluation du modèle. De plus, plusieurs visualisations sont fournies pour comprendre la distribution des données et les relations entre différentes caractéristiques.

## Jeu de Données

Le jeu de données utilisé dans ce projet est `ObesityDataSet_raw_and_data_sinthetic.csv`, qui contient les colonnes suivantes :

- `Gender` : Genre de l'individu (Female, Male)
- `Age` : Âge de l'individu
- `Height` : Taille de l'individu
- `Weight` : Poids de l'individu
- `CALC` : Fréquence de consommation d'alcool
- `FAVC` : Consommation fréquente d'aliments à haute teneur calorique
- `FCVC` : Fréquence de consommation de légumes
- `NCP` : Nombre de repas principaux
- `SCC` : Consommation de nourriture entre les repas
- `SMOKE` : Habitude de fumer
- `CH2O` : Consommation quotidienne d'eau
- `family_history_with_overweight` : Antécédents familiaux de surpoids
- `FAF` : Fréquence de l'activité physique
- `TUE` : Temps passé sur les appareils technologiques
- `CAEC` : Consommation de nourriture en dehors de la maison
- `MTRANS` : Mode de transport
- `NObeyesdad` : Niveau d'obésité (variable cible)

## Structure du Projet

- `data/` : Contient le fichier du jeu de données.
- `notebooks/` : Contient des notebooks Jupyter pour l'analyse des données, la visualisation et l'entraînement du modèle.
- `src/` : Contient des scripts Python pour le prétraitement des données, l'encodage des caractéristiques et l'entraînement du modèle.
- `models/` : Contient les modèles entraînés et les encodeurs.
- `README.md` : Description du projet et instructions de configuration.

## Installation

1. Clonez le dépôt :
    ```sh
    git clone https://github.com/votreutilisateur/obesity-analysis.git
    cd obesity-analysis
    ```

2. Créez un environnement virtuel et activez-le :
    ```sh
    python3 -m venv venv
    source venv/bin/activate
    ```

3. Installez les paquets requis :
    ```sh
    pip install -r requirements.txt
    ```

## Utilisation

### Prétraitement des Données et Entraînement du Modèle

Exécutez le script Python pour prétraiter les données et entraîner le modèle :
```sh
python src/train_model.py
```

### Visualisation

Exécutez le script de visualisation pour générer divers graphiques :
```sh
python src/visualize_data.py
```

### Notebooks d'Exemple

Explorez les notebooks Jupyter pour une analyse détaillée et des explications étape par étape :
```sh
jupyter notebook notebooks/
```

## Visualisations

Le projet inclut les visualisations suivantes :

1. **Répartition des Classes** : Répartition des différentes catégories de poids.
2. **Répartition des Genres** : Répartition des genres dans le jeu de données.
3. **Histogramme de l'Âge** : Distribution des âges dans le jeu de données.
4. **Distribution de la Taille** : Distribution des tailles dans le jeu de données.
5. **Habitude de Fumer** : Répartition des habitudes de tabagisme.
6. **Antécédents Familiaux de Surpoids** : Répartition des antécédents familiaux de surpoids.
7. **Consommation de Fast Food** : Répartition de la consommation de fast food.
8. **Distribution du Poids par Tranche d'Âge** : Poids moyen par tranche d'âge.

## Résultats

Le modèle `RandomForestClassifier` a été entraîné avec les hyperparamètres suivants :

- `n_estimators` : 150
- `max_depth` : None
- `min_samples_split` : 10


### Performance du Meilleur Modèle

- **Précision** : 0.7329
- **Rapport de Classification** :

| Classe                | Précision | Recall | F1-Score | Support |
|-----------------------|-----------|--------|----------|---------|
| Insufficient_Weight   | 0.77      | 0.77   | 0.77     | 56      |
| Normal_Weight         | 0.61      | 0.61   | 0.61     | 62      |
| Obesity_Type_I        | 0.79      | 0.72   | 0.75     | 78      |
| Obesity_Type_II       | 0.78      | 0.91   | 0.84     | 58      |
| Obesity_Type_III      | 0.88      | 0.97   | 0.92     | 63      |
| Overweight_Level_I    | 0.62      | 0.57   | 0.59     | 56      |
| Overweight_Level_II   | 0.60      | 0.54   | 0.57     | 50      |

|     Moyenne           | 0.73      | 0.73   | 0.73     | 423     |

## Contribution

N'hésitez pas à forker ce dépôt et à contribuer en soumettant une pull request. Veuillez vous assurer que vos modifications sont bien documentées et incluent les tests nécessaires.



## Remerciements

Merci aux créateurs du jeu de données et à tous les contributeurs des bibliothèques open-source utilisées dans ce projet.

---