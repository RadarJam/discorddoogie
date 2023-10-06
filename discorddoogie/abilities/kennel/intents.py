from pyttman.core.containers import ReplyStream, Reply, Message
from pyttman.core.entity_parsing.fields import StringEntityField
from pyttman.core.intent import Intent
from pyttman.core.entity_parsing.fields import TextEntityField, \
    BoolEntityField, IntEntityField, StringEntityField
from discorddoogie.abilities.kennel.models import Dog
from pyttman import app
import mongoengine

#from discorddoogie.abilities.talk import Talk

class AddDog(Intent):
    lead = ("add",)

    dog_name = TextEntityField(span=5)
    def respond(self, message: Message) -> Reply | ReplyStream:
        mongoengine.connect(**app.settings.DATABASE)
        dog_name = message.entities["dog_name"]

        Dog(name=dog_name, age="2", number_of_recieved_headpats=1).save()

        return Reply("New doogie entered the dooogi house: "+str(dog_name))

class Pet(Intent):
    lead = ("pet",)

    dog_name = TextEntityField(span=5)
    def respond(self, message: Message) -> Reply | ReplyStream:
        mongoengine.connect(**app.settings.DATABASE)
        dog_name = message.entities["dog_name"]

        the_dog = Dog.objects(name=dog_name).first()

        if(the_dog):
            Dog.objects(name=dog_name).update_one(inc__number_of_recieved_headpats=1)           

            return Reply(f"{the_dog.name} recieved one head pat. Total number of headpats: {the_dog.number_of_recieved_headpats}")
        return Reply("Could not find that dooogi")