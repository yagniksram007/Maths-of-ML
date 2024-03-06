#pip install nltk

import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline

# Sample dataset
messages = [
    {'text': 'This is a legitimate message', 'label': 'ham'},
    {'text': 'Congratulations! You won a prize.', 'label': 'spam'},
    # Add more messages with corresponding labels
]

# Split the dataset into features (X) and labels (y)
X = [message['text'] for message in messages]
y = [message['label'] for message in messages]

# Create a model using Naive Bayes classifier
model = make_pipeline(CountVectorizer(), MultinomialNB())
model.fit(X, y)

# Test the model with a new message
new_message = 'Claim your free gift now!'
predicted_label = model.predict([new_message])[0]

print(f'The document is classified as: {predicted_label}')
