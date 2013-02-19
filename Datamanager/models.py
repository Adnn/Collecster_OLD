from django.db import models
from model_utils.managers import InheritanceManager


class Concept(models.Model):
    usual_name = models.CharField(max_length=60)
    complete_name = models.CharField(max_length=180)

    def __unicode__(self):
        return self.usual_name

class AttributeCategory(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Attribute(models.Model):
    category = models.ForeignKey(AttributeCategory)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u'['+self.category.name+"] "+self.name

class Release(models.Model):
    realised_concept = models.ForeignKey(Concept)
    specificity = models.CharField(max_length=60, blank=True)
    attribute = models.ManyToManyField(Attribute, blank=True)
    objects = InheritanceManager()

    def __unicode__(self):
        return self.realised_concept.usual_name

class ReleaseComposition(models.Model):
    container_release = models.ForeignKey(Release, related_name="container_release")
    element_release = models.ForeignKey(Release)

class Instance(models.Model):
    instanciated_release = models.ForeignKey(Release)
    price = models.FloatField(blank=True, null=True)

    def __unicode__(self):
        return str(self.id)+' '+str(self.instanciated_release)

class PictureCategory(models.Model):
    name = models.CharField(max_length=60)

def name_picture(instance_picture, filename):
    #The instance picture related instance has already been saved to the DB when we save the instance picture
    path = 'instances_pictures/' + str(instance_picture.instance.id) + '/' + filename 
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
    element_instance = models.ForeignKey(Instance)

# Application specific code starts here 
class Console(Release):
    version = models.CharField(max_length=60)

    def __unicode__(self):
        return '[console] ' + str(self.id) + " " + super(Console, self).__unicode__()
   
class Game(Release):
    region = (
        (u'EU', u'Europe'),
        (u'US', u'USA'),
        (u'JP', u'Japan'),
    )
     
