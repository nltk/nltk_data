"""Train a three-class SVM sentiment classifier on NLTK tweet data."""

import argparse

import nltk
from nltk.corpus import twitter_samples
from nltk.sentiment import SentimentIntensityAnalyzer
from sklearn import metrics
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--text", default="I love this!", help="text to classify")
    args = parser.parse_args()

    # Load labeled positive and negative tweets plus an unlabeled tweet sample.
    try:
        positive = twitter_samples.strings("positive_tweets.json")
        negative = twitter_samples.strings("negative_tweets.json")
        tweets = twitter_samples.strings("tweets.20150430-223406.json")
    except LookupError:
        nltk.download("twitter_samples", quiet=True)
        positive = twitter_samples.strings("positive_tweets.json")
        negative = twitter_samples.strings("negative_tweets.json")
        tweets = twitter_samples.strings("tweets.20150430-223406.json")

    # Use VADER to find neutral examples in the unlabeled sample.
    try:
        vader = SentimentIntensityAnalyzer()
    except LookupError:
        nltk.download("vader_lexicon", quiet=True)
        vader = SentimentIntensityAnalyzer()
    neutral = [
        tweet for tweet in tweets
        if abs(vader.polarity_scores(tweet)["compound"]) < 0.05
    ]
    # Balance the three classes and create the training and test sets.
    size = min(len(positive), len(negative), len(neutral))
    texts = positive[:size] + negative[:size] + neutral[:size]
    labels = ["positive"] * size + ["negative"] * size + ["neutral"] * size

    # Split the data into training and test sets.
    X_train, X_test, y_train, y_test = train_test_split(
        texts, labels, test_size=0.2, random_state=42, stratify=labels
    )

    # Turn text into TF-IDF features, then classify it with a linear SVM.
    text_clf = make_pipeline(TfidfVectorizer(), SVC(kernel="linear"))
    text_clf.fit(X_train, y_train)

    predicted = text_clf.predict(X_test)
    print(metrics.classification_report(y_test, predicted))
    print(f"Sentiment for {args.text!r}: {text_clf.predict([args.text])[0]}")


if __name__ == "__main__":
    main()
