import sqlite3
baglanti = sqlite3.connect('personel.db')

sorgu = ('INSERT INTO tblurun (URUNADI, BARKOD) '
         'VALUES (:urunadi, :barkodno);')
parametreler = {
        'urunadi': 'Kalemtraş',
        'barkodno': '86900000014'
    }
baglanti.execute(sorgu, parametreler)
baglanti.commit()
baglanti.close()