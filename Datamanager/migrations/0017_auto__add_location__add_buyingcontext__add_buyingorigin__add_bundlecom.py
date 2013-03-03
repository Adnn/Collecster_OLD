# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Location'
        db.create_table('Datamanager_location', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('country', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('city', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Location'])

        # Adding model 'BuyingContext'
        db.create_table('Datamanager_buyingcontext', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['BuyingContext'])

        # Adding model 'BuyingOrigin'
        db.create_table('Datamanager_buyingorigin', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('location', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Location'])),
            ('context', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.BuyingContext'])),
        ))
        db.send_create_signal('Datamanager', ['BuyingOrigin'])

        # Adding model 'BundleComposition'
        db.create_table('Datamanager_bundlecomposition', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('bundle', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Bundle'])),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Instance'], unique=True)),
        ))
        db.send_create_signal('Datamanager', ['BundleComposition'])

        # Adding model 'Donation'
        db.create_table('Datamanager_donation', (
            ('bundle_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Datamanager.Bundle'], unique=True, primary_key=True)),
            ('donator', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.User'])),
        ))
        db.send_create_signal('Datamanager', ['Donation'])

        # Adding model 'Buying'
        db.create_table('Datamanager_buying', (
            ('bundle_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Datamanager.Bundle'], unique=True, primary_key=True)),
            ('price', self.gf('django.db.models.fields.FloatField')()),
            ('opportunity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.BuyingOrigin'])),
        ))
        db.send_create_signal('Datamanager', ['Buying'])

        # Adding model 'Bundle'
        db.create_table('Datamanager_bundle', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('acquisition_date', self.gf('django.db.models.fields.DateField')()),
        ))
        db.send_create_signal('Datamanager', ['Bundle'])

        # Adding model 'User'
        db.create_table('Datamanager_user', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['User'])

        # Adding field 'Console.constructor'
        db.add_column('Datamanager_console', 'constructor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Company'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Release.date'
        db.add_column('Datamanager_release', 'date',
                      self.gf('django.db.models.fields.DateField')(default=datetime.datetime(2013, 3, 3, 0, 0)),
                      keep_default=False)

        # Adding field 'Instance.notes'
        db.add_column('Datamanager_instance', 'notes',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=180, blank=True),
                      keep_default=False)

        # Adding field 'Instance.owner'
        db.add_column('Datamanager_instance', 'owner',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['Datamanager.User']),
                      keep_default=False)

        # Adding field 'Instance.add_date'
        db.add_column('Datamanager_instance', 'add_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, default=datetime.datetime(2013, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Adding field 'Instance.lastmodif_date'
        db.add_column('Datamanager_instance', 'lastmodif_date',
                      self.gf('django.db.models.fields.DateTimeField')(auto_now=True, default=datetime.datetime(2013, 3, 3, 0, 0), blank=True),
                      keep_default=False)

        # Deleting field 'Game.editor'
        db.delete_column('Datamanager_game', 'editor_id')

        # Adding field 'Game.publisher'
        db.add_column('Datamanager_game', 'publisher',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Company'], null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'Location'
        db.delete_table('Datamanager_location')

        # Deleting model 'BuyingContext'
        db.delete_table('Datamanager_buyingcontext')

        # Deleting model 'BuyingOrigin'
        db.delete_table('Datamanager_buyingorigin')

        # Deleting model 'BundleComposition'
        db.delete_table('Datamanager_bundlecomposition')

        # Deleting model 'Donation'
        db.delete_table('Datamanager_donation')

        # Deleting model 'Buying'
        db.delete_table('Datamanager_buying')

        # Deleting model 'Bundle'
        db.delete_table('Datamanager_bundle')

        # Deleting model 'User'
        db.delete_table('Datamanager_user')

        # Deleting field 'Console.constructor'
        db.delete_column('Datamanager_console', 'constructor_id')

        # Deleting field 'Release.date'
        db.delete_column('Datamanager_release', 'date')

        # Deleting field 'Instance.notes'
        db.delete_column('Datamanager_instance', 'notes')

        # Deleting field 'Instance.owner'
        db.delete_column('Datamanager_instance', 'owner_id')

        # Deleting field 'Instance.add_date'
        db.delete_column('Datamanager_instance', 'add_date')

        # Deleting field 'Instance.lastmodif_date'
        db.delete_column('Datamanager_instance', 'lastmodif_date')

        # Adding field 'Game.editor'
        db.add_column('Datamanager_game', 'editor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Company'], null=True, blank=True),
                      keep_default=False)

        # Deleting field 'Game.publisher'
        db.delete_column('Datamanager_game', 'publisher_id')


    models = {
        'Datamanager.accessory': {
            'Meta': {'object_name': 'Accessory', '_ormbases': ['Datamanager.Release']},
            'color': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'compatible_platforms': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Platform']", 'symmetrical': 'False'}),
            'force_feedback': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
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
            'opportunity': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.BuyingOrigin']"}),
            'price': ('django.db.models.fields.FloatField', [], {})
        },
        'Datamanager.buyingcontext': {
            'Meta': {'object_name': 'BuyingContext'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'})
        },
        'Datamanager.buyingorigin': {
            'Meta': {'object_name': 'BuyingOrigin'},
            'context': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.BuyingContext']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'location': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Location']"})
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
        'Datamanager.location': {
            'Meta': {'object_name': 'Location'},
            'city': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '60'}),
            'country': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
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
            'date': ('django.db.models.fields.DateField', [], {}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
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