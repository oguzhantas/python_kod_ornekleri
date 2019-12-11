Bu yazılım, bir CSV dosyasında yer alan not bilgisini öğrenciye özel olarak göndermek için geliştirilmiştir.  CSV Dosyası aşağıdaki formatta hazırlanmıştır. 

ÖĞRENCİ NO, ADI, SOYADI, EPOSTA, 1.VİZE, 2.VİZE

Diyelim ki 1.VİZE notunu göndermek istiyorsunuz, sol baştan itibaren 0,1,2,3 şeklinde sayarsanız 4.sırada olduğunu görürüz. Bu nedenle csv_not_index=4 yazarız. Eğer 2.VİZE notunu göndermek istiyorsanız csv_not_index=5 yazarız. 

NOT: CSV dosyasını incelediğinizde bir satırdaki verilerin noktalı virgül(;) ile ayrıldığını görürüz. Bazı CSV dosyaları virgül(,) ile ayarlanmış olabilir, bu durumda okunan = csv.reader(f, delimiter=';') satırını bulup noktalı virgül yerine virgül yapınız.

Kodlar Ubuntu Linux üzerinde test edilmiştir.  Örnek CSV dosyası verilmiştir, bu dosyayı indirip doldurabilirsiniz.
