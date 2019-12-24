from django.contrib import admin
from .models import (
                    KisiselBilgiler, IletisimBilgileri,
                    IsDeneyimi, EgitimBilgileri, YabanciDil,
                    KatildigiSeminerveKurslar, Referanslar,
                    EkBilgiler
                    )
                    
@admin.register(KisiselBilgiler)
class KisiselBilgilerAdmin(admin.ModelAdmin):
      fields = ('ehliyet', 'uyruk')
      list_display = ('ad', )
      search_fields = ('ad',)
      list_filter = ('ehliyet', 'mdurum', 'uyruk')


@admin.register(IletisimBilgileri)
class IletisimBilgileriAdmin(admin.ModelAdmin):
      fields = ('tel1', 'adres', 'eposta')
      list_display = ('eposta',)
      search_fields = ('adres',)
      list_filter = ('adres',)


@admin.register(IsDeneyimi)
class IsDeneyimiAdmin(admin.ModelAdmin):
      fields = ('unvan',)
      list_display = ('unvan',)
      search_fields = ('unvan',)
      list_filter = ('unvan',)


@admin.register(EgitimBilgileri)
class EgitimBilgileriAdmin(admin.ModelAdmin):
      fields = ('oAd', 'sTarihi', 'fTarihi')
      search_fields = ('oAd',)
      list_display = ('oAd',)


@admin.register(YabanciDil)
class YabaciDilBilgisiAdmin(admin.ModelAdmin):
      fields = ('yAd', 'ySeviye')
      list_display = ('yAd', 'ySeviye' )
      search_fields = ('yAd', 'ySeviye')
      list_filter = ('yAd', 'ySeviye')


@admin.register(KatildigiSeminerveKurslar)
class KatildigiSeminerveKurslarAdmin(admin.ModelAdmin):
      fields = ('kurs', 'seminer', 'sertifikalar')
      list_display = ('sertifikalar',)
      search_fields = ('sertifikalar',)
      list_filter = ('sertifikalar',)


@admin.register(Referanslar)
class ReferanslarAdmin(admin.ModelAdmin):
      fields = ('referans',)
      list_display = ('referans',)
      search_fields = ('referans',)
      list_filter = ('referans',)

@admin.register(EkBilgiler)
class EkBilgilerAdmin(admin.ModelAdmin):
      fields = ('saglikdurumu','kariyerhedefi')
      list_display = ('saglikdurumu',  'kariyerhedefi')
      search_fields = ('saglikdurumu',  'kariyerhedefi',
                       'askerlik')
      list_filter = ('askerlik', 'saglikdurumu', )