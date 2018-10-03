from django.urls import reverse
from django.db import models

class Student(models.Model):
    name          =  models.CharField(max_length = 200)
    roll_num      =  models.CharField(max_length = 10, primary_key =True)
    f_name        =  models.CharField(max_length = 200)
    m_name        =  models.CharField(max_length = 200)
    date_of_birth =  models.DateField(null =True, blank = True)
    reg_date      =  models.DateField(null =True)
    fee_receipt   =  models.CharField(max_length = 20, null =True)
    per_address   =  models.TextField(null =True)
    city          =  models.CharField(max_length = 100, null =True, blank = True)
    state         =  models.CharField(max_length = 100, null =True, blank = True)
    room_num      = models.ForeignKey('Room', on_delete=models.SET_NULL, null = True, blank = True)
    
    class Meta:
        ordering = ['name']

    def __str__(self):
        return '%s %s %s' % (self.name, self.roll_num, self.room_num)

    def get_absolute_url(self):
        return reverse('student-detail', args=[str(self.roll_num)])


class Block(models.Model):
    block_num = models.CharField(
        max_length  = 1,
        choices     = (('A', 'Block-A'), ('B', 'Block-B'), ('C', 'Block-C')),
        default     = 'A',
        primary_key = True
    )

class Room(models.Model):
    room_num        = models.CharField( max_length = 4, primary_key = True)
    accommodation   = models.CharField(
        max_length  = 10,
        choices     =  (('S', 'Single'),('D', 'Double'), ('T', 'Triple')),
        default     =  'T',
    )
    room_status     = (
        ('A', 'Available'),
        ('NA', 'Not Available')
    )
    status         = models.CharField(
        max_length = 2,
        choices    = room_status,
        blank = True,
        help_text = 'Room Availability'
    )

    block_num      =  models.ForeignKey(Block, on_delete=models.SET_NULL, null = True, blank = True)

    class Meta():
        ordering = ['status']
    
    def __str__(self):
        return '%s %s' % (self.room_num, self.status)