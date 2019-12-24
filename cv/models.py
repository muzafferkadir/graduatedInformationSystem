from django.db import models
from users.models import UserTable 

class KisiselBilgiler(models.Model):
    ad = models.OneToOneField(UserTable, on_delete=models.CASCADE) 
    mdurum = models.CharField(max_length=5)
    ehliyet = models.BooleanField()
    #fotograf = models.ImageField()
    uyruk = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'Kişisel Bilgiler'

    def _str_(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{ad} {soyad}'.format(ad=self.ad, soyad=self.soyad)


class IletisimBilgileri(models.Model):
    ad = models.ForeignKey(UserTable,
                           related_name ='IletisimBilgileri',
                           on_delete=models.CASCADE
                          )
    eposta = models.EmailField()
    tel1 = models.CharField(max_length=30)
    tel2 = models.CharField(max_length=30, blank=True)
    adres = models.TextField()

    class Meta:
        verbose_name = 'İletişim Bilgileri'

    def _str_(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{ad} {soyad}'.format(ad=self.ad.ad, soyad=self.ad.soyad)

class IsDeneyimi(models.Model):
    ad = models.ForeignKey(UserTable,
                           related_name ='IsDeneyimi',
                           on_delete=models.CASCADE
                          )
    sTarihi = models.DateField(blank=True)
    fTarihi = models.DateField(blank=True)
    sAD = models.TextField(blank=True)
    unvan = models.CharField(max_length=30)

    class Meta:
        verbose_name = 'İş Deneyimi'

    def _str_(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{ad} {soyad} - {unvan}'.format(ad=self.ad.ad,
                                               soyad=self.ad.soyad,
                                               unvan=self.unvan
                                               )

class EgitimBilgileri(models.Model):
    ad = models.ForeignKey(UserTable,
                           related_name ='EgitimBilgileri',
                           on_delete=models.CASCADE
                          )
    sTarihi = models.DateField()
    fTarihi = models.DateField()
    oAd = models.TextField(max_length=50)

    class Meta:
        verbose_name = 'Eğitim Bilgileri'

    def _str_(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{ad} {soyad} - {oAd}'.format(ad=self.ad.ad,
                                             soyad=self.ad.soyad,
                                             oAd=self.oAd
                                             )

class YabanciDil(models.Model):
    ad = models.ForeignKey(UserTable,
                           related_name ='YabanciDil',
                           on_delete=models.CASCADE
                          )
    yAd = models.CharField(max_length=20)
    ySeviye = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Yabancı Dil Ve Seviyesi'

    def _str_(self):
        return self.get_full_name()

    def get_full_name(self):
        return '{ad} {soyad} - {yAd}'.format(ad=self.ad.ad,
                                             soyad=self.ad.soyad,
                                             yAd=self.yAd
                                             )

class KatildigiSeminerveKurslar(models.Model):
        ad = models.ForeignKey(UserTable,
                               related_name ='KatildigiSeminerveKurslar',
                               on_delete=models.CASCADE)
        sTarihi = models.DateField(blank=True)
        fTarihi = models.DateField(blank=True)
        kurs = models.CharField(max_length=50, blank=True)
        seminer = models.CharField(max_length=50, blank=True)
        sertifikalar = models.CharField(max_length=30, blank=True)
        sertifikano = models.CharField(max_length=30, blank=True)
        dernekvekulupuyelikleri = models.CharField(max_length=50, blank=True)

        class Meta:
            verbose_name = 'KatildigiSeminerveKurslar'

        def _str_(self):
            return self.get_full_name()

        def get_full_name(self):
            return '{ad} {soyad} - {kurs} - {seminer}'.format(ad=self.ad.ad,
                                                            soyad=self.ad.soyad,
                                                            kurs=self.kurs,
                                                            seminer=self.seminer
                                                            )


class Referanslar(models.Model):
        ad = models.ForeignKey(UserTable,
                               related_name ='Referanslar',
                               on_delete=models.CASCADE)
        referans = models.CharField(max_length=50, blank=True)
        referansverenkisiveyakurum = models.CharField(max_length=30, blank=True)

        class Meta:
             verbose_name = 'Referanslar'

        def _str_(self):
             return self.get_full_name()

        def get_full_name(self):
            return '{ad} {soyad}-{referans}'.format(ad=self.ad.ad,
                                                    soyad=self.ad.soyad,
                                                    referans=self.referans
                                                    )

class EkBilgiler(models.Model):
        ad = models.ForeignKey(UserTable,
                               related_name ='EkBilgiler',
                               on_delete=models.CASCADE)
        saglikdurumu = models.CharField(max_length=30)
        askerlik = models.CharField(max_length=15, blank=True)
        kariyerhedefi = models.TextField(max_length=60)
        sigaraalkolkullanimi = models.CharField(max_length=30, blank=True)
        eklIstedikleri = models.TextField(blank=True)

        class Meta:
            verbose_name = 'EkBilgiler'

        def _str_(self):
            return self.get_full_name()

        def get_full_name(self):
            return '{ad} {soyad}-{eklIstedikleri}'.format(ad=self.ad.ad,
                                            soyad=self.ad.soyad,
                                            eklIstedikleri=self.eklIstedikleri)
