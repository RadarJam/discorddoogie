# Created by Pyttman 
from mongoengine import *

class Dog(Document):
    name = StringField(max_length=50)
    age = StringField(max_length=50)
    number_of_recieved_headpats = IntField()