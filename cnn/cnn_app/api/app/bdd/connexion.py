import mysql.connector as mysqlpyth

from app.config import DB_USER, DB_PASSWORD, DB_HOST, DB_PORT, DB_NAME

class Connexion :

    @classmethod
    def ouvrir_connexion(cls):
        cls.bdd = mysqlpyth.connect(user=DB_USER, password=DB_PASSWORD, host=DB_HOST, port=DB_PORT, database=DB_NAME)
        cls.cursor = cls.bdd.cursor(dictionary=True)
    
    @classmethod
    def fermer_connexion(cls):
        if hasattr(cls, "cursor") and cls.cursor:
            cls.cursor.close()
        if hasattr(cls, "bdd") and cls.bdd:
            cls.bdd.close()