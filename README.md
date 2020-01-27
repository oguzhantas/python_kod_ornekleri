Bu yazılım, bir CSV dosyasında yer alan not bilgisini, e-posta ile öğrenciye özel olarak göndermek için geliştirilmiştir.  CSV Dosyası aşağıdaki formatta hazırlanmıştır. Biz yine bu dosyada yer alan öğrenci e-posta adresini kullanacağız.

ÖĞRENCİ NO, ADI, SOYADI, EPOSTA, 1.VİZE, 2.VİZE, PROJE, FİNAL, ORTALAMA, HARF NOTU

Diyelim ki 1.VİZE notunu göndermek istiyorsunuz, sol baştan itibaren 0,1,2,3 şeklinde sayarsanız 4.sırada olduğunu görürüz. Bu nedenle csv_not_index bilgisi 4 yazarız. Eğer 2.VİZE notunu göndermek istiyorsanız csv_not_index değeri 5 olarak yazılır. Örneğin Final sınavı için de ayrı bir sütun açıp notları girdikten sonra bu program aracılığı ile öğrencilerinize toplu gönderebilirsiniz.  

ÖNEMLİ NOT 1: CSV dosyasını incelediğinizde bir satırdaki verilerin noktalı virgül(;) ile ayrıldığını görürüz. Bazı CSV dosyaları virgül(,) ile ayarlanmış olabilir, bu durumda okunan = csv.reader(f, delimiter=';') satırını bulup noktalı virgül yerine virgül yapınız.

ÖNEMLİ NOT 2: CSV dosyasında küsürat haneleri virgül(,) ile ayrılmışssa, editörden Bul-değiştir(Replace) yaparak mutlaka nokta(.) şekline çeviriniz. Örneğin 83,25 olmamalı, 83.25 olmalıdır.

Kodlar Ubuntu Linux üzerinde test edilmiştir.  Örnek CSV dosyası verilmiştir, bu dosyayı indirip doldurabilirsiniz. E-posta metninin kendinize göre değiştirebilirsiniz.

Öğrencinize aşağıdaki gibi bir e-mail gidecektir.






ÖRNEK E-MAİL ÇIKTISI:

Oguzhan TAS, ISU <oguzhan.tas@istinye.edu.tr>
	
16:30 (5 dakika önce)
	
Alıcı: ben
Sayın Oğuzhan Taşkent,

Quiz Notunuz: 88
Quiz Sınıf Ortalaması: 88.0

1.Vize Notunuz: 93
1.Vize Sınıf Ortalaması: 90.5

2.Vize Notunuz: 93
2.Vize Sınıf Ortalaması: 91.5

Proje Notunuz: 75
Proje Sınıf Ortalaması: 87.5

Final Notunuz: 88
Final Sınıf Ortalaması: 81.5

Geçme Notunuz: 86.25
Final Sınıf Ortalaması: 86.175

Harf Notunuz: AA

NOTLAR:
1) Notu DC veya DD olan öğrencinin mezuniyet aşamasında not ortalaması 2.00 altında olması .
durumunda veya yönetmelikte yazan bazı durumlarda öğrenci bu dersi tekrar edebilir.

AA =>4    =>(86-100 arası)        =>Geçti
BA =>3.5  =>(80-85 arası)         =>Geçti
BB =>3    =>(70-79 arası)         =>Geçti
CB =>2.5  =>(60-69 arası)         =>Geçti
CC =>2    =>(46-59 arası)         =>Geçti
DC =>1.5  =>(40-45 arası)         =>Şartlı Geçti
DD =>1    =>(33-39 arası)         =>Şartlı Geçti
FF =>0    =>(0-32 arası)          =>Kaldı
DZ => Devamsız Başarısız(Finale gelmeyen)   =>Kaldı

2) Bu e-posta Python ile yeni geliştirilen bir yazılımın test amaçlı gönderimidir.
Eksik veya yanlış bir bilgi varsa oguzhan.tas@istinye.edu.tr adresine bildiriniz.

İyi günler dilerim...

Öğr.Gör. Oğuzhan TAŞ
İstanbul İstinye Üniversitesi
[Oguzhan TAS, ISU İmza]
