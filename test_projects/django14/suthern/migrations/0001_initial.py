# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'MuffinModel'
        db.create_table('suthern_muffinmodel', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('fudge_is_yummy', self.gf('likert_field.models.LikertField')(null=True, blank=True)),
            ('item', self.gf('likert_field.models.LikertField')(null=True, blank=True)),
            ('too_many_questions', self.gf('likert_field.models.LikertField')(null=True, blank=True)),
            ('too_few_questions', self.gf('likert_field.models.LikertField')(null=True, blank=True)),
            ('questions_should_not_be_optional', self.gf('likert_field.models.LikertField')(null=True, blank=True)),
        ))
        db.send_create_signal('suthern', ['MuffinModel'])


    def backwards(self, orm):
        # Deleting model 'MuffinModel'
        db.delete_table('suthern_muffinmodel')


    models = {
        'suthern.muffinmodel': {
            'Meta': {'object_name': 'MuffinModel'},
            'fudge_is_yummy': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'item': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'}),
            'questions_should_not_be_optional': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'}),
            'too_few_questions': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'}),
            'too_many_questions': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'})
        }
    }

    complete_apps = ['suthern']