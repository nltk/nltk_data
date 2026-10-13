"""Unit tests for the sentiment analysis example."""

import contextlib
import io
import sys
import unittest
from types import SimpleNamespace
from unittest.mock import patch

from examples import sentiment_analysis


class FakeSentimentIntensityAnalyzer:
    def polarity_scores(self, text):
        return {"compound": 0.0 if text.startswith("neutral") else 0.8}


class SentimentAnalysisTests(unittest.TestCase):
    def test_main_trains_classifier_and_reports_all_sentiment_classes(self):
        positive = [f"great excellent lovely {i}" for i in range(5)]
        negative = [f"awful terrible dreadful {i}" for i in range(5)]
        neutral = [f"neutral package delivery {i}" for i in range(5)]
        corpus = SimpleNamespace(
            strings=lambda name: {
                "positive_tweets.json": positive,
                "negative_tweets.json": negative,
                "tweets.20150430-223406.json": neutral,
            }[name]
        )
        output = io.StringIO()

        with (
            patch.object(sentiment_analysis, "twitter_samples", corpus),
            patch.object(
                sentiment_analysis,
                "SentimentIntensityAnalyzer",
                FakeSentimentIntensityAnalyzer,
            ),
            patch.object(sentiment_analysis.nltk, "download"),
            patch.object(sys, "argv", ["sentiment_analysis.py", "--text", "great"]),
            contextlib.redirect_stdout(output),
        ):
            sentiment_analysis.main()

        result = output.getvalue()
        self.assertIn("positive", result)
        self.assertIn("negative", result)
        self.assertIn("neutral", result)
        self.assertIn("Sentiment for 'great':", result)


if __name__ == "__main__":
    unittest.main()
