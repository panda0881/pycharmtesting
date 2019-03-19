import ujson as json
import node2vec
import networkx as nx
from gensim.models import Word2Vec
import logging
import random
import numpy as np
from sklearn.metrics import roc_auc_score
import pandas
from tqdm import tqdm


def divide_data(input_list, group_number):
    local_division = len(input_list) / float(group_number)
    random.shuffle(input_list)
    return [input_list[int(round(local_division * i)): int(round(local_division * (i + 1)))] for i in
            range(group_number)]


def get_G_from_edges(edges):
    tmp_G = nx.DiGraph()
    for edge in tqdm(edges):
        # add edges to the graph
        tmp_G.add_edge(edge[0], edge[1])
        # add weights for all the edges
        tmp_G[edge[0]][edge[1]]['weight'] = 1
    return tmp_G


def randomly_choose_false_edges(nodes, true_edges):
    tmp_list = list()
    all_edges = list()
    for i in range(len(nodes)):
        for j in range(len(nodes)):
            all_edges.append((i, j))
    random.shuffle(all_edges)
    for edge in all_edges:
        if edge[0] == edge[1]:
            continue
        if (nodes[edge[0]], nodes[edge[1]]) not in true_edges and (nodes[edge[1]], nodes[edge[0]]) not in true_edges:
            tmp_list.append((nodes[edge[0]], nodes[edge[1]]))
    return tmp_list


def get_neighbourhood_score(local_model, node1, node2):
    try:
        vector1 = local_model.wv.syn0[local_model.wv.index2word.index(node1)]
        vector2 = local_model.wv.syn0[local_model.wv.index2word.index(node2)]
        return np.dot(vector1, vector2) / (np.linalg.norm(vector1) * np.linalg.norm(vector2))
    except:
        return random.random()


def get_AUC(model, true_edges, false_edges):
    true_list = list()
    prediction_list = list()
    for edge in true_edges:
        tmp_score = get_neighbourhood_score(model, str(edge[0]), str(edge[1]))
        true_list.append(1)
        prediction_list.append(tmp_score)

    for edge in false_edges:
        tmp_score = get_neighbourhood_score(model, str(edge[0]), str(edge[1]))
        true_list.append(0)
        prediction_list.append(tmp_score)
    y_true = np.array(true_list)
    y_scores = np.array(prediction_list)
    return roc_auc_score(y_true, y_scores)


directed = True
p = 1
q = 1
num_walks = 10
walk_length = 10
dimension = 200
window_size = 5
num_workers = 4
iterations = 10
number_of_groups = 5

logging.basicConfig(format='%(asctime)s : %(levelname)s : %(message)s', level=logging.INFO)

# Start to load the raw network

train_edges = list()
raw_train_data = pandas.read_csv('train.csv')
for i, record in raw_train_data.iterrows():
    train_edges.append((str(record['head']), str(record['tail'])))

print('finish loading the train data')

G = node2vec.Graph(get_G_from_edges(train_edges), directed, p, q)
print('finish generate the graph')
G.preprocess_transition_probs()
print('finish generate the probability')
walks = G.simulate_walks(num_walks, walk_length)
print('finish the random walk')
model = Word2Vec(walks, size=dimension, window=window_size, min_count=0, sg=1, workers=num_workers, iter=iterations)


valid_positive_edges = list()
valid_negative_edges = list()
raw_valid_data = pandas.read_csv('valid.csv')
for i, record in raw_valid_data.iterrows():
    if record['label']:
        valid_positive_edges.append((str(record['head']), str(record['tail'])))
    else:
        valid_negative_edges.append((str(record['head']), str(record['tail'])))
tmp_AUC_score = get_AUC(model, valid_positive_edges, valid_negative_edges)

print('tmp_accuracy:', tmp_AUC_score)

print('end')
