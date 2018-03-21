from django.contrib import admin
from .models import Tour
from .models import Tourist



class SiteAdmin(admin.ModelAdmin):
   # list_display = ["title", "timestamp"]
    #list_filter = ["timestamp"]
    #search_fields = ["title", "content"]
    class Meta:
        model = Tour

        class Meta:
            model = Tourist

   # class Meta:
    #    model = Name


admin.site.register(Tour, SiteAdmin)

admin.site.register(Tourist, SiteAdmin)


