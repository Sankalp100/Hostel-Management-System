from django.contrib import admin
from .models import Student, Block, Room

# admin.site.register(Student)
# admin.site.register(Room)
admin.site.register(Block)

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('name','f_name', 'date_of_birth', 'roll_num', 'room_num' , 'reg_date', 'per_address')
    list_filter  = ('room_num','reg_date')
@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ('room_num', 'accommodation', 'status', 'block_num')