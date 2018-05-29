import mysql.connector
import datetime
import app
import optimization

dateSubmitted = ''

class connection():
    global dateSubmitted
    def createData(seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost,
                   internQACost, seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver, seniorQADeliver,
                   techQADeliver, juniorQADeliver, internQADeliver, x1, x2, x3, x4, x5, x6, x7, x8, projectPoints,
                   sprintPoints):
        cnx = mysql.connector.connect(  # user='scott', password='password',
            user='root',
            password='',
            host='127.0.0.1',
            database='operaciones')
        cursor = cnx.cursor()
        add_model = ("INSERT INTO History"
                     "(seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost, internQACost, seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver, seniorQADeliver, techQADeliver, juniorQADeliver, internQADeliver, x1, x2, x3, x4, x5, x6, x7, x8, projectPoints,sprintPoints, date)"
                     " VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s)")
        data_model = (
            seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost,
            internQACost,
            seniorDevDeliver, techDevDeliver, juniorDevDeliver, internDevDeliver, seniorQADeliver,
            techQADeliver, juniorQADeliver, internQADeliver, x1, x2, x3, x4, x5, x6, x7, x8, projectPoints,
            sprintPoints, datetime.datetime.now())
        cursor.execute(add_model, data_model)
        cnx.commit()
        cursor.close()
        cnx.close()

    def queryData(id):
        cnx = mysql.connector.connect(  # user='scott', password='password',
            user='root',
            password='',
            host='127.0.0.1',
            database='operaciones')
        cursor = cnx.cursor()
        query = ("SELECT * FROM History "
                 "WHERE id = " + str(id))

        cursor.execute(query)

        for (id, seniorDevCost, techDevCost, juniorDevCost, internDevCost, seniorQACost, techQACost, juniorQACost,
             internQACost,
             seniorDevDeliver, techDevDeliver, juniorDevDeliver,
             internDevDeliver, seniorQADeliver, techQADeliver, juniorQADeliver, internQADeliver,
             x1, x2, x3, x4, x5, x6, x7, x8,projectPoints,sprintPoints,
              date) in cursor:
            id = id
            app.seniorDevCost = seniorDevCost
            app.techDevCost = techDevCost
            app.juniorDevCost = juniorDevCost
            app.internDevCost = internDevCost
            app.seniorQACost = seniorQACost
            app.techQACost = techQACost
            app.juniorQACost = juniorQACost
            app.internQACost = internQACost
            app.seniorDevDeliver = seniorDevDeliver
            app.techDevDeliver = techDevDeliver
            app.juniorDevDeliver = juniorDevDeliver
            app.internDevDeliver = internDevDeliver
            app.seniorQADeliver = seniorQADeliver
            app.techQADeliver = techQADeliver
            app.juniorQADeliver = juniorQADeliver
            app.internQADeliver = internQADeliver
            app.sprintPoints = sprintPoints
            app.projectPoints = projectPoints
            # app.projectBudget = projectBudget
            optimization.x1 = x1
            optimization.x2 = x2
            optimization.x3 = x3
            optimization.x4 = x4
            optimization.x5 = x5
            optimization.x6 = x6
            optimization.x7 = x7
            optimization.x8 = x8
            dateSubmitted = date
            
        cursor.close()
        cnx.close()

    def queryFullData():
        list = []
        info = []
        cnx = mysql.connector.connect(  # user='scott', password='password',
            user='root',
            password='',
            host='127.0.0.1',
            database='operaciones')
        cursor = cnx.cursor()
        query = ("SELECT id,date FROM History ")

        cursor.execute(query)

        for (id, date) in cursor:
            info = [id, date]
            list.insert(0, info)

        cursor.close()
        cnx.close()
        return list
