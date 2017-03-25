# bag of words is count vectorizer in sklearn
# in Python interpreter

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer()
string1 = "hi Katie the self driving car will be late best Sebastion"
string2 = "Hi Sebastian the machine learning class will be great great great Best Katie"
string3 = "Hi Katie the machine learning class will be most excellent"
email_list = [string1, string2, string3]

bag_of_words = vectorizer.fit(email_list)
bag_of_words = vectorizer.transform(email_list)
print bag_of_words

# (1, 6) 3
# in doc 1, (string2) word 6 occurs 3 times

# to find the index of a specific word I am interested in --> 6
print vectorizer.vocabulary_.get("great")



# to get rid of stop words
# import a list of stopwords
from nltk.corpus import stopwords
sw = stopwords.words("english")

# find the most common stopwords
sw[0]
# "I"

sw[1]
# "me"

print len(sw)
# 153 or 127


from nltk.stem.snowball import SnowballStemmer
stemmer = SnowballStemmer("english")
stemmer.stem("responsiveness")

# u'respons'

stemmer.stem("unresponsive")
# u'unrespons'



# Sklearn stop words list
CountVectorizer(stop_words='english')


from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(stop_words="english", lowercase=True)

