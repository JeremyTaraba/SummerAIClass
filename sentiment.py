from sklearn import svm
from sklearn.feature_extraction.text import TfidfVectorizer

input_data = [ ]
sentences = [
            "There was a decent amount of meat though and the noodles were great.", 
             "The food is slightly worse than the other two locations.", 
             "The beef noodle soup taste so bad and the male waiter(with glasses) even took a sip on it to prove that it's ok.", 
             "My son says good food."
             ]

vectorizer = TfidfVectorizer()
input_data = vectorizer.fit_transform(sentences)

output_data = [1, 0, 0, 1] # 1 is good, 0 is bad

model = svm.SVC()
model.fit(input_data, output_data)

test_sentences = [
 "The food I ate is worse than the old store.",
 "My dad said good food."
]


print(model.predict(vectorizer.transform(test_sentences)))

from textblob import TextBlob

text = TextBlob("The food I ate is worse than the old store.")

polarity = text.sentiment.polarity

print(polarity)