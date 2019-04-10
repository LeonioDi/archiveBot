import sqlite3


def connect(func):
    def connectTo(*args, **kwargs):
        try:
            con = sqlite3.connect("db_archive")
            cur = con.cursor()
        except Exception as e:
            print(e)
        return func(con, cur, *args, **kwargs)

    return connectTo


""" Метод обавления нового пользователя """


@connect
def addUser(con, cur, idUser, name):
    cur.execute("INSERT INTO USER(idUser, name) VALUES ({},'{}')".format(idUser, name))
    con.commit()


""" Метод Проверки пользователя на верификацию """


@connect
def chekUser(con, cur, idUser):
    cur.execute("SELECT verification FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
    except Exception as e:
        print(e)
        res = None
    if res is not None:
        if res[0] == 'TRUE':
            return True
        else:
            return 'Not verificated'
    else:
        return None


"""Методы для работы мастаера добавления статьи """


@connect
def getCurrentState(con, cur, idUser):
    cur.execute("SELECT currentState FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
        return res[-1]
    except Exception as e:
        print(e)
        return None


@connect
def setCurrentState(con, cur, idUser, value):
    cur.execute("UPDATE USER SET currentState = {} WHERE idUser = {}".format(value, idUser))
    con.commit()


""" методы для определения и работы с активной статьей"""


@connect
def getCurrentidArticle(con, cur, idUser):
    cur.execute("SELECT currentidArticle FROM USER WHERE idUser = {}".format(idUser))
    con.commit()
    try:
        res = cur.fetchall()[0]
        return res[-1]
    except Exception as e:
        print(e)
        return None


@connect
def setCurrentidArticle(con, cur, idUser, idArticle):
    cur.execute("UPDATE USER SET currentidArticle = '{}' WHERE idUser = {}".format(idArticle, idUser))
    con.commit()


"""Добавление новой статьи"""


@connect
def addArticle(con, cur, idArticle, idUser):
    cur.execute("INSERT INTO ARTICLE(idArticle, idUser) VALUES ('{}','{}')".format(idArticle, idUser))
    con.commit()


"""Обновление данных статьи по ключу"""


@connect
def updateArticle(con, cur, idArticle, key, value):
    cur.execute("UPDATE ARTICLE SET {} = '{}' WHERE idArticle = '{}'".format(key, value, idArticle))
    con.commit()


"""Получение всех данных по статье"""


@connect
def getAllArticle(con, cur, idArticle):
    cur.execute("SELECT * FROM ARTICLE WHERE idArticle = '{}'".format(idArticle))
    con.commit()
    try:
        res = cur.fetchall()[0]
        return res
    except Exception as e:
        print(e)
        return None
