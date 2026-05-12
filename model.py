from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB

texts = [
    "Win money now",
    "Claim your prize",
    "Cheap loans available",
    "Free recharge offer",
    "Meeting at 5pm",
    "Project deadline tomorrow",
    "Team lunch today",
    "Assignment submission today"
]

labels = [
    "Spam",
    "Spam",
    "Spam",
    "Spam",
    "Important",
    "Important",
    "Normal",
    "Important"
]

vectorizer = CountVectorizer()
X = vectorizer.fit_transform(texts)

model = MultinomialNB()
model.fit(X, labels)

def predict_message(msg):
    vec = vectorizer.transform([msg])
    pred = model.predict(vec)[0]
    prob = max(model.predict_proba(vec)[0])
    return pred, round(prob * 100, 2)