# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Instance.tag'
        db.add_column('Datamanager_instance', 'tag',
                      self.gf('django.db.models.fields.files.ImageField')(default='', max_length=100, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Instance.tag'
        db.delete_column('Datamanager_instance', 'tag')


    models = {
        'Datamanager.accessory': {
            'Meta': {'object_name': 'Accessory', '_ormbases': ['Datamanager.Release']},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'compatible_platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Platform']", 'symmetrical': 'False'}),
            'force_feedback': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'}),
            'rumble_feedback': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'wireless': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'Datamanager.accessoryspecifics': {
            'Meta': {'object_name': 'AccessorySpecifics'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'}),
            'working': ('django.db.models.fields.CharField', [], {'default': "u'?'", 'max_length': '1'})
        },
        'Datamanager.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.AttributeCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.attributecategory': {
            'Meta': {'object_name': 'AttributeCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'Datamanager.company': {
            'Meta': {'object_name': 'Company'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'Datamanager.concept': {
            'Meta': {'object_name': 'Concept'},
            'category': ('django.db.models.fields.CharField', [], {'max_length': '20'}),
            'common_name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'company': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Company']", 'null': 'True', 'blank': 'True'}),
            'complete_name': ('django.db.models.fields.CharField', [], {'max_length': '180', 'unique': 'True', 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.console': {
            'Meta': {'object_name': 'Console', '_ormbases': ['Datamanager.Release']},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'implemented_platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Platform']", 'symmetrical': 'False'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'})
        },
        'Datamanager.consolespecifics': {
            'Meta': {'object_name': 'ConsoleSpecifics'},
            'copy_modded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'}),
            'region_modded': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'working': ('django.db.models.fields.CharField', [], {'default': "u'?'", 'max_length': '1'})
        },
        'Datamanager.game': {
            'Meta': {'object_name': 'Game', '_ormbases': ['Datamanager.Release']},
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Company']", 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Platform']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'})
        },
        'Datamanager.gamespecifics': {
            'Meta': {'object_name': 'GameSpecifics'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'}),
            'working': ('django.db.models.fields.CharField', [], {'default': "u'?'", 'max_length': '1'})
        },
        'Datamanager.instance': {
            'Meta': {'object_name': 'Instance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanciated_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'Datamanager.instanceattribute': {
            'Meta': {'object_name': 'InstanceAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Attribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.instancecomposition': {
            'Meta': {'object_name': 'InstanceComposition'},
            'container_instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'container_instance'", 'to': "orm['Datamanager.Instance']"}),
            'element_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.instancepicture': {
            'Meta': {'object_name': 'InstancePicture'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.PictureCategory']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']"})
        },
        'Datamanager.picturecategory': {
            'Meta': {'object_name': 'PictureCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'Datamanager.platform': {
            'Meta': {'object_name': 'Platform'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'Datamanager.release': {
            'Meta': {'object_name': 'Release'},
            'attribute': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Attribute']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'realised_concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Concept']"}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'Datamanager.releasecomposition': {
            'Meta': {'object_name': 'ReleaseComposition'},
            'container_release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'container_release'", 'to': "orm['Datamanager.Release']"}),
            'element_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['Datamanager']