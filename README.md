# Google'da E-posta Adresi Arama Aracı

Bu Python betiği, Google arama motorunu kullanarak belirli bir kelimeyi ve belirli bir web sitesini hedefleyen e-posta adreslerini bulmanıza yardımcı olur. Kod, belirli bir kelimeyi içeren ve belirli bir sitede bulunan e-posta adreslerini toplar. Elde edilen e-posta adresleri daha sonra bir Excel dosyasına kaydedilir.


## Gereksinimler

Bu betiği çalıştırmak için aşağıdaki Python kütüphanelerine ihtiyacınız vardır. Gereksinimleri yüklemek için aşağıdaki komutları kullanabilirsiniz:

```bash
pip install -r requirements.txt
```

## Kullanım

Betiği çalıştırırken, aşağıdaki argümanları kullanarak e-posta adresleri çekmek istediğiniz web sitesini, aranacak kelimeyi ve çekilecek e-posta adresi sayısını belirtmelisiniz:

- `-s` veya `--site`: E-posta adresleri çekilecek web sitesini belirtin.
- `-k` veya `--keyword`: Aranacak kelimeyi belirtin.
- `-n` veya `--num_emails`: Kaç adet e-posta adresi çekileceğini belirtin.

Örnek kullanım:
```python
python script.py -s instagram -k "web developer" -n 10
```

![image](https://github.com/ugurcomptech/Instagram-mail-scarping/assets/133202238/040b6682-6ef8-4a56-8015-90854978f927)


## Önemli Notlar

- Bu betiğin Google arama sonuçlarını çektiğini unutmayın. Google, otomasyonlu sorguları sınırlayabilir veya yasaklayabilir.
- Bu kod örneği, yalnızca eğitim amaçlıdır. Toplanan e-posta adreslerini spam veya kötü amaçlı kullanım için kullanmamalısınız.
- Eğer HTTPS hatası alırsanız VPN açıp kullanmaya devam edebilirsiniz.


## Lisans

[![License: CC BY-NC-SA 4.0](https://licensebuttons.net/l/by-nc-sa/4.0/88x31.png)](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode)

Bu projeyi [Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International License](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) altında lisansladık. Lisansın tam açıklamasını [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode) sayfasında bulabilirsiniz.
