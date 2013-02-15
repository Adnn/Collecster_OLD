from django.db import models

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

    def __unicode__(self):
        return self.realised_concept.usual_name

class ReleaseComposition(models.Model):
    container_release = models.ForeignKey(Release, related_name="container_release")
    element_release = models.ForeignKey(Release)

class Instance(models.Model):
    instanciated_release = models.ForeignKey(Release)
    price = models.FloatField(blank=True)

    def __unicode__(self):
        return str(self.id)+' '+str(self.instanciated_release)

class InstanceAttribute(models.Model):
    instance = models.ForeignKey(Instance)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=60)

# Application specific code starts here 
class Console(Release):
    version = models.CharField(max_length=60)
   
class Game(Release):
    region = (
        (u'EU', u'Europe'),
        (u'US', u'USA'),
        (u'JP', u'Japan'),
    )
     
