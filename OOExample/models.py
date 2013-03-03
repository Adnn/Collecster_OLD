from django.db import models

#An attribute is a name, that can be given a value at instance level.
class Attribute(models.Model):
    name = models.CharField(max_length=60)

    def __unicode__(self):
        return self.name

#A release can be compared to a class in OO : it's a data structure description (the attributes' list)
class Release(models.Model):
    name = models.CharField(max_length=60)
    #A release is caracterized by a list of attributes
    # the same attribute can be present in several releases
    attributes = models.ManyToManyField(Attribute, blank=True, null=True)

    def __unicode__(self):
        return self.name

#an instance entry can be compared to an object in OO : it instantiates a release, and can hold its own value for each of the attributes in this release. Actual attribute-value pairs for the instances are stored in the InstanceAttribute model.
#Nb : Attributes are all optional (an instance is not forced to 'store' an attribute even if it is present in the related release)
class Instance(models.Model):
    #the instantiated release
    release = models.ForeignKey(Release)

class InstanceAttribute(models.Model):
    instance = models.ForeignKey(Instance)
    attribute = models.ForeignKey(Attribute)
    value = models.CharField(max_length=60)

