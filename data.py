import time
import pandas as pd
import re
import requests
from bs4 import BeautifulSoup
from validate_email_address import validate_email

# Kullanıcıdan aranacak kelimeyi alın
aranacak_kelime = input("Aramak istediğiniz kelimeyi girin: ")

# Kaç adet e-posta adresi istendiğini kullanıcıdan alın
eposta_adresi_sayisi = int(input("Kaç adet e-posta adresi istediğinizi girin: "))

# Arama sorgusu oluşturun
arama_kelimesi = f'{aranacak_kelime} "@gmail.com" site:instagram.com'

# E-posta adreslerini tutmak için bir liste oluşturun
eposta_listesi = []

# İlgili arama sonuçlarını döndüren bir döngü oluşturun
for i in range(10):  # İlk 10 sayfa için döngü oluşturduk
    # Sayfa numarasına göre arama sonuçlarını alın
    start = i * 10
    url = f"https://www.google.com/search?q={arama_kelimesi}&start={start}"

    # Sayfayı indirin ve BeautifulSoup ile analiz edin
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    # Sayfadaki metni bulun ve içerisindeki e-posta adreslerini arayın
    metin = soup.get_text()
    eposta_adresleri = re.findall(r'[\w\.-]+@[\w\.-]+\.\w+', metin)

    # E-posta adreslerini doğrula ve listeye ekleyin
    for eposta in eposta_adresleri:
        if eposta not in eposta_listesi and validate_email(eposta):
            eposta_listesi.append(eposta)
            print(eposta)  # Terminalde bulunan e-posta adreslerini yazdırın

    # E-posta adresi sayısı istenilen miktara ulaşıldığında döngüyü sonlandırın
    if len(eposta_listesi) >= eposta_adresi_sayisi:
        break

    # İstekler arasına gecikme ekleyin
    time.sleep(2)  # 2 saniye gecikme örneği

# E-posta adreslerini bir Excel dosyasına kaydedin
df = pd.DataFrame({'E-posta Adresi': eposta_listesi})
df.to_excel('eposta_adresleri.xlsx', index=False)

print("E-posta adresleri başarıyla kaydedildi.")
