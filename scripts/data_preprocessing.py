import pandas as pd
import re
from langdetect import detect
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer

# Load the dataset
data = pd.read_csv('../data/comments.csv')

# Initialize tools
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

# Define text cleaning function
def clean_text(text):
    # Remove URLs
    text = re.sub(r"http\S+|www\S+|https\S+", '', text, flags=re.MULTILINE)
    # Remove special characters and numbers
    text = re.sub(r'\W', ' ', text)
    text = re.sub(r'\d', '', text)
    # Convert to lowercase
    text = text.lower()
    # Tokenize and remove stopwords
    tokens = word_tokenize(text)
    filtered_tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(filtered_tokens)

# Detect language and clean text
def preprocess_data(data):
    processed_comments = []
    for comment in data['comment']:
        try:
            if detect(comment) == 'en':  # Only process English comments
                processed_comments.append(clean_text(comment))
            else:
                processed_comments.append(None)  # Mark non-English comments as None
        except:
            processed_comments.append(None)  # Handle detection errors
    data['cleaned_comment'] = processed_comments
    return data.dropna()

# Preprocess the dataset
processed_data = preprocess_data(data)
processed_data.to_csv('../data/processed_comments.csv', index=False)
print("Data preprocessing complete. Saved to processed_comments.csv.")
