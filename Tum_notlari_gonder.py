#ÖĞRENCİ NO ;ADI ;SOYADI ;EPOSTA ;1.Sınav Notu
import csv, math
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

gonderen_adres = 'oguzhan.tas@istinye.edu.tr' #e-posta adresiniz
gonderen_sifre = 'Şifreniz' #e-posta şifreniz
csv_dosya="deneme_notlar.csv" #Göndereceğiniz CSV dosyası, Excel'de farklı kaydet seçip CSV formatında kaydedebilirsiniz.
eposta_konu="Quiz, 1. Vize, 2.Vize, Proje Notlarınız" #E-posta başlığı
csv_not_indexler=[4,5,6,7] #Burada CSV(Excel) belgesindeki sütün numarası yazılıyor, ilk sütün 0'dan başlıyor, sonra 1,2,3... şeklinde gidiyor.
imza="Öğr.Gör. Oğuzhan TAŞ\nİstanbul İstinye Üniversitesi" # E-postanın altında yer alacak imza

def is_not_blank(s):
    return bool(s and s.strip())
# CSV dosyasında sütun indeksi verilen notun Ortalaması hesaplanıyor
def hesapla(dosya, not_index):
    f = open(dosya)
    okunan = csv.reader(f, delimiter=',') # CSV dosyasında  alanları birbirinden ayıran işarettir noktalı virgül(;) veya virgül(,) olabilir.
    i = 0
    n=0
    toplam = 0
    not1 = []
    for satir in okunan:
        if (i != 0):
            if (is_not_blank(satir[not_index])):
                toplam += float(satir[not_index])
                not1.append(float(satir[not_index]))
                n+=1
        i += 1
    f.close()
    if (n!=0):
     ortalama = toplam / n
    return (ortalama)

# her bir sütunun ortalaması ayrı ayrı hesaplanıp sonuc listesine(dizisine) atılıyor
sonuc=[]
for k in range(len(csv_not_indexler)):
    sonuc.append(hesapla(csv_dosya,csv_not_indexler[k]))


#notların bulunduğu dosya açılıyor ve notları e-mail atıyoruz.
file = open(csv_dosya)
oku = csv.reader(file, delimiter=',')
i = 0
for s in oku:

    if (i != 0):
            alici_adres = ""
            metin = ""
            mesaj = ""
            metin += "Sayın " + s[1] + " " + s[2] + ",\n\n"

            metin += "Quiz Notunuz: " + s[4] + "\n"  #Quiz notu örnek dosyada 4.sütünda, sütunlar 0'dan başlıyor
            metin += "Quiz Sınıf Ortalaması: " + str(sonuc[0]) + "\n\n"

            metin += "1.Vize Notunuz: " + s[5] + "\n" # Vize 1 değeri 5. sütunda
            metin += "1.Vize Sınıf Ortalaması: " + str(sonuc[1]) + "\n\n"

            metin += "2.Vize Notunuz: " + s[6] + "\n" # Vize 2 değeri 6. sütunda
            metin += "2.Vize Sınıf Ortalaması: " + str(sonuc[2]) + "\n\n"

            metin += "Proje Notunuz: " + s[7] + "\n" #Proje Notu 7.sütunda
            metin += "Proje Sınıf Ortalaması: " + str(sonuc[3]) + "\n\n"

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
            # Aşağıdaki satır her e-posta gönderildikten sonra bilgi amaçlı ekrana yazılıyor.
            print(str(i) + '. e-posta :' + s[3] + ' (' + s[1] + ' ' + s[2] + '-'+s[0]+') kişiye ' + s[4]+' '+s[5] +' '+s[6]+' '+s[7]+ ' notu gönderildi.')
    i += 1









