import mysql.connector


class Db :
    def __init__(self , post_num ,titre,reactions_aime, reactions_adore,reactions_haha,reactions_grrr,commentaires):
        self.post_num=post_num
        self.titre=titre
        self.reactions_aime=reactions_aime
        self.reactions_adore=reactions_adore
        self.reactions_haha=reactions_haha
        self.reactions_grrr=reactions_grrr
        self.commentaires=commentaires

    def connect (self):
        conn = mysql.connector.connect(user='root', database='e_reputation')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS datas (post_num INT, titre TEXT, aime INT ,adore INT ,Haha INT ,Grrr INT,commentaires TEXT )''')
        #c.execute('''CREATE TABLE IF NOT EXISTS commentaires (post_num INT ,  )''')
        c.execute('''INSERT INTO datas VALUES(%s,%s,%s,%s,%s,%s,%s)''', ( str(self.post_num),str(self.titre), int(self.reactions_aime),int(self.reactions_adore),int(self.reactions_haha),int(self.reactions_grrr),str(self.commentaires)))
        conn.commit()
        conn.close()
class DB2 :
    def __init__(self , number_comm):
        self.number_comm=number_comm
    def connect2(self):
        conn = mysql.connector.connect(user='root', database='e_reputation')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS NUMBER_COMM ( num_comm INT ) ''')
        c.execute('''INSERT INTO NUMBER_COMM VALUES (%s)''', (int(self.number_comm),))
        conn.commit()
        conn.close()
