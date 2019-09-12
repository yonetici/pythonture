from django.contrib import admin

# Register your models here.

from .models import Article
#admin.site.register(Article)
@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    #Listemede görüntülenecek alanlar
    list_display = ["title", "author", "created_date"]
    #Listelemede hangi alanlarda link olmalı
    list_display_links = ["title", "created_date"]
    #Arama ekleme
    search_fields = ["title"]
    #Sağ barda filte oluşturma
    list_filter = ["created_date"]
    #ArticleAdmin ile Article bağlantısı için
    class Meta:
        model = Article

