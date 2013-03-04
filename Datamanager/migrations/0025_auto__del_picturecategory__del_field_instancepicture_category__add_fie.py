# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'PictureCategory'
        db.delete_table('Datamanager_picturecategory')

        # Deleting field 'InstancePicture.category'
        db.delete_column('Datamanager_instancepicture', 'category_id')

        # Adding field 'InstancePicture.subject'
        db.add_column('Datamanager_instancepicture', 'subject',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Attribute'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'InstancePicture.detail'
        db.add_column('Datamanager_instancepicture', 'detail',
                      self.gf('django.db.models.fields.CharField')(default=u'GRP', max_length=3),
                      keep_default=False)


    def backwards(self, orm):
        # Adding model 'PictureCategory'
        db.create_table('Datamanager_picturecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60, unique=True)),
        ))
        db.send_create_signal('Datamanager', ['PictureCategory'])

        # Adding field 'InstancePicture.category'
        db.add_column('Datamanager_instancepicture', 'category',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.PictureCategory'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'InstancePicture.subject'
        db.delete_column('Datamanager_instancepicture', 'subject_id')

        # Deleting field 'InstancePicture.detail'
        db.delete_column('Datamanager_instancepicture', 'detail')


    models = {
        'Datamanager.accessory': {
            'Meta': {'object_name': 'Accessory', '_ormbases': ['Datamanager.Release']},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'compatible_platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Platform']", 'symmetrical': 'False'}),
            'force_feedback': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'loose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'}),
            'tipe': ('django.db.models.fields.CharField', [], {'max_length': '3'})
        },
        'Datamanager.attributecategory': {
            'Meta': {'object_name': 'AttributeCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'Datamanager.bundle': {
            'Meta': {'object_name': 'Bundle'},
            'acquisition_date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.bundlecomposition': {
            'Meta': {'object_name': 'BundleComposition'},
            'bundle': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Bundle']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'})
        },
        'Datamanager.buying': {
            'Meta': {'object_name': 'Buying', '_ormbases': ['Datamanager.Bundle']},
            'bundle_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Bundle']", 'unique': 'True', 'primary_key': 'True'}),
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.BuyingContext']"}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Location']"}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        'Datamanager.buyingcontext': {
            'Meta': {'object_name': 'BuyingContext'},
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
            'constructor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Company']", 'null': 'True', 'blank': 'True'}),
            'implemented_platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Platform']", 'symmetrical': 'False'}),
            'loose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
        'Datamanager.donation': {
            'Meta': {'object_name': 'Donation', '_ormbases': ['Datamanager.Bundle']},
            'bundle_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Bundle']", 'unique': 'True', 'primary_key': 'True'}),
            'donator': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.User']"})
        },
        'Datamanager.game': {
            'Meta': {'object_name': 'Game', '_ormbases': ['Datamanager.Release']},
            'loose': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Platform']"}),
            'publisher': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Company']", 'null': 'True', 'blank': 'True'}),
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
            'add_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanciated_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'lastmodif_date': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'notes': ('django.db.models.fields.CharField', [], {'max_length': '180', 'blank': 'True'}),
            'origin': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'owner': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.User']"}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'}),
            'tag': ('django.db.models.fields.files.ImageField', [], {'max_length': '100', 'blank': 'True'})
        },
        'Datamanager.instanceattribute': {
            'Meta': {'object_name': 'InstanceAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Attribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'Datamanager.instancecomposition': {
            'Meta': {'object_name': 'InstanceComposition'},
            'container_instance': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'container_instance'", 'to': "orm['Datamanager.Instance']"}),
            'element_instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']", 'unique': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.instancepicture': {
            'Meta': {'object_name': 'InstancePicture'},
            'detail': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Instance']"}),
            'subject': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Attribute']", 'null': 'True', 'blank': 'True'})
        },
        'Datamanager.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.platform': {
            'Meta': {'object_name': 'Platform'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '20'})
        },
        'Datamanager.release': {
            'Meta': {'object_name': 'Release'},
            'attribute': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Attribute']", 'symmetrical': 'False', 'blank': 'True'}),
            'date': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'}),
            'realised_concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Concept']"}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        },
        'Datamanager.releasecomposition': {
            'Meta': {'object_name': 'ReleaseComposition'},
            'container_release': ('django.db.models.fields.related.ForeignKey', [], {'related_name': "'container_release'", 'to': "orm['Datamanager.Release']"}),
            'element_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        },
        'Datamanager.user': {
            'Meta': {'object_name': 'User'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['Datamanager']