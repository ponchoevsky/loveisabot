from nltk.corpus import wordnet as wn

f = open('adjectives_file.txt', 'w')



all_adjectives = []

adjectives = list(wn.all_synsets('a'))

all_adjectives = list(set([x.name().split(".")[0] for x in adjectives]))
all_adjectives.sort()

for i in all_adjectives[2:]:
	f.write("love is ")
	f.write(i.replace("_"," "))
	f.write('\n')


f.close()
#print adjectives[0:10]