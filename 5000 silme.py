import sqlite3
baglanti = sqlite3.connect('personel.db')
baglanti.execute("DELETE from tblurun where urunID = 2;")
baglanti.commit()
cursor = baglanti.execute("SELECT * from tblurun")
print(cursor.fetchall())
baglanti.close()