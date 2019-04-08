import sqlite3

""" Добавление нового пользователя """


def addUser(idUser, name):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("INSERT INTO USER(idUser, name) VALUES ({},'{}')".format(idUser, name))
    con.commit()
    cur.close()
    con.close()


""" Метод Проверки пользователя на верификацию """


def chekUser(idUser):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("SELECT verification FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
    except Exception as e:
        print(e)
        res = None
    cur.close()
    con.close()
    if res is not None:
        if res[0] == 'TRUE':
            return True
        else:
            return 'Not verificated'
    else:
        return None


"""Методы для работы мастаера добавления статьи """


def getCurrentState(idUser):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("SELECT currentState FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
    except Exception as e:
        print(e)
        res = None
    cur.close()
    con.close()
    return res[-1]


def setCurrentState(idUser, value):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("UPDATE USER SET currentState = {} WHERE idUser = {}".format(value, idUser))
    con.commit()
    cur.close()
    con.close()


""" методы для определения и работы с активной статьей"""


def getCurrentidArticle(idUser):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("SELECT currentidArticle FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
    except Exception as e:
        print(e)
        res = None
    cur.close()
    con.close()
    return res[-1]


def setCurrentidArticle(idUser, idArticle):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("UPDATE USER SET currentidArticle = '{}' WHERE idUser = {}".format(idArticle, idUser))
    con.commit()
    cur.close()
    con.close()


"""Добавление новой статьи"""


def addArticle(idArticle, idUser):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("INSERT INTO ARTICLE(idArticle, idUser) VALUES ('{}','{}')".format(idArticle, idUser))
    con.commit()
    cur.close()
    con.close()


"""Обновление данных статьи по ключу"""


def updateArticle(idArticle, key, value):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("UPDATE ARTICLE SET {} = '{}' WHERE idArticle = '{}'".format(key, value, idArticle))
    con.commit()
    cur.close()
    con.close()


"""Получение всех данных по статье"""


def getAllArticle(idArticle):
    con = sqlite3.connect("db_archive")
    cur = con.cursor()
    cur.execute("SELECT * FROM ARTICLE WHERE idArticle = '{}'".format(idArticle))
    con.commit()
    try:
        res = cur.fetchall()[0]
    except Exception as e:
        print(e)
        res = None
    cur.close()
    con.close()
    return res
