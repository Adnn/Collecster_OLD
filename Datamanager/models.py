from django.db import models
from model_utils.managers import InheritanceManager

from south.modelsinspector import add_introspection_rules


class Company(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name

class Concept(models.Model):
    class Category:
        CONSOLE = u'CONSOLE'
        GAME = u'GAME'
        ACCESSORY = u'ACCESSORY'

    CONSOLE = Category.CONSOLE 
    GAME = Category.GAME
    PAD = 'PAD'
    ANALOG_PAD = 'ANALOG_PAD'
    GUN = 'GUN'

    TYPES_SUBTYPES = (
        (CONSOLE, 'Console'),
        (GAME, 'Game'),
        ('Accessory', (
            (PAD, 'Pad'),
            (ANALOG_PAD, 'Analog pad'),
            (GUN, 'Gun'),)
        )
    )
    
    common_name = models.CharField(max_length=60, unique=True)
    complete_name = models.CharField(max_length=180, unique=True, blank=True, null=True)

    company = models.ForeignKey(Company, blank=True, null=True)
    category = models.CharField(max_length=20, choices=TYPES_SUBTYPES,)

    def __unicode__(self):
        return self.common_name

class InstanceParent(models.Model):
    class Meta:
        abstract = True

    ORIGINAL = u'OR'
    BUY_USAGE = u'BU'
    BUY_COLLEC = u'BC'

    ORIGIN = (
        (ORIGINAL, u'Original'),
        (BUY_USAGE, u'Buy usage'),
        (BUY_COLLEC, u'Buy collection'),
    )

    price = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=2, choices=ORIGIN)

#Generic models
class AttributeCategory(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name

class Attribute(models.Model):
    category = models.ForeignKey(AttributeCategory)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u'['+self.category.name+'] '+self.name

class Release(models.Model):
    realised_concept = models.ForeignKey(Concept)
    specificity = models.CharField(max_length=60, blank=True)
    attribute = models.ManyToManyField(Attribute, blank=True)
    objects = InheritanceManager()

    def __unicode__(self):
        return self.realised_concept.common_name

class ReleaseComposition(models.Model):
    container_release = models.ForeignKey(Release, related_name="container_release")
    element_release = models.ForeignKey(Release)

class Instance(InstanceParent):
    instanciated_release = models.ForeignKey(Release)

    def __unicode__(self):
        return str(self.id)+' '+str(self.instanciated_release)

class PictureCategory(models.Model):
    name = models.CharField(max_length=60, unique=True)

def name_picture(instance_picture, filename):
    #The instance picture related instance has already been saved to the DB when we save the instance picture
    path = 'images/instances/' + str(instance_picture.instance.id) + '/' + filename 
    print path
    return path

class InstancePicture(models.Model):
    instance = models.ForeignKey(Instance)
    image = models.ImageField(upload_to=name_picture)
    category = models.ForeignKey(PictureCategory, blank=True, null=True)

class InstanceAttribute(models.Model):
    instance = models.ForeignKey(Instance)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=60)

class InstanceComposition(models.Model):
    container_instance = models.ForeignKey(Instance, related_name="container_instance")
    element_instance = models.ForeignKey(Instance, unique=True)


# Application specific code starts here 
class Region:
    EUROPE = u'EU'
    USA = u'US'
    JAPAN = u'JP'

    CHOICES = (
        (EUROPE, u'Europe'),
        (USA, u'USA'),
        (JAPAN, u'Japan'),
    )
    
class Color:
    BLACK = u'BLK'
    WHITE = u'WIT'
    GREY = u'GRY'
    RED = u'RED'

    CHOICES = (
        (BLACK, u'Black'),
        (WHITE, u'White'),
    )

class WorkingState:
    YES = u'Y'
    NO = u'N'
    UNKNOWN = u'?'

    CHOICES = (
        (UNKNOWN, u'N/A'),
        (YES, u'Yes'),
        (NO, u'No'),
    )

class Platform(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __unicode__(self):
        return self.name

class ConsoleSpecifics(models.Model):
    #unique to simulate one-to-one relationship
    instance = models.ForeignKey(Instance, unique=True)
    working = models.CharField(max_length=1, choices=WorkingState.CHOICES, default=WorkingState.UNKNOWN)
    region_modded = models.BooleanField()
    copy_modded = models.BooleanField()

class Console(Release):
    class Dna:
        specifics = ConsoleSpecifics
        category = Concept.Category.CONSOLE

    version = models.CharField(max_length=20, blank=True, null=True)
    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    color = models.CharField(max_length=3, choices=Color.CHOICES) 
    implemented_platforms = models.ManyToManyField(Platform)


    def __unicode__(self):
        return '[console] ' + str(self.id) + " " + super(Console, self).__unicode__()
   
class GameSpecifics(models.Model):
    instance = models.ForeignKey(Instance, unique=True)
    working = models.CharField(max_length=1, choices=WorkingState.CHOICES, default=WorkingState.UNKNOWN)

class Game(Release):
    class Dna:
        specifics = GameSpecifics
        category = Concept.Category.GAME 

    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    platform = models.ForeignKey(Platform)
    editor = models.ForeignKey(Company, blank=True, null=True)

class AccessorySpecifics(models.Model):
    instance = models.ForeignKey(Instance, unique=True)
    working = models.CharField(max_length=1, choices=WorkingState.CHOICES, default=WorkingState.UNKNOWN)

class Accessory(Release):
    class Dna:
        specifics = AccessorySpecifics
        category = Concept.Category.ACCESSORY

    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    color = models.CharField(max_length=3, choices=Color.CHOICES) 
    compatible_platforms = models.ManyToManyField(Platform)

    wireless = models.BooleanField()
    force_feedback = models.BooleanField()
    rumble_feedback = models.BooleanField()


