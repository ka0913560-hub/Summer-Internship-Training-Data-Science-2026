# 📅 Data Science Internship - Day 19
## Topic: Natural Language Processing (NLP), Sentiment Analysis, Naive Bayes, RNN, LSTM & CNN

**Date:** 23 July 2026

---

# 📖 Today's Learning

Today's class focused on **Natural Language Processing (NLP)**, **Deep Learning**, and **Computer Vision**. We learned how machines understand human language, classify text, analyze sentiments, and process images using Deep Learning models.

---

# 1️⃣ Natural Language Processing (NLP)

## What is NLP?

Natural Language Processing (NLP) is a branch of Artificial Intelligence (AI) that enables computers to understand, analyze, process, and generate human language.

### Applications of NLP

- Chatbots
- Voice Assistants
- Google Translate
- Sentiment Analysis
- Spam Detection
- Email Filtering
- Text Classification
- Recommendation Systems
- Question Answering Systems
- Text Summarization
- Machine Translation

---

# 2️⃣ NLP Pipeline

The complete NLP workflow consists of the following steps:

1. Collect Text Data
2. Text Cleaning
3. Text Preprocessing
4. Tokenization
5. Remove Stopwords
6. Stemming
7. Lemmatization
8. Feature Extraction
9. Model Training
10. Prediction

---

# 3️⃣ Text Preprocessing

Text preprocessing is performed before training any NLP model.

Topics covered:

- Convert text to lowercase
- Remove HTML Tags
- Remove URLs
- Remove Punctuation
- Remove Special Characters
- Remove Numbers
- Remove Extra Spaces
- Remove Emojis (optional)

Example:

Original:
```
I LOVE Python!!! 😍
```

Processed:
```
love python
```

---

# 4️⃣ Tokenization

Tokenization means breaking text into smaller parts called tokens.

Example:

Sentence:
```
I love Machine Learning
```

Tokens:

```
I
love
Machine
Learning
```

---

# 5️⃣ Stopwords Removal

Stopwords are commonly used words that usually do not contribute much meaning.

Examples:

- is
- am
- are
- the
- of
- a
- an
- and

---

# 6️⃣ Stemming

Stemming reduces words to their root form.

Examples:

Playing → Play

Played → Play

Playing → Play

Studies → Studi

Running → Run

Library Used:

```
PorterStemmer
```

---

# 7️⃣ Lemmatization

Lemmatization converts words into meaningful dictionary words.

Example

Better → Good

Running → Run

Studies → Study

Library Used:

```
WordNetLemmatizer
```

Difference:

Stemming is faster but less accurate.

Lemmatization is slower but more accurate.

---

# 8️⃣ Part of Speech (POS) Tagging

POS Tagging identifies the grammatical role of every word.

Example:

Noun

Verb

Adjective

Pronoun

Adverb

---

# 9️⃣ Named Entity Recognition (NER)

NER identifies real-world entities.

Examples:

Person

Organization

Location

Date

Money

---

# 🔟 Bag of Words (BoW)

Bag of Words converts text into numerical vectors based on word frequency.

Steps:

- Create vocabulary
- Count frequency
- Convert into matrix

---

# 1️⃣1️⃣ CountVectorizer

CountVectorizer automatically converts text into Bag of Words vectors.

Used for:

- Spam Detection
- Text Classification
- Sentiment Analysis

---

# 1️⃣2️⃣ TF-IDF

TF-IDF gives higher importance to important words and lower importance to common words.

Advantages:

- Better than Bag of Words
- Removes importance of common words
- Improves accuracy

---

# 1️⃣3️⃣ Word Embeddings

Introduction to word representation.

Mentioned concepts:

- Word2Vec
- Embedding Layer

---

# 1️⃣4️⃣ Sentiment Analysis

Sentiment Analysis predicts whether text is:

Positive

Negative

Neutral

Workflow:

Dataset

↓

Cleaning

↓

Tokenization

↓

Stopword Removal

↓

Stemming

↓

TF-IDF

↓

Train/Test Split

↓

Machine Learning Model

↓

Prediction

---

# Models Used

- Logistic Regression
- Decision Tree
- Naive Bayes

Evaluation:

- Accuracy
- Classification Report
- Prediction

---

# 1️⃣5️⃣ Naive Bayes Algorithm

Naive Bayes is a probabilistic machine learning algorithm mainly used for text classification.

Applications:

- Spam Detection
- Email Filtering
- Sentiment Analysis
- News Classification

Steps:

- Dataset
- CountVectorizer
- Train Test Split
- Train Naive Bayes
- Predict
- Evaluate Accuracy

---

# 1️⃣6️⃣ Recurrent Neural Network (RNN)

RNN is a Deep Learning model used for sequential data.

Applications:

- NLP
- Speech Recognition
- Language Translation
- Text Generation

---

# 1️⃣7️⃣ Long Short-Term Memory (LSTM)

LSTM is an improved version of RNN.

Advantages:

- Remembers long-term dependencies
- Solves Vanishing Gradient Problem
- Better accuracy than RNN

Layers discussed:

Embedding Layer

↓

LSTM Layer

↓

Dropout Layer

↓

Dense Layer

Workflow:

Tokenizer

↓

Sequence Encoding

↓

Padding

↓

Model Building

↓

Training

↓

Prediction

---

# 1️⃣8️⃣ Convolutional Neural Network (CNN)

CNN is mainly used for image processing.

Applications:

- Image Classification
- Face Recognition
- Object Detection
- Medical Imaging

CNN Architecture:

Input Image

↓

Convolution Layer

↓

ReLU

↓

Pooling Layer

↓

Flatten

↓

Dense Layer

↓

Output

---

# CNN Layers

## Conv2D

Extracts image features.

## MaxPooling2D

Reduces image dimensions.

## Flatten

Converts feature maps into a 1D vector.

## Dense Layer

Performs classification.

## Dropout

Reduces overfitting.

---

# Libraries Used

- Python
- NumPy
- Pandas
- Matplotlib
- TensorFlow
- Keras
- NLTK
- Scikit-Learn
- OpenCV (cv2)

---

# Machine Learning Models Covered

- Logistic Regression
- Decision Tree
- Multinomial Naive Bayes

---

# Deep Learning Models Covered

- CNN
- RNN
- LSTM

---

# Important Concepts Learned

- NLP
- NLP Pipeline
- Text Cleaning
- Tokenization
- Stopwords
- Stemming
- Lemmatization
- POS Tagging
- NER
- Bag of Words
- CountVectorizer
- TF-IDF
- Sentiment Analysis
- Text Classification
- Naive Bayes
- Logistic Regression
- Decision Tree
- RNN
- LSTM
- CNN
- Conv2D
- MaxPooling2D
- Flatten
- Dense Layer
- Dropout
- Embedding Layer

---

# Conclusion

Today's session covered the fundamentals of **Natural Language Processing**, **Text Classification**, **Sentiment Analysis**, **Naive Bayes**, **Recurrent Neural Networks (RNN)**, **Long Short-Term Memory (LSTM)**, and **Convolutional Neural Networks (CNN)**. We explored the complete NLP workflow from preprocessing text to training machine learning models, along with deep learning architectures for handling sequential text data and image classification tasks. These concepts form the foundation for advanced AI, Machine Learning, Deep Learning, and Generative AI applications.
