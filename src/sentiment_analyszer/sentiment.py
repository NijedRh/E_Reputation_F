from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
class SentimentAnalyzer :
    def __init__(self, sample):
        self.sample = sample
    def analyse ( self):
        analyzer = SentimentIntensityAnalyzer()
        sentence = self.sample
        vs = analyzer.polarity_scores(sentence)
        return str(vs)