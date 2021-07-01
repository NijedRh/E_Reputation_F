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
            h=a,b,c,d,e
            print(h)
            return e#json.dumps(h, ensure_ascii=False,separators=(',', ':') )
        elif vs["compound"] <= -0.1:
            e = "negative comment"

            h = [a, b, c, d, e]
            print(h)
            return e #json.dumps(h, ensure_ascii=False,separators=(',', ':'))
        else:
            e = "neutral comment"

            h = [a, b, c, d, e]
            print(h)
            return e #json.dumps(h,ensure_ascii=False, separators=(',', ':'))
    """def nbr_pos_neg_neu (self ):

            analyzer = SentimentIntensityAnalyzer()
            sentence = self.sample
            vs = analyzer.polarity_scores(sentence)

            i=0
            j=0
            k=0
            if vs["compound"] >= 0.1:
                i=i+1
            elif vs["compound"] <= -0.1:
                j=j+1
            else :
                k=k+1
            return  i ,j , k"""

