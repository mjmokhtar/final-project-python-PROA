import mysql.connector
from mysql.connector import connection, errorcode, Error

import pandas as pd

import matplotlib.pyplot as plt

# Menghubungkan ke database
mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="mysql2024",
  database="iot"
)

#connecting to MySQL db server
try:
    conn = mydb
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Access denied")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("No such db")
    else:
        print(err)
else:
    print (mydb)
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM rtos_mj")
    myresult = mycursor.fetchall()

#for x in myresult:
#   print(x)
# 2. Membaca data dari tabel MySQL ke DataFrame Pandas

df = pd.DataFrame(myresult)
df.columns=['id','datetime','temp','hum','x','condition']
print(df)
#plt.plot(df['datetime'],df['temp'],df['hum'],df['x'])

fig, ax = plt.subplots()
fig.subplots_adjust(right=0.75)

twin1 = ax.twinx()
twin2 = ax.twinx()

# Offset the right spine of twin2.  The ticks and label have already been
# placed on the right by twinx above.
twin2.spines.right.set_position(("axes", 1.2))

p1, = ax.plot(df['temp'], "C0", label="Temperature")
p2, = twin1.plot(df['hum'], "C1", label="Humidity")
p3, = twin2.plot(df['x'], "C2", label="Cross")

ax.set(xlim=(0, 1000), ylim=(0, 100), xlabel="Date", ylabel="Temperature")
twin1.set(ylim=(0, 50), ylabel="Humidity")
twin2.set(ylim=(1, 2000), ylabel="Cross")

ax.yaxis.label.set_color(p1.get_color())
twin1.yaxis.label.set_color(p2.get_color())
twin2.yaxis.label.set_color(p3.get_color())

ax.tick_params(axis='y', colors=p1.get_color())
twin1.tick_params(axis='y', colors=p2.get_color())
twin2.tick_params(axis='y', colors=p3.get_color())

ax.legend(handles=[p1, p2, p3])
plt.title("Data Sensor Harian")
plt.grid()
plt.show()

#plt.plot(df['id'],df['temp'],df['hum'])

#plt.xlabel('Data')
#plt.ylabel('Parameter fisis')

#plt.show()
