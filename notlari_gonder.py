#ÖĞRENCİ NO ;ADI ;SOYADI ;EPOSTA ;1.Sınav Notu
import csv, math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gonderen_adres = 'oguzhan.tas@istinye.edu.tr'
gonderen_sifre = 'Şifreniz'
csv_dosya="notlar.csv"
eposta_konu="1. Vize Notunuz"
hangi_not="1. Vize"
csv_not_index=5
imza="Öğr.Gör. Oğuzhan TAŞ\nİstanbul İstinye Üniversitesi"

def is_not_blank(s):
    return bool(s and s.strip())
# CSV dosyasında sütun indeksi verilen notun Ortalama ve standart sapması hesaplanıyor
def hesapla(dosya, csv_not_index):
    f = open(dosya)
    # CSV dosyasında  alanları birbirinden ayıran işarettir ; olmalıdır, bazen virgül(,) olabilir.
    okunan = csv.reader(f, delimiter=';')
    i = 0
    n=0
    toplam = 0
    not1 = []
    for satir in okunan:
        if (i != 0):
            if (is_not_blank(satir[csv_not_index])):
                toplam += float(satir[csv_not_index])
                not1.append(float(satir[csv_not_index]))
                n+=1
        i += 1
    f.close()
    ortalama = toplam / n
    #print("Toplam:",toplam)
    #print("Adet:",n)
    print("Ortalama:", ortalama)
    toplam2 = 0
    for i in not1:
        toplam2 += ((i - ortalama) ** 2)
    ssapma = round(math.sqrt(toplam2 / (len(not1) - 1)),2)
    print("Standart Sapma:", ssapma)
    return (ortalama,ssapma)
# CSV dosyasında 4 numaralı sütundaki notların ortalama ve std sapması yazılıyor

sonuc=[]
sonuc= hesapla(csv_dosya,csv_not_index)


file = open(csv_dosya)
oku = csv.reader(file, delimiter=';')
i = 0

for s in oku:

    if (i != 0):
            alici_adres = ""
            metin = ""
            mesaj = ""
            metin += "Sayın " + s[1] + " " + s[2] + ",\n\n"
            metin += hangi_not + " Notunuz: " + s[csv_not_index] + "\n"
            metin += "Sınıf Ortalama: " + str(sonuc[0]) + "\n"
            metin += "Sınıf Standart Sapma: " + str(sonuc[1]) + "\n\n"
            metin += "NOT: Bu e-posta Python ile yeni geliştirilen bir yazılımın test amaçlı gönderimidir.\n"
            metin += "Eksik veya yanlış bir bilgi varsa "+gonderen_adres+" adresine bildiriniz.\n\n"
            metin += "İyi günler dilerim...\n\n"
            metin += imza

            alici_adres = s[3]

            mesaj = MIMEMultipart()
            mesaj['From'] = gonderen_adres
            mesaj['To'] = alici_adres
            mesaj['Subject'] = eposta_konu
            mesaj.attach(MIMEText(metin, 'plain'))

            session = smtplib.SMTP('smtp.office365.com', 587)
            session.starttls()
            session.login(gonderen_adres, gonderen_sifre)

            text = mesaj.as_string()
            session.sendmail(gonderen_adres, alici_adres, text)
            session.quit()
            print(str(i) + '. e-posta :' + s[3] + ' (' + s[1] + ' ' + s[2] + '-'+s[0]+') kişiye ' + s[
                csv_not_index] + ' notu gönderildi.')
    i += 1









