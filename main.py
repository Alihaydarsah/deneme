isim = input("Lütfen isminizi Giriniz: ")
toDoList = []

def gorevEkle(toDoList):
    gorev = input("Yapılacak Olan Görevi Giriniz: ")
    toDoList.append(gorev)
    print("Görev Başarılı bir şekilde eklendi.")

def gorevleriGoster(toDoList):
    print("Yapılacak Görevler:")
    siraSayisi = 1
    for gorev in toDoList:
        print(f"{siraSayisi}- {gorev}")
        siraSayisi += 1

def gorevSil(toDoList):
    gorev = input("Silinecek Görevi Giriniz: ") 
    if gorev in toDoList:
        toDoList.remove(gorev)
        print("Görev Başarılı Bir Şekilde Silindi...")
    else: 
        print("Görev Bulunamadı.")

while True:
    print(f"\nMerhaba {isim}, To Do List Uygulamasına Hoş Geldin!")     
    print("\nLütfen Yapmak İstediğiniz İşlemi Seçiniz:\n"
          "1 - Görev Ekle\n"
          "2 - Görevleri Göster\n"
          "3 - Görev Sil\n"
          "4 - Uygulamadan Çık")

    try:
        secim = int(input("Lütfen Seçiminizi Giriniz: "))
    except ValueError:
        print("Lütfen geçerli bir sayı girin.")
        continue

    if secim == 1:
        gorevEkle(toDoList)
    elif secim == 2:
        gorevleriGoster(toDoList)
    elif secim == 3:
        gorevSil(toDoList)      
    elif secim == 4:
        print("Uygulamadan çıkılıyor...")
        break
    else:
        print("Geçersiz işlem. Lütfen tekrar deneyiniz.")
    