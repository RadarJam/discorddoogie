"""
Write code here which need access to the app during runtime. 
You can decorate functions using '@pyttman.app.hooks.run("before_start")' and have 
them executed before the app goes online - useful for database connections and alike.
"""

import mongoengine as me
from pyttman import app

from abilities.kennel.models import Dog

@app.hooks.run("before_start")
def _():
    pass
    #me.connect(host=app.settings.DB_CONNECTION_STRING, db="kennel",alias='default')
    #number_of_dogs = len(Dogs.objects())
    #£if number_of_dogs == 0:
    #    dog_named_joe = Dog(name="Joe", age="4").save()
    #    dog_named_joe.save()