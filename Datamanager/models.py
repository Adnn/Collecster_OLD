from django.db import models
from model_utils.managers import InheritanceManager

from south.modelsinspector import add_introspection_rules

import qrcode
from PIL import Image, ImageDraw

import os

from Datamanager import stringer
from Datamanager import settings


def generate_qr(id):
    qr = qrcode.QRCode(
        box_size = settings.TAG_QR_BOXSIZE,
    )
    qr.add_data(str(id))
    return qr.make_image()._img

def get_textsize(text):
        dum_img = Image.new('RGB', (1, 1), 'white')
        dum_draw = ImageDraw.Draw(dum_img)
        return dum_draw.textsize(text)

def organize_tag(release_img, instance_img, qr_img, border=True):
    
    if border:
        border_size = 1
    else:
        border_size = 0

    left_width = max(
        release_img.size[0],
        instance_img.size[0],
        settings.TAG_MIN_COLS*get_textsize('_')[0]
    )
    width = 2*border_size + qr_img.size[0] + left_width
    height = 2*border_size + max(qr_img.size[1], (release_img.size[1]+instance_img.size[1]))

    final_image = Image.new('RGB', (width, height), 'white')
    draw = ImageDraw.Draw(final_image)
    if(border):
        draw.rectangle([(0,0), (width-1, height-1)], outline='black') 
    
    final_image.paste(release_img, (border_size, border_size))
#we want to put the instance details at the bottom edge
    final_image.paste(instance_img, (border_size, height-border_size-instance_img.size[1]))
    final_image.paste(qr_img, (border_size+left_width, border_size))
    
    return final_image

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

    
#crazy Python does not allow to call a class method (or static method) inside the class defining it, so get_choices has to be defined outside (and before) InstanceParent, and still see ORIGIN_DICT.
#a default method (without self) would not be able to see the static dict at all.
class Origin():
    ORIGINAL = u'OR'
    BUY_USAGE = u'BU'
    BUY_COLLEC = u'BC'

#element :    key(=value to be stored in DB) : (web display value, tag spot color)
    ORIGIN_DICT = {
        ORIGINAL : (u'Original', 'green'),
        BUY_USAGE : (u'Buy usage', 'blue'),
        BUY_COLLEC : (u'Buy collection', 'red'),
    }

    """ORIGIN = (
        (ORIGINAL, u'Original'),
        (BUY_USAGE, u'Buy usage'),
        (BUY_COLLEC, u'Buy collection'),
    )"""

    @classmethod
    def get_choices(cls):
        return [(key, value[0]) for key, value in cls.ORIGIN_DICT.items()]


class InstanceParent(models.Model):
    class Meta:
        abstract = True

    price = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=2, choices=Origin.get_choices())

    def get_parent_tag(self):
        parent_image = Image.new('RGB', (20, settings.TAG_INSTANCEDETAIL_HEIGHT), 'white')
        draw = ImageDraw.Draw(parent_image)

        draw.ellipse([5, 5, 15, 15], fill=Origin.ORIGIN_DICT[self.origin][1])
        return parent_image

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

    def get_tag(self):
        name_color = 'black'
        try:
            name_color = type(self).Dna.name_color
        except AttributeError:
            pass
        name = stringer.balance_string(self.realised_concept.common_name, settings.TAG_MAX_LINES, settings.TAG_MIN_COLS) 
        name_lines = name.split(os.linesep)

        def add(x, y):
            return x+y
        name_width = reduce(max, [width for width, height in map(get_textsize, name_lines)])
        name_height = reduce(add, [height for width, height in map(get_textsize, name_lines)])
        complement = self.get_tag_complement()
        if complement:
            complement_size = get_textsize(complement)
        else:
            complement_size = (0, 0)

        left_pad = 2
        release_img = Image.new('RGB', (max(name_width, complement_size[0])+left_pad, name_height+complement_size[1]), 'white')
        release_draw = ImageDraw.Draw(release_img)

        offset = 0
        for name_part in name_lines:
            release_draw.text((left_pad, offset), name_part, fill=name_color)
            offset += release_draw.textsize(name_part)[1]

        if complement:
            release_draw.text((left_pad, offset), complement, fill='black')


        return release_img

    """ An empty method in case the release subclass does not override it """
    # \return : string complement information
    def get_tag_complement(self):
        return

class ReleaseComposition(models.Model):
    container_release = models.ForeignKey(Release, related_name="container_release")
    element_release = models.ForeignKey(Release)

class Instance(InstanceParent):
    instanciated_release = models.ForeignKey(Release)

    def __unicode__(self):
        return str(self.id)+' '+str(self.instanciated_release)

    def generate_tag(self):
        release_subclass = Release.objects.get_subclass(id=self.instanciated_release.id)
        ReleaseSpecifics = type(release_subclass).Dna.specifics
        #generate the qrcode base on Instance.id (i.e. per instance data)
        qr_image = generate_qr(self.id) 
        
        #get the release identification information (with optional subclass information)
        #(i.e. per release data)
        release_image = release_subclass.get_tag();

        #get the instance details 
        #(i.e. per instance data)
        instance_image = self._generate_instance_tag(ReleaseSpecifics)

        return organize_tag(release_image, instance_image, qr_image)

    def _generate_instance_tag(self, ReleaseSpecifics):
        try:
            #get tag complement from the ReleaseSpecifics attached to this instance (i.e. per instance data)
            specifics = ReleaseSpecifics.objects.get(instance=self.id)
            specifics_image = specifics.get_tag();
        except AttributeError: #in case the release_subclass does not have specifics attached
            specifics_image = Image.new('RGB', (0, 0), 'white')

        try:
            #get tag complement from the InstanceParent (i.e. per instance data)
            parent_image = super(Instance, self).get_parent_tag()
        except AttributeError: #in case the custom InstanceParent does not define get_parent_tag()
            specifics_image = Image.new('RGB', (0, 0), 'white')

        spacing = 10
        size = (
            specifics_image.size[0] + parent_image.size[0] + spacing,
            max(specifics_image.size[1], parent_image.size[1])
        )        
        instance_image = Image.new('RGB', size, 'white')
        instance_image.paste(parent_image, (0, 0))
        instance_image.paste(specifics_image, (parent_image.size[0]+spacing, 0))
        return instance_image 

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

class AbstractSpecifics(models.Model):
    class Meta:
        abstract = True
    #unique to simulate one-to-one relationship
    instance = models.ForeignKey(Instance, unique=True)

    def __unicode__(self):
        return 'for :: ' + str(self.instance) 



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

class WorkingSpecifics(AbstractSpecifics):
    class Meta:
        abstract = True

    working = models.CharField(max_length=1, choices=WorkingState.CHOICES, default=WorkingState.UNKNOWN)

    def get_tag(self):
        work = 'work'

        text_size = get_textsize(work)

        side = 10
        spacing = 3 
        height = max(text_size[1], settings.TAG_INSTANCEDETAIL_HEIGHT)
        workingbox_img = Image.new('RGB', (text_size[0]+side+spacing, height), 'white')
        draw = ImageDraw.Draw(workingbox_img)

        draw.text([0, (height-text_size[1])/2], work, fill='black')
        up_left = (text_size[0]+spacing, (height-side)/2)
        #draw.rectangle documentation is too laconic, we are missing the right edge of the square if we do not substract 1 from its side because it seems that we are defining the two points on the outline
        down_right = (up_left[0] + side-1, up_left[1] + side-1) 
        draw.rectangle([up_left, down_right], outline='black')

        check_pos = (up_left[0]+2, up_left[1])
        if (self.working==WorkingState.YES):
            draw.text(check_pos, 'V', fill='green')
        elif (self.working==WorkingState.NO):
            draw.text(check_pos, 'X', fill='red')

        return workingbox_img
        

class ConsoleSpecifics(WorkingSpecifics):
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

    def get_tag_complement(self):
        return '[' + self.region + ']'
   
class GameSpecifics(WorkingSpecifics):
    pass

class Game(Release):
    class Dna:
        specifics = GameSpecifics
        category = Concept.Category.GAME 
        name_color = 'red'

    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    platform = models.ForeignKey(Platform)
    editor = models.ForeignKey(Company, blank=True, null=True)

class AccessorySpecifics(WorkingSpecifics):
    pass

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


