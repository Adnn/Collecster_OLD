# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting model 'Content'
        db.delete_table('Datamanager_content')

        # Deleting model 'Concrete'
        db.delete_table('Datamanager_concrete')

        # Deleting model 'ContentCategory'
        db.delete_table('Datamanager_contentcategory')

        # Adding model 'AttributeCategory'
        db.create_table('Datamanager_attributecategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['AttributeCategory'])

        # Adding model 'Instance'
        db.create_table('Datamanager_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instanciated_release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Release'])),
            ('price', self.gf('django.db.models.fields.FloatField')(blank=True)),
        ))
        db.send_create_signal('Datamanager', ['Instance'])

        # Adding model 'Attribute'
        db.create_table('Datamanager_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.AttributeCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Attribute'])

        # Removing M2M table for field content on 'Release'
        db.delete_table('Datamanager_release_content')

        # Adding M2M table for field attribute on 'Release'
        db.create_table('Datamanager_release_attribute', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['Datamanager.release'], null=False)),
            ('attribute', models.ForeignKey(orm['Datamanager.attribute'], null=False))
        ))
        db.create_unique('Datamanager_release_attribute', ['release_id', 'attribute_id'])


        # Changing field 'Release.specificity'
        db.alter_column('Datamanager_release', 'specificity', self.gf('django.db.models.fields.CharField')(default='', max_length=60))

    def backwards(self, orm):
        # Adding model 'Content'
        db.create_table('Datamanager_content', (
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.ContentCategory'])),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Content'])

        # Adding model 'Concrete'
        db.create_table('Datamanager_concrete', (
            ('price', self.gf('django.db.models.fields.FloatField')(blank=True)),
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instanciated_release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Release'])),
        ))
        db.send_create_signal('Datamanager', ['Concrete'])

        # Adding model 'ContentCategory'
        db.create_table('Datamanager_contentcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['ContentCategory'])

        # Deleting model 'AttributeCategory'
        db.delete_table('Datamanager_attributecategory')

        # Deleting model 'Instance'
        db.delete_table('Datamanager_instance')

        # Deleting model 'Attribute'
        db.delete_table('Datamanager_attribute')

        # Adding M2M table for field content on 'Release'
        db.create_table('Datamanager_release_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['Datamanager.release'], null=False)),
            ('content', models.ForeignKey(orm['Datamanager.content'], null=False))
        ))
        db.create_unique('Datamanager_release_content', ['release_id', 'content_id'])

        # Removing M2M table for field attribute on 'Release'
        db.delete_table('Datamanager_release_attribute')


        # Changing field 'Release.specificity'
        db.alter_column('Datamanager_release', 'specificity', self.gf('django.db.models.fields.CharField')(max_length=60, null=True))

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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.concept': {
            'Meta': {'object_name': 'Concept'},
            'complete_name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usual_name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.console': {
            'Meta': {'object_name': 'Console', '_ormbases': ['Datamanager.Release']},
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.game': {
            'Meta': {'object_name': 'Game', '_ormbases': ['Datamanager.Release']},
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'})
        },
        'Datamanager.instance': {
            'Meta': {'object_name': 'Instance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanciated_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'Datamanager.release': {
            'Meta': {'object_name': 'Release'},
            'attribute': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Attribute']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nested_releases': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'nested_releases_rel_+'", 'blank': 'True', 'to': "orm['Datamanager.Release']"}),
            'realised_concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Concept']"}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '60', 'blank': 'True'})
        }
    }

    complete_apps = ['Datamanager']