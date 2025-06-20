# tp_spark.py
# TP Spark : Liste des amis communs entre Sidi (1) et Mohamed (2)

from pyspark import SparkContext

sc = SparkContext("local", "AmisCommunsTP")

# Charger les données
data = sc.textFile("file://./mini_tp_spark.txt")

# Générer les paires triées (min, max) avec leur liste d'amis
def generate_pairs(line):
    parts = line.split()
    user_id = parts[0]
    friends = parts[2].split(",")
    pairs = []
    for friend in friends:
        pair = tuple(sorted([user_id, friend]))
        pairs.append((pair, set(friends)))
    return pairs

pair_rdd = data.flatMap(generate_pairs)

# Calcul des amis communs par intersection
common_friends = pair_rdd.reduceByKey(lambda a, b: a & b)

# Filtrer la paire (1,2)
result = common_friends.filter(lambda x: x[0] == ('1', '2')).collect()

# Afficher le résultat proprement
for pair, friends in result:
    print(f"Paire: {pair[0]} Sidi {pair[1]} Mohamed -> Amis communs: {', '.join(friends) if friends else 'Aucun'}")

# Sauvegarder dans un fichier
sc.parallelize([
    f"{pair[0]} Sidi {pair[1]} Mohamed -> Amis communs: {', '.join(friends) if friends else 'Aucun'}"
    for pair, friends in result
]).saveAsTextFile("file://./output_tp")

sc.stop()
