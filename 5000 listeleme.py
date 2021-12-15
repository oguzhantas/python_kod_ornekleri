import sqlite3
baglanti = sqlite3.connect('personel.db')
cursor = baglanti.execute("SELECT * from tblurun")
print(cursor.fetchall())
baglanti.close()