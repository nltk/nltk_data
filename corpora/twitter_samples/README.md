# Twitter Samples


These samples of Tweets (or 'status updates') were collected from the Twitter Streaming APIs (see [API Documentation](https://dev.twitter.com/overview/documentation), [Streaming Overview](https://dev.twitter.com/streaming/overview)). Each file consists of line-separated JSON-formatted tweets, i.e. one Tweet per line. For a detailed description of the JSON fields in a Tweet, see [Tweets: Field Guide](https://dev.twitter.com/overview/api/tweets).

Any use of this data is subject to the [Twitter Developer Agreement and
Developer Policy](https://dev.twitter.com/overview/terms/agreement-and-policy).


## tweets.20150430-223406.json


Collected from the public stream of the Streaming API using the `statuses / filter` endpoint. The value of `track` was set to the following keywords:

	"david cameron, miliband, milliband, sturgeon, clegg, farage, tory, tories, ukip, snp, libdem"

## Sentiment analysis example

The repository includes [`examples/sentiment_analysis.py`](../../examples/sentiment_analysis.py), which trains a Support Vector Machine (SVM) to classify text as positive, negative, or neutral. It uses `positive_tweets.json` and `negative_tweets.json` as labeled examples. Since the general tweet sample does not include sentiment labels, the example uses NLTK's VADER lexicon to select neutral tweets. These neutral labels are approximate.

From the repository root, install the Python dependencies and run the example:

```bash
python -m pip install nltk scikit-learn
python examples/sentiment_analysis.py --text "This is the greatest place ever!"
```

The script prints a classification report for its test split, then predicts the sentiment of the text passed with `--text`. Treat the test score as an estimate, especially for neutral sentiment, because those examples are labeled automatically with VADER.
