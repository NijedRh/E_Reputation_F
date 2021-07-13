from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import json
class SentimentAnalyzer :
    def __init__(self, sample):
        self.sample = sample

    def analyse ( self):
        analyzer = SentimentIntensityAnalyzer()
        sentence = self.sample
        vs = analyzer.polarity_scores(sentence)
        a="Overall sentiment dictionary is : ", vs
        b="comment was rated as ", vs['neg'] * 100, "% Negative"
        c="comment was rated as ", vs['neu'] * 100, "% Neutral"
        d="comment was rated as ", vs['pos'] * 100, "% Positive "

        if vs["compound"] >= 0.1:
            e = "positive comment"
            p="po"
            return e ,p ,float(vs.get("compound"))
        elif vs["compound"] <= -0.1:
            e = "negative comment"
            p="neg"
            h = [a, b, c, d, e]

            return e ,p ,float(vs.get("compound"))
        else:
            e = "neutral comment"
            p="neu"
            h = [a, b, c, d, e]

            return e,p ,float(vs.get("compound"))


