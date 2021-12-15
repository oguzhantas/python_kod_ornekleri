import sqlite3
baglanti = sqlite3.connect('personel.db')
baglanti.execute("UPDATE tblurun SET URUNADI ='Kalemtraş' where urunID = 2")
baglanti.commit()
cursor = baglanti.execute("SELECT * from tblurun")
print(cursor.fetchall())
baglanti.close()