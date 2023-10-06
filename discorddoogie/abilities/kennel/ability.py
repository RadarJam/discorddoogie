"""
This ability holds intents related to the
Recipes feature of the application.
"""

from pyttman.core.ability import Ability
from discorddoogie.abilities.kennel.intents import AddDog, Pet


class TalkAbility(Ability):
    """
    Ability class for recipes, storing and retrieving
    recipes in the application
    """
    intents = (AddDog, Pet)