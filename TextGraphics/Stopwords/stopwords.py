stopwords = []
stops = open('english.txt')
for line in stops:
	line = line.strip()
	stopwords.append(line)
print stopwords	