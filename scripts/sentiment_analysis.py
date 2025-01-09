import pandas as pd
import numpy as np
from langdetect import detect
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, classification_report
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
data = pd.read_csv("data/comments.csv")
data['language'] = data['comment'].apply(detect)

# Preprocessing
stop_words = stopwords.words("english")
data['cleaned_comment'] = data['comment'].apply(
    lambda x: ' '.join(word for word in x.split() if word not in stop_words)
)

# TF-IDF vectorization
vectorizer = TfidfVectorizer(max_features=5000)
X = vectorizer.fit_transform(data['cleaned_comment']).toarray()
y = data['sentiment']

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a model
model = LogisticRegression()
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print("Model Accuracy:", accuracy)

# Classification report
print(classification_report(y_test, y_pred))

# Visualization
sns.countplot(x="sentiment", data=data)
plt.title("Sentiment Distribution")
plt.show()
