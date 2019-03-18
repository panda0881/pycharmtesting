import pandas
import ujson as json
from tqdm import tqdm

all_record = list()
with open('/home/data/corpora/YELP/yelp_dataset_challenge_round13/user.json', 'r') as f:
    for line in f:
        all_record.append(json.loads(line))

with open('selected_user_ids.json', 'r') as f:
    selected_user_ids = json.load(f)
selected_user_ids = set(selected_user_ids)

selected_edges = list()

for tmp_record in tqdm(all_record):
    if tmp_record['user_id'] in selected_user_ids:
        tmp_friends = tmp_record['friends'].split(', ')
        for friend_id in tmp_friends:
            if friend_id in selected_user_ids:
                selected_edges.append((tmp_record['user_id']))

print('extracted edges:', len(selected_edges))

with open('selected_edges.json', 'w') as f:
    json.dump(selected_edges, f)

print('end')
