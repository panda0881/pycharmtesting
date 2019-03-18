import pandas

tmp_data = pandas.read_excel('Mcrae.xlsx')
print(tmp_data)

all_words = list()
for index, line in tmp_data.iterrows():
    all_words.append(line['VERB'])
    all_words.append(line['NOUN_or_NP'])

print(len(all_words))
print(all_words)
all_words_set = set(all_words)
print(len(all_words_set))