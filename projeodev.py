import sys



 

k=0
user='fatma dogan'
while k<3:
    
    
    a=input("Lütfen kullanıcı adınızı giriniz:")
    
    if a==user:
         print("WELCOME")
         k=3 
    else:
             k=k+1
             if k==3:
                 print("Please try again later..") 
                 sys.exit()
                 

                 
                 
dersgir=[]
k=0
a=int(input("Kaç ders seçmek istersiniz:"))


while a<3 or a>5:

        print("You failed in class")
        a=int(input("Kaç ders seçmek istersiniz:"))
        


while k<a:
    ders=input("Derslerinizi seçiniz:")
    k=k+1
    dersgir.append(ders)
    
print("DERSLERİNİZ:",dersgir)
lesson=input("Bir ders seçiniz ve sınava giriniz:")
vize=int(input("Vize notunuzu giriniz:"))
final=int(input("Final notunuzu giriniz:"))
proje=int(input("Proje notunuzu giriniz:"))
puanlar={"vize":vize,"final":final,"proje":proje}
print("NOTLARINIZ:",puanlar)
ortalama=0
ortalama=(vize/100*30)+(final/100*50)+(proje/100*20)
print("Ortalamanız:",ortalama)

harf=''

if ortalama>=90:
    harf='AA'
elif ortalama>=70 and ortalama<90:
    harf='BB'
elif ortalama>=50 and ortalama<70:
    harf='CC'
elif ortalama<=30 and ortalama<50:
    harf='DD'
else:
    harf='FF'


    
print("Harf notunuz:",harf)