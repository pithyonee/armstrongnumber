print("""
////////////////////////////////////////////////
Armstrong sayısı mı ? Değil mi ?
////////////////////////////////////////////////
Eğer bir sayı basamaklarındaki sayıların
basamak sayısı kadar kuvvetleri alınır ve
bu sayılar toplandığında bu sayının kendisine
eşit oluyorsa bu sayısa Armstrong sayısı denir.
////////////////////////////////////////////////
Programdan çıkmak için q yazabilirsiniz.
////////////////////////////////////////////////
""")

while True:
    a= input("Lütfen sayıyı giriniz:")
    bas_say = len(a)
    if (a=="q" or a=="Q"):
        break

    else:
        b = int(a)
        listNumber = list()
        for i in range(0,bas_say):
            x = b % 10
            b = b / 10
            x = int(x)
            listNumber.append(x)

        deger = 0
        for s in listNumber:
            deger += s ** bas_say

        a = int(a)
        print("Armstrong sayısı olması için yapılan işlemler sonucu çıkan sayı {} olur".format(deger))
        if (a == deger):
            print("Girdiğiniz {} sayısı bir Armstrong sayısıdır.".format(a))

        else:
            print("Girdiğiniz sayı bir Armstrong sayısı değildir.")


