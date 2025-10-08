from django.contrib import admin
from Card.models import *
# Register your models here.

@admin.register(User_id)
class clientUsere(admin.ModelAdmin):
    list_display = ['dp','First_Name','Last_Name','Occupation','Email','Password']


class Course_list_admin(admin.ModelAdmin):
    list_display=("Course_Title","Course_level","course_intro","Course_time")
admin.site.register(Course_name_list,Course_list_admin)

class Module_admin_list(admin.ModelAdmin):
    list_display=("course","Module_Title","Module_Index")
    list_filter = ('course',)
admin.site.register(Modules_list,Module_admin_list)

# # @admin.register(Card)
# # class CardAdmin(admin.ModelAdmin):
# #     list_display=('Course_Title','Module_Index','Module_Title','Front','Back')
# #     list_filter = ('Course_Title',)

@admin.register(Card)
class CardAdmin(admin.ModelAdmin):
    list_display=('id','course','module','Card_Index','Front','Back')
    list_filter = ('course',)



