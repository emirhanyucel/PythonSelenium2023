liste = ["Ali Yılmaz","Ayşe Doğan","Veli Demir","Deniz Çelik"]

def ogrenciEkle():
    ad = input("Ad giriniz: ")
    soyad =input("Soyadı giriniz: ")
    ogrenci = ad + " " + soyad
    if ogrenci in liste:
        print("Bu öğrenci zaten listede.")
    else:
        liste.append(ogrenci)
        print(ogrenci + " listeye eklendi.")
    print(liste)


def ogrenciSil():
    ad = input("Ad giriniz: ")
    soyad = input("Soyadı giriniz: ")
    ogrenci = ad + " " + soyad
    if ogrenci in liste:
        liste.remove(ogrenci)
        print( ogrenci + " isimli öğrenci silindi.")
    else:
        print(ogrenci + " listede bulunamadı.")
    print(liste)

def cokOgrenciEkle():
    kacOgrenci = int(input("Eklemek istediğiniz öğrenci sayısını giriniz: "))
    for i in range(kacOgrenci):
        ogrenciEkle()
    print(liste)

def cokOgrenciSil():
    kacOgrenci = int(input("Silmek istediğiniz öğrenci sayısını yazınız: "))
    i = 0
    while i < kacOgrenci:
        ogrenciSil()
        i +=1
    print(liste)

#1'den başlayarak numarasıyla birlikte listeyi gösterir.
def listeyiGoster():
    print("Sınıf listesi: ")
    for ogrenci in range(len(liste)):
        print(f"{ogrenci + 1} -- {liste[ogrenci]}")
    


ogrenciEkle()
ogrenciSil()
cokOgrenciEkle()
cokOgrenciSil()
listeyiGoster()
