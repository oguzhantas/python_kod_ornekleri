import sqlite3 #sql lite için bağlantı kütüphanesi
#baglanti kuralım
baglanti = sqlite3.connect('personel.db')
# cursor nesnesi
cursor = baglanti.cursor()
# tablo varsa önce silelim
cursor.execute("DROP TABLE IF EXISTS tblurun")
# tablo oluşturalım
sorgu = """CREATE TABLE "tblurun" (
	"urunID"	INTEGER,
	"URUNADI"	TEXT,
	"BARKOD"	TEXT,
	PRIMARY KEY("urunID" AUTOINCREMENT))"""
cursor.execute(sorgu)
# onaylayıp kaydedelim.
baglanti.commit()
baglanti.close()


