from django.contrib import admin

from .models import Article,Comment

# Register your models here. Yani admin paneline Article dahil etmek için yapılan işlem..

admin.site.register(Comment)

@admin.register(Article) #register ettik
class ArticleAdmin(admin.ModelAdmin): #ArticleAdmin diye ad verdik. en yukarıda "import admin" den türeyen bir class yazdık.. Admin sayfasında görünmesi için..
    
    list_display=["title","author","created_date"]
    list_display_links=["title","created_date"]
    
    search_fields=["title"]

    list_filter=["created_date"]
    
   

    class Meta: #Django meta yazacaksın diyor.. Böylece Admin paneli özelleştrilmeye başlanacabilecek.
        model= Article