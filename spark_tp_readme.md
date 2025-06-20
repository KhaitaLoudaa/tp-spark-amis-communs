# TP Spark : Liste des amis communs entre Sidi et Mohamed

## Objectif

Développer un programme en PySpark pour découvrir la liste des amis communs entre deux utilisateurs dans un graphe social représenté sous forme de fichier texte.

## Format des données

Chaque ligne du fichier `mini_tp_spark.txt` contient :

```
<user_id> <Nom> <friend_id1>,<friend_id2>,...
```

Exemple :

```
1 Sidi 2,3,4
2 Mohamed 1,3,4
3 Ali 1,2,4
```

## Étapes d'exécution

1\. Supprimez le dossier `output_tp` s’il existe déjà :

```bash
rm -r output_tp
```

2\. Lancez le script avec PySpark :

```bash
pyspark tp_spark.py
```

3\. Les résultats sont générés dans :

```
output_tp/
```

et sont également affichés dans le terminal.

## Fonctionnalités

- Génération de couples d'amis triés (min, max)
- Calcul des amis communs
- Filtrage des amis communs pour la paire (1, 2)
- Sauvegarde des résultats

## Auteur

Khaita Loudaa

