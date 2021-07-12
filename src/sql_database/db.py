import mysql.connector


class Db :
    def __init__(self , post_num ,titre,reactions_aime, reactions_adore,reactions_haha,reactions_grrr,commentaires,nbr_pos,nbr_neg,nbr_neu):
        self.post_num=post_num
        self.titre=titre
        self.reactions_aime=reactions_aime
        self.reactions_adore=reactions_adore
        self.reactions_haha=reactions_haha
        self.reactions_grrr=reactions_grrr
        self.commentaires=commentaires
        self.nbr_pos=nbr_pos
        self.nbr_neg=nbr_neg
        self.nbr_neu=nbr_neu

    def connect (self):
        conn = mysql.connector.connect(user='root', database='e_reputation')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS datas (post_num INT,
                                                       titre TEXT,
                                                       aime INT ,
                                                       adore INT ,
                                                       Haha INT ,
                                                       Grrr INT,
                                                       commentaires TEXT,
                                                       nbr_com_pos INT,
                                                       nbr_com_neg INT,
                                                       nbr_comm_neu INT )''')

        c.execute('''INSERT INTO datas(post_num,titre,aime,adore,Haha,Grrr,commentaires,nbr_com_pos,nbr_com_neg,nbr_comm_neu) 
                     VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)''',
                    ( int(self.post_num),str(self.titre), int(self.reactions_aime),int(self.reactions_adore),int(self.reactions_haha),int(self.reactions_grrr),str(self.commentaires),self.nbr_pos,self.nbr_neg,self.nbr_neu))
        conn.commit()
        conn.close()
class DB2 :
    def __init__(self , number_comm ,a_sum, b_sum, c_sum):
        self.number_comm=number_comm
        self.a_sum=a_sum
        self.b_sum=b_sum
        self.c_sum=c_sum
    def connect2(self):
        conn = mysql.connector.connect(user='root', database='e_reputation')
        c = conn.cursor()
        try:
            c.execute('''ALTER TABLE datas ADD  NUMBER_COMM INT ;''')
        except:
            pass
        try:
            c.execute('''ALTER TABLE datas ADD  NUM_COMM_PO INT ;''')
        except:
            pass
        try:
            c.execute('''ALTER TABLE datas ADD  NUM_COMM_NEG INT ;''')
        except:
            pass
        try:
            c.execute('''ALTER TABLE datas ADD  NUM_COMM_NEU INT  ; ''')
        except:
            pass
        c.execute('''INSERT INTO datas(NUMBER_COMM,NUM_COMM_PO,NUM_COMM_NEG,NUM_COMM_NEU)
                     VALUES (%s,%s,%s,%s)''',
                     (int(self.number_comm),int(self.a_sum),int(self.b_sum),int(self.c_sum)))
        conn.commit()
        print("everything is updated")
        conn.close()
