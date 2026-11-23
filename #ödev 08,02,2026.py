#ödev



#sayfa 73 sıra sizde 

sozluk={"Bilim insanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","astronom":"Ali Kuşçu"}
meslekler=sozluk.copy()
print(sozluk)
sozluk.clear()


sozluk={"Bilim insanı":"Aziz Sancar","Şair":"Mehmet Akif Ersoy","astronom":"Ali Kuşçu"}
print("Sanatçı" in sozluk)
sozluk["Bilim insanı"]="Canan Dağdeviren"
print(sozluk["Şair"])


onemli_telefonlar={"Acil Çağrı Merkezi":"112","Polis İmdat":"155","Milli Eğitim Bakanlığı İletişim Merkezi":"444 0 632"}
print(onemli_telefonlar)
del onemli_telefonlar
önemli_telefonlar={}
  