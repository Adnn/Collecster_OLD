# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Removing M2M table for field attrbutes on 'Release'
        db.delete_table('OOExample_release_attrbutes')

        # Adding M2M table for field attributes on 'Release'
        db.create_table('OOExample_release_attributes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['OOExample.release'], null=False)),
            ('attribute', models.ForeignKey(orm['OOExample.attribute'], null=False))
        ))
        db.create_unique('OOExample_release_attributes', ['release_id', 'attribute_id'])


    def backwards(self, orm):
        # Adding M2M table for field attrbutes on 'Release'
        db.create_table('OOExample_release_attrbutes', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('release', models.ForeignKey(orm['OOExample.release'], null=False)),
            ('attribute', models.ForeignKey(orm['OOExample.attribute'], null=False))
        ))
        db.create_unique('OOExample_release_attrbutes', ['release_id', 'attribute_id'])

        # Removing M2M table for field attributes on 'Release'
        db.delete_table('OOExample_release_attributes')


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
            'attributes': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'to': "orm['OOExample.Attribute']", 'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '60'})
        }
    }

    complete_apps = ['OOExample']