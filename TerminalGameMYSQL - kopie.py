import mysql.connector
from mysql.connector import errorcode

try:
  cnx = mysql.connector.connect(user='pi', 
                                password='test123',
                                host='127.0.0.1',
                                db='hackgame')
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with your user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    query = ("SELECT uid, players, hint, language FROM hack " "")
    print(query)
	#hire_start = datetime.date(1999, 1, 1)
	#hire_end = datetime.date(1999, 12, 31)

    cursor.execute(query)
	#cursor.execute(query, params=None, multi=False)

    for (uid, players, hint) in cursor:
        print("".format(uid, players, hint))

	#cursor.close()
	#cnx.close()

#else:
#	query = ("SELECT first_name, last_name, hire_date FROM employees "
#         "WHERE hire_date BETWEEN %s AND %s")

#	hire_start = datetime.date(1999, 1, 1)
#	hire_end = datetime.date(1999, 12, 31)

#	cursor.execute(query, (hire_start, hire_end))

#	for (first_name, last_name, hire_date) in cursor:
#	  print("{}, {} was hired on {:%d %b %Y}".format(
#		last_name, first_name, hire_date))

#	cursor.close()
#	cnx.close()