from django.contrib import admin
from .models import Unit
from .models import Register_Unit
from .models import User

# Register your models here.
class UnitAdmin(admin.ModelAdmin):
    list_display = ('pk', 'subject_name', 'subject_category')

class UserAdmin(admin.ModelAdmin):
    list_display = ('pk', 'compulsory_unit', 'select_unit', 'free_unit', 'core_unit')


admin.site.register(Unit, UnitAdmin)
admin.site.register(Register_Unit)
admin.site.register(User, UserAdmin)
 

