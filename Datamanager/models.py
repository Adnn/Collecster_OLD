from django.db import models
from model_utils.managers import InheritanceManager
from django.forms import widgets

import qrcode
from PIL import Image, ImageDraw, ImageFont

import os

from Datamanager import stringer
from Datamanager import settings


#Global fonts
font_title = ImageFont.truetype(settings.TAG_FONT_TITLE, settings.TAG_FONT_TITLESIZE)
font_detail = ImageFont.truetype(settings.TAG_FONT_DETAIL, settings.TAG_FONT_DETAILSIZE)
font_checksign = ImageFont.truetype(settings.TAG_FONT_CHECKSIGN, settings.TAG_FONT_CHECKSIGNSIZE)

def get_instance_mediapath(instance):
    return os.path.join(settings.PATH_MEDIA_INSTANCES, str(instance.id))

def name_picture(instance_picture, filename):
    #The instance picture related instance has already been saved to the DB when we save the instance picture
    return os.path.join(get_instance_mediapath(instance_picture.instance), filename)

def name_tag(instance, filename=None):
    return os.path.join(
        get_instance_mediapath(instance), 
        settings.PATH_TAGFILE
    )


def generate_qr(id, object_typename=None):
    qr = qrcode.QRCode(
        box_size = settings.TAG_QR_BOXSIZE,
    )

    qrdata = ''
    if(object_typename):
        qrdata += object_typename + '/'
    qrdata += str(id)
    qr.add_data(qrdata)

    return qr.make_image()._img

def get_textsize(text, font):
    return font.getsize(text)

def get_titlesize(text):
    return get_textsize(text, font_title)

# \todo : implement a nice layout system instead of hardcoded positions (like flows in html  ; )
""" Organize the final aspect of the printed tag (in a rather rigid way).
The layout is divided in two columns.
Takes: -a release_img (generic info about the release) and put it at the top of the left column.
        -an instance_img (specific info about this instance) and put it at the bottom of the left columng.
        -a qr_img and put it at the top of the right column.""" 
def organize_tag(release_img, instance_img, qr_img, border=True):
    
    if border:
        border_size = 1
    else:
        border_size = 0

    left_width = max(
        release_img.size[0],
        instance_img.size[0],
        settings.TAG_MIN_COLS*get_textsize('_', font_title)[0]
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

#
# Custom models
#
class Company(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name

class Subtype:
    class Category:
        CONSOLE = u'CONSOLE'
        GAME = u'GAME'
        ACCESSORY = u'ACCESSORY'

    CONSOLE = Category.CONSOLE 
    GAME = Category.GAME
    
    ANALOG_PAD = u'ANALOG_PAD'
    BATTERY = u'BATTERY'
    CAMERA = u'CAMERA'
    COVER = u'COVER'
    DANCEMAT = u'DANCEMAT'
    DRUM = u'DRUM'
    FISHING_ROD = u'FISHING_ROD'
    GESTURE_RECO = u'GESTURE_RECO'
    GUITAR = u'GUITAR'
    GUN = u'GUN'
    HEADPHONES = u'HEADPHONES'
    JOYSTICK = u'JOYSTICK'
    KEYBOARD = u'KEYBOARD'
    MAGNIFIER = u'MAGNIFIER'
    MEMORYCARD = u'MEMORYCARD'
    MODEM = u'MODEM'
    MOUSE = u'MOUSE'
    MULTITAP = u'MULTITAP'
    PAD = u'PAD'
    PAD_CHARGER = u'PAD_CHARGER'
    SPEAKERS = u'SPEAKERS'
    STEERINGWHEEL = u'STEERINGWHEEL'
    STEREOGLASSES = u'STEREOGLASSES'
    TURNTABLE = u'TURNTABLE'

    DICT = {
        CONSOLE : ('Console', Category.CONSOLE),
        GAME : ('Game', Category.GAME),

        ANALOG_PAD : ('Analog pad', Category.ACCESSORY),
        BATTERY : ('Battery', Category.ACCESSORY),
        CAMERA : ('Camera', Category.ACCESSORY),
        COVER : ('Cover', Category.ACCESSORY),
        DANCEMAT : ('Dancemat', Category.ACCESSORY),
        DRUM : ('Drum', Category.ACCESSORY),
        FISHING_ROD : ('Fishing rod', Category.ACCESSORY),
        GESTURE_RECO : ('Gesture', Category.ACCESSORY),
        GUITAR : ('Guitar', Category.ACCESSORY),
        GUN : ('Gun', Category.ACCESSORY),
        HEADPHONES : ('Headphones', Category.ACCESSORY),
        JOYSTICK : ('Joystick', Category.ACCESSORY),
        KEYBOARD : ('Keyboard', Category.ACCESSORY),
        MAGNIFIER : ('Magnifier', Category.ACCESSORY),
        MEMORYCARD : ('Memorycard', Category.ACCESSORY),
        MODEM : ('Modem', Category.ACCESSORY),
        MOUSE : ('Mouse', Category.ACCESSORY),
        MULTITAP : ('Multitap', Category.ACCESSORY),
        PAD : ('Pad', Category.ACCESSORY),
        PAD_CHARGER : ('Pad charger', Category.ACCESSORY),
        SPEAKERS : ('Speakers', Category.ACCESSORY),
        STEERINGWHEEL : ('Steeringwheel', Category.ACCESSORY),
        STEREOGLASSES : ('Stereoglasses', Category.ACCESSORY),
        TURNTABLE : ('Turntable', Category.ACCESSORY),
     }

    @classmethod
    def get_choices(cls):
        accessories = []
        others = []
        for key, value in cls.DICT.items():
            if value[1]==cls.Category.ACCESSORY:
                accessories.append((key, value[0]))
            else:
                others.append((key, value[0]))
        return tuple(others) + (('Accessory', tuple(accessories)),)
         
class Concept(models.Model):
    common_name = models.CharField(max_length=60, unique=True)
    complete_name = models.CharField(max_length=180, unique=True, blank=True, null=True)

    company = models.ForeignKey(Company, blank=True, null=True)
    category = models.CharField(max_length=20, choices=Subtype.get_choices())

    def __unicode__(self):
        return self.common_name

    
#crazy Python does not allow to call a class method (or static method) inside the class defining it, so get_choices has to be defined outside (and before) InstanceParent, and still see ORIGIN_DICT.
#a default method (without self) would not be able to see the static dict at all.
class Origin():
    ORIGINAL = u'OR'
    BUY_USAGE = u'BU'
    BUY_COLLEC = u'BC'
    #For lost/stolen original elements...
    BUY_AGAIN = u'BA'
    GIFT = u'GF'

#element :    key(=value to be stored in DB) : (web display value, tag spot color)
    ORIGIN_DICT = {
        ORIGINAL : (u'Original', 'green'),
        BUY_USAGE : (u'Buy usage', 'blue'),
        BUY_COLLEC : (u'Buy collection', 'red'),
        BUY_AGAIN : (u'Buy back', 'yellow'),
        GIFT : (u'Gift', 'pink'),
    }

    @classmethod
    def get_choices(cls):
        return [(key, value[0]) for key, value in cls.ORIGIN_DICT.items()]


class InstanceParent(models.Model):
    class Meta:
        abstract = True

    price = models.FloatField(blank=True, null=True)
    origin = models.CharField(max_length=2, choices=Origin.get_choices())
    notes = models.CharField(max_length=180, blank=True)

    def get_parent_tag(self):
        side = settings.TAG_INSTANCEDETAIL_HEIGHT
        diameter = side/2
        padding = (side-diameter)/2

        ellipse_bbox = [padding, padding, padding+diameter, padding+diameter]
        fill_color = Origin.ORIGIN_DICT[self.origin][1]
        sample_factor = settings.TAG_SUPERSAMPLE_FACTOR

        supersize = sample_factor * side
        supersampled = Image.new('RGB', (supersize, supersize), 'white')
        superdraw = ImageDraw.Draw(supersampled)
        superdraw.ellipse(map((lambda x: x*sample_factor), ellipse_bbox), fill=fill_color)

        parent_image = supersampled.resize((side, side), Image.ANTIALIAS)
        return parent_image

#Generic models
class AttributeType:
    RATING = u'RTG'
    RATING_NULL = u'RTN'
    PRESENCE  = u'PRS'

    RATING_CHOICES = (
        (u'M', u'Mint'),
        (u'A', u'A'),
        (u'B', u'B'),
        (u'C', u'C'),
        (u'D', u'D'),
        (u'E', u'E'),
    )

    RATING_NULL_CHOICES = ((u'', u'---'),) + RATING_CHOICES

    DICT = {
        RATING : (u'Rating', (widgets.Select, {'choices':RATING_CHOICES,}) ),
        RATING_NULL : (u'Rating w/ null', (widgets.Select, {'choices':RATING_NULL_CHOICES,}) ),
        PRESENCE : (u'Presence', (widgets.CheckboxInput, None) ),
    }
    
    @classmethod
    def get_choices(cls):
        return [(key, value[0]) for key, value in cls.DICT.items()]

    @classmethod
    def get_class_and_options(cls, attribute_type):
        value = cls.DICT[attribute_type][1]
        return value[0], value[1]

class AttributeCategory(models.Model):
    name = models.CharField(max_length=60, unique=True)

    def __unicode__(self):
        return self.name

class Attribute(models.Model):
    class Meta:
        ordering = ('category', 'name')
    category = models.ForeignKey(AttributeCategory)
    name = models.CharField(max_length=60)
    tipe = models.CharField(max_length=3, choices=AttributeType.get_choices())

    def __unicode__(self):
        return u'['+self.category.name+'] '+self.name

class Release(models.Model):
    realised_concept = models.ForeignKey(Concept)
    name = models.CharField(max_length=60, blank=True)
    date = models.DateField(blank=True, null=True)
    specificity_text = models.CharField(max_length=60, blank=True)
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
        name_width = reduce(max, [width for width, height in map(get_titlesize, name_lines)])
        name_height = reduce(add, [height for width, height in map(get_titlesize, name_lines)])
        complement = self.get_tag_complement()
        if complement:
            complement_size = get_textsize(complement, font_detail)
        else:
            complement_size = (0, 0)

        left_pad = settings.TAG_TEXT_BORDER_PAD
        release_img = Image.new('RGB', (max(name_width, complement_size[0])+left_pad, name_height+complement_size[1]), 'white')
        release_draw = ImageDraw.Draw(release_img)

        offset = 0
        for name_part in name_lines:
            release_draw.text((left_pad, offset), name_part, font=font_title, fill=name_color)
            offset += release_draw.textsize(name_part, font=font_title)[1]

        if complement:
            release_draw.text((left_pad, offset), complement, font=font_title, fill='black')

        return release_img

    """ An empty method in case the release subclass does not override it """
    # \return : string complement information
    def get_tag_complement(self):
        return

class ReleaseComposition(models.Model):
    container_release = models.ForeignKey(Release, related_name="container_release")
    element_release = models.ForeignKey(Release)

class Specificity(models.Model):
    name = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        return self.name
     
class SpecificityComposition(models.Model):
    specificity = models.ForeignKey(Specificity)
    release = models.ForeignKey(Release)
    value = models.CharField(max_length=60)
    
class Person(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Instance(InstanceParent):
    instanciated_release = models.ForeignKey(Release)
    tag = models.ImageField(upload_to=name_tag, blank=True)

    owner = models.ForeignKey(Person)
    add_date = models.DateTimeField(auto_now_add=True)
    lastmodif_date = models.DateTimeField(auto_now=True)

    def __unicode__(self):
        return str(self.id)+' '+str(self.instanciated_release)

    def generate_tag(self):
        release_subclass = Release.objects.get_subclass(id=self.instanciated_release.id)
        ReleaseSpecifics = type(release_subclass).Dna.specifics
        #generate the qrcode base on Instance.id (i.e. per instance data)
        qr_image = generate_qr(self.id, type(self).__name__.lower()) 
        
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

        idtext = str(self.id).rjust(settings.TAG_ID_LEFTPADDING_CHARS)
        idtext_size = get_textsize(idtext, font_detail) 

        spacing = settings.TAG_INSTANCEDATA_SPACING 
        size = (
            specifics_image.size[0] + parent_image.size[0] + spacing + idtext_size[0] + spacing,
            max(specifics_image.size[1], parent_image.size[1], idtext_size[1])
        )        
        instance_image = Image.new('RGB', size, 'white')
        draw = ImageDraw.Draw(instance_image)
        instance_image.paste(parent_image, (0, 0))
        instance_image.paste(specifics_image, (parent_image.size[0]+spacing, 0))
        draw.text(
                (specifics_image.size[0] + spacing + parent_image.size[0] + spacing,
                (max(idtext_size[1], settings.TAG_INSTANCEDETAIL_HEIGHT)-idtext_size[1])/2),
            idtext,
            font = font_detail,
            fill='black',)

        return instance_image 

class PictureDetail():
    GROUP = u'GRP'
    FRONT = u'FRT'
    BACK = u'BCK'
    SIDE = u'SID'
    SIDE_LABEL = u'SLB'
    INSIDE = u'INS'

    DICT = {
        GROUP : (u'Group',),
        FRONT : (u'Front',),
        BACK : (u'Back',),
        SIDE : (u'Side',),
        SIDE_LABEL : (u'Side label',),
        INSIDE : (u'Inside',),
    }

    @classmethod
    def get_choices(cls):
        return [(key, value[0]) for key, value in cls.DICT.items()]

class InstancePicture(models.Model):
    instance = models.ForeignKey(Instance)
    image = models.ImageField(upload_to=name_picture)
    attribute = models.ForeignKey(Attribute, blank=True, null=True)
    detail = models.CharField(max_length=3, choices=PictureDetail.get_choices(), blank=False, default=PictureDetail.GROUP)

class InstanceAttribute(models.Model):
    instance = models.ForeignKey(Instance)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=60, blank=True)

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


#
# Application specific code 
#
class Bundle(models.Model):
    acquisition_date = models.DateField()

    objects = InheritanceManager()

class Country:
    LITHUANIA = u'LT'
    FRANCE = u'FR'
    GERMANY = u'DE'
    ITALY = u'IT'
    JAPAN = u'JP'
    SPAIN = u'ES'
    UK = u'UK'
    USA = u'US'
    
    CHOICES = (
        (u'Europe', 
            ((LITHUANIA, u'Lithuania'),
            (FRANCE, u'France'),
            (GERMANY, u'Germany'),
            (ITALY, u'Italy'),
            (SPAIN, u'Spain'),)
        ),
        (JAPAN, u'Japan'),
        (UK, u'UK'),
        (USA, u'USA'),
    )
        
class Location(models.Model):
    country = models.CharField(max_length=2, choices=Country.CHOICES)
    city = models.CharField(max_length=60, unique=True, blank=True)

    def __unicode__(self):
        return '['+self.country+'] ' + self.city

class BuyingContextCategory:
    INTERNET = u'NET'
    SHOP = u'SHP'
    SECONDHAND = u'SEC' 
    
    DICT = {
        INTERNET : (u'Internet',),
        SHOP : (u'Shop',),
        SECONDHAND : (u'Secondhand trade',),
    }

    @classmethod
    def get_choices(cls):
        return [(key, value[0]) for key, value in cls.DICT.items()]

class BuyingContext(models.Model):
    category = models.CharField(max_length=3, choices=BuyingContextCategory.get_choices())
    name = models.CharField(max_length=60)
    location = models.ForeignKey(Location, blank=True, null=True)
    complement = models.CharField(max_length=60, blank=True)

    def __unicode__(self):
        value = self.name
        if self.complement:
            value += ' ' + complement
        if self.location:
            value += ', ' + str(self.location)
        return value

class Buying(Bundle):
    price = models.FloatField()
    shipping_cost = models.FloatField(blank=True, null=True)
    location = models.ForeignKey(Location, blank=True, null=True)
    context = models.ForeignKey(BuyingContext)

    def __unicode__(self):
        return str(self.acquisition_date) + ' ' + str(self.context)

class Donation(Bundle):
    donator = models.ForeignKey(Person)

class BundleComposition(models.Model):
    bundle = models.ForeignKey(Bundle)
    instance = models.ForeignKey(Instance, unique=True)

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
    GREEN = u'GRN'
    BLUE = u'BLU'
    YELLOW = u'YEL'
    ORANGE = u'ORA'
    PINK = u'PIN'
    BROWN = u'BRO'
    PURPLE = u'PUR'

    GOLD = u'GLD'
    SILVER = u'SIL'

    CHOICES = (
        (BLACK, u'Black'),
        (WHITE, u'White'),
        (GREY, u'Grey'),
        (RED, u'Red'),
        (GREEN, u'Green'),
        (BLUE, u'Blue'),
        (YELLOW, u'Yellow'),
        (ORANGE, u'Orange'),
        (PINK, u'Pink'),
        (BROWN, u'Brown'),
        (PURPLE, u'Purple'),

        (GOLD, u'Gold'),
        (SILVER, u'Silver'),
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
        work = settings.STR_WORK

        text_size = get_textsize(work, font_detail)

        side = settings.TAG_CHECKBOX_SIDE
        spacing = settings.TAG_TEXT_BORDER_PAD 
        height = max(text_size[1], settings.TAG_INSTANCEDETAIL_HEIGHT)
        workingbox_img = Image.new('RGB', (text_size[0]+side+spacing, height), 'white')
        draw = ImageDraw.Draw(workingbox_img)

        draw.text([0, (height-text_size[1])/2], work, font=font_detail, fill='black')
        up_left = (text_size[0]+spacing, (height-side)/2)
        #draw.rectangle documentation is too laconic, we are missing the right edge of the square if we do not substract 1 from its side because it seems that we are defining the two points on the outline
        down_right = (up_left[0] + side-1, up_left[1] + side-1) 
        draw.rectangle([up_left, down_right], outline='black')

        check_pos = (
            up_left[0]+settings.TAG_CHECKSIGN_PAD[0],
            up_left[1] + settings.TAG_CHECKSIGN_PAD[1])

        if (self.working==WorkingState.YES):
            draw.text(check_pos, 'V', font=font_checksign, fill='green')
        elif (self.working==WorkingState.NO):
            draw.text(check_pos, 'X', font=font_checksign, fill='red')

        return workingbox_img
        

class ConsoleSpecifics(WorkingSpecifics):
    region_modded = models.BooleanField()
    copy_modded = models.BooleanField()

class Console(Release):
    class Dna:
        specifics = ConsoleSpecifics
        category = Subtype.Category.CONSOLE
        name_color = u'red'

    loose = models.BooleanField()
    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    color = models.CharField(max_length=3, choices=Color.CHOICES) 
    implemented_platforms = models.ManyToManyField(Platform)

    version = models.CharField(max_length=20, blank=True, null=True)
    constructor = models.ForeignKey(Company, blank=True, null=True)

    def __unicode__(self):
        return '[console] ' + str(self.id) + " " + super(Console, self).__unicode__()

    def get_tag_complement(self):
        return '[' + self.region + ']'
   
class GameSpecifics(WorkingSpecifics):
    pass

class Game(Release):
    class Dna:
        specifics = GameSpecifics
        category = Subtype.Category.GAME 
        name_color = u'green'

    loose = models.BooleanField()
    region = models.CharField(max_length=2, choices=Region.CHOICES) 
    platform = models.ForeignKey(Platform)
    publisher = models.ForeignKey(Company, blank=True, null=True)

class AccessorySpecifics(WorkingSpecifics):
    pass

class Accessory(Release):
    class Dna:
        specifics = AccessorySpecifics
        category = Subtype.Category.ACCESSORY
        name_color = u'blue'

    loose = models.BooleanField()
    region = models.CharField(max_length=2, choices=Region.CHOICES, blank=True) 
    color = models.CharField(max_length=3, choices=Color.CHOICES) 
    compatible_platforms = models.ManyToManyField(Platform)

    wireless = models.BooleanField()
    force_feedback = models.BooleanField()
    rumble_feedback = models.BooleanField()
