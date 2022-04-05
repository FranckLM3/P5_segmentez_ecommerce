# Projet : Segmentez des clients d'un site e-commerce

**Autor :** Franck LE MAT

**Date :** 13/12/2021

**Durée totale :** 70 heures

## Background du projet :
Vous êtes consultant pour Olist, une solution de vente sur les marketplaces en ligne.
Olist souhaite que vous fournissiez à ses équipes d'e-commerce une segmentation des clients qu’elles pourront utiliser au quotidien pour leurs campagnes de communication.
Votre objectif est de comprendre les différents types d’utilisateurs grâce à leur comportement et à leurs données personnelles.
Vous devrez fournir à l’équipe marketing une description actionable de votre segmentation et de sa logique sous-jacente pour une utilisation optimale, ainsi qu’une proposition de contrat de maintenance basée sur une analyse de la stabilité des segments au cours du temps.
Données : https://www.kaggle.com/olistbr/brazilian-ecommerce


## Key point du projet :
- Réaliser une analyse exploratoire
- Tester différents méthodes non supervisées pour regrouper ensemble des clients de profils similaires. Ces catégories pourront être utilisées par l’équipe marketing pour mieux communiquer.
    - Méthodes testées : Clustering K-means, Clustering Hiérarchique, DBSCAN
    - Comparaison des performances (davies_bouldin_score, silouhette_score)
- La segmentation proposée doit être exploitable et facile d’utilisation pour l’équipe marketing.
- Vous évaluerez la fréquence à laquelle la segmentation doit être mise à jour, afin de pouvoir effectuer un devis de contrat de maintenance.
- Le code fourni doit respecter la convention PEP8, pour être utilisable par Olist.


## Livrables :
- Un notebook de l'analyse exploratoire (non cleané, pour comprendre votre démarche).
- Un notebook d’essais des différentes approches de modélisation (non cleané, pour comprendre votre démarche).
- Un support de présentation pour la soutenance.


## Compétences évaluées :
- Mettre en place le modèle d'apprentissage non supervisé adapté au problème métier
- Transformer les variables pertinentes d'un modèle d'apprentissage non supervisé
- Adapter les hyperparamètres d'un algorithme non supervisé afin de l'améliorer
- Évaluer les performances d’un modèle d'apprentissage non supervisé

