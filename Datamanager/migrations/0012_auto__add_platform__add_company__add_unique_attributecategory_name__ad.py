# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Platform'
        db.create_table('Datamanager_platform', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=20)),
        ))
        db.send_create_signal('Datamanager', ['Platform'])

        # Adding model 'Company'
        db.create_table('Datamanager_company', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(unique=True, max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Company'])

        # Adding unique constraint on 'AttributeCategory', fields ['name']
        db.create_unique('Datamanager_attributecategory', ['name'])

        # Adding field 'Console.region'
        db.add_column('Datamanager_console', 'region',
                      self.gf('django.db.models.fields.CharField')(default='EU', max_length=2),
                      keep_default=False)

        # Adding field 'Console.color'
        db.add_column('Datamanager_console', 'color',
                      self.gf('django.db.models.fields.CharField')(default='BLK', max_length=3),
                      keep_default=False)

        # Adding M2M table for field implemented_platforms on 'Console'
        db.create_table('Datamanager_console_implemented_platforms', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('console', models.ForeignKey(orm['Datamanager.console'], null=False)),
            ('platform', models.ForeignKey(orm['Datamanager.platform'], null=False))
        ))
        db.create_unique('Datamanager_console_implemented_platforms', ['console_id', 'platform_id'])


        # Changing field 'Console.version'
        db.alter_column('Datamanager_console', 'version', self.gf('django.db.models.fields.CharField')(max_length=20, null=True))
        # Deleting field 'Concept.usual_name'
        db.delete_column('Datamanager_concept', 'usual_name')

        # Adding field 'Concept.common_name'
        db.add_column('Datamanager_concept', 'common_name',
                      self.gf('django.db.models.fields.CharField')(default='rename_me', unique=True, max_length=60),
                      keep_default=False)

        # Adding field 'Concept.company'
        db.add_column('Datamanager_concept', 'company',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Company'], null=True, blank=True),
                      keep_default=False)

        # Adding field 'Concept.category'
        db.add_column('Datamanager_concept', 'category',
                      self.gf('django.db.models.fields.CharField')(default='CONSOLE', max_length=20),
                      keep_default=False)


        # Changing field 'Concept.complete_name'
        db.alter_column('Datamanager_concept', 'complete_name', self.gf('django.db.models.fields.CharField')(max_length=180, unique=True, null=True))
        # Adding unique constraint on 'Concept', fields ['complete_name']
        db.create_unique('Datamanager_concept', ['complete_name'])

        # Adding field 'Game.region'
        db.add_column('Datamanager_game', 'region',
                      self.gf('django.db.models.fields.CharField')(default='EU', max_length=2),
                      keep_default=False)

        # Adding field 'Game.platform'
        db.add_column('Datamanager_game', 'platform',
                      self.gf('django.db.models.fields.related.ForeignKey')(default=1, to=orm['Datamanager.Platform']),
                      keep_default=False)

        # Adding field 'Game.editor'
        db.add_column('Datamanager_game', 'editor',
                      self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Company'], null=True, blank=True),
                      keep_default=False)

        # Adding unique constraint on 'PictureCategory', fields ['name']
        db.create_unique('Datamanager_picturecategory', ['name'])

        # Deleting field 'ConsoleSpecifics.modded'
        db.delete_column('Datamanager_consolespecifics', 'modded')

        # Adding field 'ConsoleSpecifics.working'
        db.add_column('Datamanager_consolespecifics', 'working',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ConsoleSpecifics.region_modded'
        db.add_column('Datamanager_consolespecifics', 'region_modded',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Adding field 'ConsoleSpecifics.copy_modded'
        db.add_column('Datamanager_consolespecifics', 'copy_modded',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Removing unique constraint on 'PictureCategory', fields ['name']
        db.delete_unique('Datamanager_picturecategory', ['name'])

        # Removing unique constraint on 'Concept', fields ['complete_name']
        db.delete_unique('Datamanager_concept', ['complete_name'])

        # Removing unique constraint on 'AttributeCategory', fields ['name']
        db.delete_unique('Datamanager_attributecategory', ['name'])

        # Deleting model 'Platform'
        db.delete_table('Datamanager_platform')

        # Deleting model 'Company'
        db.delete_table('Datamanager_company')

        # Deleting field 'Console.region'
        db.delete_column('Datamanager_console', 'region')

        # Deleting field 'Console.color'
        db.delete_column('Datamanager_console', 'color')

        # Removing M2M table for field implemented_platforms on 'Console'
        db.delete_table('Datamanager_console_implemented_platforms')


        # Changing field 'Console.version'
        db.alter_column('Datamanager_console', 'version', self.gf('django.db.models.fields.CharField')(default='1', max_length=60))
        # Adding field 'Concept.usual_name'
        db.add_column('Datamanager_concept', 'usual_name',
                      self.gf('django.db.models.fields.CharField')(default='rename_me', max_length=60),
                      keep_default=False)

        # Deleting field 'Concept.common_name'
        db.delete_column('Datamanager_concept', 'common_name')

        # Deleting field 'Concept.company'
        db.delete_column('Datamanager_concept', 'company_id')

        # Deleting field 'Concept.category'
        db.delete_column('Datamanager_concept', 'category')


        # Changing field 'Concept.complete_name'
        db.alter_column('Datamanager_concept', 'complete_name', self.gf('django.db.models.fields.CharField')(default='rename', max_length=180))
        # Deleting field 'Game.region'
        db.delete_column('Datamanager_game', 'region')

        # Deleting field 'Game.platform'
        db.delete_column('Datamanager_game', 'platform_id')

        # Deleting field 'Game.editor'
        db.delete_column('Datamanager_game', 'editor_id')

        # Adding field 'ConsoleSpecifics.modded'
        db.add_column('Datamanager_consolespecifics', 'modded',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'ConsoleSpecifics.working'
        db.delete_column('Datamanager_consolespecifics', 'working')

        # Deleting field 'ConsoleSpecifics.region_modded'
        db.delete_column('Datamanager_consolespecifics', 'region_modded')

        # Deleting field 'ConsoleSpecifics.copy_modded'
        db.delete_column('Datamanager_consolespecifics', 'copy_modded')


    models = {
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
            'working': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        'Datamanager.game': {
            'Meta': {'object_name': 'Game', '_ormbases': ['Datamanager.Release']},
            'editor': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Company']", 'null': 'True', 'blank': 'True'}),
            'platform': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Platform']"}),
            'region': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'})
        },
        'Datamanager.instance': {
            'Meta': {'object_name': 'Instance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanciated_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'price': ('django.db.models.fields.FloatField', [], {'null': 'True', 'blank': 'True'})
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