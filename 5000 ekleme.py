import sqlite3
baglanti = sqlite3.connect('personel.db')
baglanti.execute("INSERT INTO tblurun (URUNADI,BARKOD) "
             "VALUES ('Defter','86900000012')")
baglanti.execute("INSERT INTO tblurun (URUNADI, BARKOD) "
             "VALUES ('Kalem','86900000013')")
baglanti.execute("INSERT INTO tblurun (URUNADI, BARKOD) "
             "VALUES ('Silgi','86900000014')")
baglanti.commit()
baglanti.close()