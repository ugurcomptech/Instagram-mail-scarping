# Google'da E-posta Adresi Arama Aracı

Bu Python betiği, Google arama motorunu kullanarak belirli bir kelimeyi ve belirli bir web sitesini hedefleyen e-posta adreslerini bulmanıza yardımcı olur. Kod, belirli bir kelimeyi içeren ve belirli bir sitede ("instagram.com") bulunan e-posta adreslerini toplar. Elde edilen e-posta adresleri daha sonra bir Excel dosyasına kaydedilir.

## Gereksinimler

Bu betiği çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır:

- `time`: Zaman gecikmeleri için kullanılır.
- `pandas`: Veri çerçeveleri oluşturmak ve Excel dosyasına veri kaydetmek için kullanılır.
- `re`: Düzenli ifadelerle metin eşleştirmek için kullanılır.
- `requests`: Web sayfalarını indirmek için kullanılır.
- `bs4` (BeautifulSoup): HTML içeriğini analiz etmek için kullanılır.
- `validate_email`: E-posta adreslerini doğrulamak için kullanılır.

Bu kütüphaneleri yüklemek için terminale aşağıdaki komutları kullanabilirsiniz:

```python
pip install pandas beautifulsoup4 validate_email_address
```

## Nasıl Kullanılır


![İsimsiz video ‐ Clipchamp ile yapıldı](https://github.com/ugurcomptech/Instagram-mail-scarping/assets/133202238/1270dfb0-c578-43b0-be68-8a9e49d610b7)


1. Kodu indirin veya kopyalayın.
2. Terminali açın ve kodun olduğu klasöre gidin.
3. Kodu çalıştırmak için aşağıdaki komutu kullanın:

```python
python data.py
```

4. İstenilen kelimeyi ve e-posta adresi sayısını girin.
5. Kod, belirtilen kelimeyi ve sitedeki e-posta adreslerini Google aramasıyla bulmaya başlayacaktır.
6. Bulunan e-posta adresleri ekranda görüntülenecek ve `eposta_adresleri.xlsx` adlı bir Excel dosyasına kaydedilecektir.

## Önemli Notlar

- Bu betiğin Google arama sonuçlarını çektiğini unutmayın. Google, otomasyonlu sorguları sınırlayabilir veya yasaklayabilir.
- Bu kod örneği, yalnızca eğitim amaçlıdır. Toplanan e-posta adreslerini spam veya kötü amaçlı kullanım için kullanmamalısınız.
- Eğer HTTPS hatası alırsanız VPN açıp kullanmaya devam edebilirsiniz.


## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.
