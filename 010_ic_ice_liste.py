kultur_dersler=["fizik","matematik","kimya"]
dersler=["programlama temelleri","BTT",kultur_dersler]
print(dersler)

cift_sayilar=[0,2,4,6,8]
sayilar=[1,3,5,7, cift_sayilar]
print(sayilar)

bellekler=["RAM","ROM","EPROM","EEPROM"]
sabitdiskler=["IDE","SCSI","SSD"]
yazicilar=["mürekkepli","tonerli","nokta vuruşlu"]
parcalar=bellekler,sabitdiskler,yazicilar
print(parcalar)
#print(parcalar[0][2]) #EPROM
print(parcalar[0,2])
#print(parcalar[0][3]) #EEPROM
#print(parcalar[2][0]) #mürekkepli

