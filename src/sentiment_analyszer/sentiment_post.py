

class SentimentPost :
    def __init__(self , t  ):
        self.t =t

    def analyse_post(self):
        """initialise compound number to  0
            if like number > 1 grr number ==> compound +0.1
            if like number > 2 grrr number ==> compound + 0.2
            if  like number > 3 grr number ==> compound + 0.3
            if HAha number and grrr number > like number ==> compound - 0.2
            if HAha number and like number > grr number ==> compound +0.1
            make a sum of coumpound number for each comment * 0.7
            +
            sum of compound number for the reaction *0.3
            if  overall compound number > 0.1 then post sent is positive
            elif overall compound number < 0.1 then post sent ins negative
            else post sent in neutre
            """


        score = 0
        try:
            if 1* self.t['Grrr'] < self.t['J’aime '] < 2*self.t['Grrr']:
                score +=0.1

            elif 2* self.t['Grrr'] <= self.t['J’aime '] < 3*self.t['Grrr']:
                score +=0.2
            elif 3* self.t['Grrr'] <= self.t['J’aime '] :
                score +=0.3
        except :
            pass
        try:
            if (self.t['Haha'] and self.t['Grrr'])>self.t['J’aime']:
                score -= 0.2
            elif(self.t['Haha']and self.t['J’aime'])>self.t['Grrr']:
                score +=0.1
        except:
            pass
        return "le score est " + str(score)









