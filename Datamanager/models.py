from django.db import models

class Concept(models.Model):
    usual_name = models.CharField(max_length=60)
    complete_name = models.CharField(max_length=180)

    def __unicode__(self):
        return self.usual_name

class ContentCategory(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

class Content(models.Model):
    category = models.ForeignKey(ContentCategory)
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return u'['+self.category.name+"] "+self.name

class Release(models.Model):
    realised_concept = models.ForeignKey(Concept)
    specificity = models.CharField(max_length=60, blank=True)
    content = models.ManyToManyField(Content, blank=True)
    nested_releases = models.ManyToManyField('self', blank=True)

    def __unicode__(self):
        return self.realised_concept.usual_name

class Concrete(models.Model):
    instanciated_release = models.ForeignKey(Release)
    price = models.FloatField(blank=True)


# Application specific code starts here 
class Console(Release):
    version = models.CharField(max_length=60)
   
class Game(Release):
    region = (
        (u'EU', u'Europe'),
        (u'US', u'USA'),
        (u'JP', u'Japan'),
    )
     
