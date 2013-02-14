# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Concept'
        db.create_table('Datamanager_concept', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('usual_name', self.gf('django.db.models.fields.CharField')(max_length=60)),
            ('complete_name', self.gf('django.db.models.fields.CharField')(max_length=180)),
        ))
        db.send_create_signal('Datamanager', ['Concept'])

        # Adding model 'ContentCategory'
        db.create_table('Datamanager_contentcategory', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['ContentCategory'])

        # Adding model 'Content'
        db.create_table('Datamanager_content', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('category', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.ContentCategory'])),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Content'])

        # Adding model 'Release'
        db.create_table('Datamanager_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('realised_concept', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Concept'])),
            ('specificity', self.gf('django.db.models.fields.CharField')(max_length=60, null=True, blank=True)),
        ))
        db.send_create_signal('Datamanager', ['Release'])

        # Adding M2M table for field content on 'Release'
        db.create_table('Datamanager_release_content', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['Datamanager.release'], null=False)),
            ('content', models.ForeignKey(orm['Datamanager.content'], null=False))
        ))
        db.create_unique('Datamanager_release_content', ['release_id', 'content_id'])

        # Adding M2M table for field nested_releases on 'Release'
        db.create_table('Datamanager_release_nested_releases', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('from_release', models.ForeignKey(orm['Datamanager.release'], null=False)),
            ('to_release', models.ForeignKey(orm['Datamanager.release'], null=False))
        ))
        db.create_unique('Datamanager_release_nested_releases', ['from_release_id', 'to_release_id'])

        # Adding model 'Concrete'
        db.create_table('Datamanager_concrete', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instanciated_release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['Datamanager.Release'])),
            ('price', self.gf('django.db.models.fields.FloatField')(blank=True)),
        ))
        db.send_create_signal('Datamanager', ['Concrete'])

        # Adding model 'Console'
        db.create_table('Datamanager_console', (
            ('release_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Datamanager.Release'], unique=True, primary_key=True)),
            ('version', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('Datamanager', ['Console'])

        # Adding model 'Game'
        db.create_table('Datamanager_game', (
            ('release_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['Datamanager.Release'], unique=True, primary_key=True)),
        ))
        db.send_create_signal('Datamanager', ['Game'])


    def backwards(self, orm):
        # Deleting model 'Concept'
        db.delete_table('Datamanager_concept')

        # Deleting model 'ContentCategory'
        db.delete_table('Datamanager_contentcategory')

        # Deleting model 'Content'
        db.delete_table('Datamanager_content')

        # Deleting model 'Release'
        db.delete_table('Datamanager_release')

        # Removing M2M table for field content on 'Release'
        db.delete_table('Datamanager_release_content')

        # Removing M2M table for field nested_releases on 'Release'
        db.delete_table('Datamanager_release_nested_releases')

        # Deleting model 'Concrete'
        db.delete_table('Datamanager_concrete')

        # Deleting model 'Console'
        db.delete_table('Datamanager_console')

        # Deleting model 'Game'
        db.delete_table('Datamanager_game')


    models = {
        'Datamanager.concept': {
            'Meta': {'object_name': 'Concept'},
            'complete_name': ('django.db.models.fields.CharField', [], {'max_length': '180'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'usual_name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.concrete': {
            'Meta': {'object_name': 'Concrete'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instanciated_release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Release']"}),
            'price': ('django.db.models.fields.FloatField', [], {'blank': 'True'})
        },
        'Datamanager.console': {
            'Meta': {'object_name': 'Console', '_ormbases': ['Datamanager.Release']},
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'}),
            'version': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.content': {
            'Meta': {'object_name': 'Content'},
            'category': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.ContentCategory']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.contentcategory': {
            'Meta': {'object_name': 'ContentCategory'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'Datamanager.game': {
            'Meta': {'object_name': 'Game', '_ormbases': ['Datamanager.Release']},
            'release_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['Datamanager.Release']", 'unique': 'True', 'primary_key': 'True'})
        },
        'Datamanager.release': {
            'Meta': {'object_name': 'Release'},
            'content': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['Datamanager.Content']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'nested_releases': ('django.db.models.fields.related.ManyToManyField', [], {'blank': 'True', 'related_name': "'nested_releases_rel_+'", 'null': 'True', 'to': "orm['Datamanager.Release']"}),
            'realised_concept': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['Datamanager.Concept']"}),
            'specificity': ('django.db.models.fields.CharField', [], {'max_length': '60', 'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['Datamanager']