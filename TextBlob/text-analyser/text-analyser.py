from textblob import TextBlob
from langdetect import detect
import nltk

# Ensure necessary data is downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Sample text
text = """.bhcdjk ajcsb acjbsn bgcsa bsakhcnschkcss hvsa chsahk csa"""

# Create a TextBlob object
blob = TextBlob(text)

# Sentiment Analysis
sentiment = blob.sentiment
print(f"Sentiment Analysis:\n Polarity: {sentiment.polarity}, Subjectivity: {sentiment.subjectivity}\n")

# Tokenization
words = blob.words
sentences = blob.sentences
print("Tokenization:")
print(f"Words: {words}")
print(f"Sentences: {sentences}\n")

# Part-of-Speech Tagging
print("Part-of-Speech Tagging:")
for word, pos in blob.tags:
    print(f"{word}: {pos}")
print()

# Noun Phrase Extraction
noun_phrases = blob.noun_phrases
print("Noun Phrases:")
for np in noun_phrases:
    print(np)
print()

# Translation and Language Detection
try:
    translated_blob = blob.translate(to='es')  # Translating to Spanish
    print(f"Translation to Spanish:\n{translated_blob}\n")
except Exception as e:
    print(f"Translation Error: {e}")

# Language Detection using langdetect
try:
    detected_language = detect(text)
    print(f"Detected Language: {detected_language}\n")
except Exception as e:
    print(f"Language Detection Error: {e}")
