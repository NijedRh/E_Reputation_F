

class SentimentPost :

    def analyse_post(self ,t):
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
            i[0] = j'aime , i[1]=j'adore , i[2]= haha , i[3]=grrr

            """
        score=0
        for i in t:
            if 1* i[3] < i[0] < 2*i[3]:
                score +=0.1
            elif 2* i[3] <= i[0] < 3*i[3]:
                score +=0.2
            elif 3* i[3] <= i[0] :
                score +=0.3

            if (i[2] and i[3])>i[0]:
                score -= 0.2
            elif(i[2]and i[0])>i[3]:
                score +=0.1

        return float(score)*0.3











