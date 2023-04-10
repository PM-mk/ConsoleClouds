import re
import wordcloud
from wordcloud import WordCloud
from nltk.corpus import stopwords
from nltk import SnowballStemmer


def filter_and_stem_text(path: str) -> list[str]:
    file = open(path, 'r')
    text = file.read()
    text = re.sub(r'\'|\d|\.|@\w+|’|\(|\)', '', text).lower()
    text = re.sub(r'-|\W+', ' ', text)
    result = text.split()
    result = [word for word in result if word not in blacklist]
    for i in range(len(result)):
        if result[i] not in stem_stop:
            result[i] = sb.stem(result[i])

    return result


def generate_cloud(words: list[str], filename: str, color='white'):
    text_color = wordcloud.get_single_color_func(color)
    word_cloud = WordCloud(collocations=False, background_color='black',
                           max_words=50, min_word_length=4, scale=2, color_func=text_color).generate("+".join(words))
    word_cloud.to_file(filename)


sb = SnowballStemmer('english')
blacklist = set(stopwords.words('english'))
stem_stop = ['playstation', 'videogame', 'videogames', 'console', 'really', 'online', 'myrise', 'series']
corpusPS = filter_and_stem_text('./corpusPS.txt')
corpusXB = filter_and_stem_text('./corpusXB.txt')

# Generate clouds for each console

generate_cloud(corpusPS, 'PlayStation.png', 'blue')
generate_cloud(corpusXB, 'Xbox.png', 'green')

# Generate clouds for each console with terms exclusive to each

setPS, setXB = set(corpusPS), set(corpusXB)

uniquePS = [word for word in corpusPS if word not in setXB]
uniqueXB = [word for word in corpusXB if word not in setPS]
generate_cloud(uniquePS, 'PlayStationUnique.png', 'blue')
generate_cloud(uniqueXB, 'XboxUnique.png', 'green')

# Generate a cloud with terms common to both

common_terms = list(setPS & setXB)
commonPSXB = [word for word in corpusXB if word in common_terms]
generate_cloud(commonPSXB, 'Common.png')
