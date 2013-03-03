# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Attribute'
        db.create_table('OOExample_attribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('OOExample', ['Attribute'])

        # Adding model 'Release'
        db.create_table('OOExample_release', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
        ))
        db.send_create_signal('OOExample', ['Release'])

        # Adding M2M table for field attrbutes on 'Release'
        db.create_table('OOExample_release_attrbutes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['OOExample.release'], null=False)),
            ('attribute', models.ForeignKey(orm['OOExample.attribute'], null=False))
        ))
        db.create_unique('OOExample_release_attrbutes', ['release_id', 'attribute_id'])

        # Adding model 'Instance'
        db.create_table('OOExample_instance', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('release', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OOExample.Release'])),
        ))
        db.send_create_signal('OOExample', ['Instance'])

        # Adding model 'InstanceAttribute'
        db.create_table('OOExample_instanceattribute', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('instance', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OOExample.Instance'])),
            ('attribute', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['OOExample.Attribute'])),
            ('value', self.gf('django.db.models.fields.CharField')(max_length=60)),
        ))
        db.send_create_signal('OOExample', ['InstanceAttribute'])


    def backwards(self, orm):
        # Deleting model 'Attribute'
        db.delete_table('OOExample_attribute')

        # Deleting model 'Release'
        db.delete_table('OOExample_release')

        # Removing M2M table for field attrbutes on 'Release'
        db.delete_table('OOExample_release_attrbutes')

        # Deleting model 'Instance'
        db.delete_table('OOExample_instance')

        # Deleting model 'InstanceAttribute'
        db.delete_table('OOExample_instanceattribute')


    models = {
        'OOExample.attribute': {
            'Meta': {'object_name': 'Attribute'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'OOExample.instance': {
            'Meta': {'object_name': 'Instance'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'release': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OOExample.Release']"})
        },
        'OOExample.instanceattribute': {
            'Meta': {'object_name': 'InstanceAttribute'},
            'attribute': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OOExample.Attribute']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'instance': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['OOExample.Instance']"}),
            'value': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        },
        'OOExample.release': {
            'Meta': {'object_name': 'Release'},
            'attrbutes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['OOExample.Attribute']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'})
        }
    }

    complete_apps = ['OOExample']