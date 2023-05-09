from django.contrib import admin
from .models import *
# Register your models here.

class CatalogAdmin(admin.ModelAdmin):
	def validate_url(value):
		url_validator = URLValidator()
		try:
			url_validator(value)
		except:
			raise ValidationError("Invalid URL")
	def formfield_for_dbfield(self, db_field, **kwargs):
		if db_field.name == 'url':
			kwargs['validators'] = [validate_url]
		return super().formfield_for_dbfield(db_field, **kwargs)



class blogCommitDetailsAdmin(admin.ModelAdmin):
    list_display= ['id','name','email','comment','created_at','updated_at']
admin.site.register(BlogComment,blogCommitDetailsAdmin)



admin.site.register(Blog)

