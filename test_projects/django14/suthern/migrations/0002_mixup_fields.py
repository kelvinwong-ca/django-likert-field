# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'MuffinModel.item'
        db.delete_column('suthern_muffinmodel', 'item')


        # Changing field 'MuffinModel.too_many_questions'
        db.alter_column('suthern_muffinmodel', 'too_many_questions', self.gf('likert_field.models.LikertField')())

        # Changing field 'MuffinModel.too_few_questions'
        db.alter_column('suthern_muffinmodel', 'too_few_questions', self.gf('likert_field.models.LikertField')())

    def backwards(self, orm):
        # Adding field 'MuffinModel.item'
        db.add_column('suthern_muffinmodel', 'item',
                      self.gf('likert_field.models.LikertField')(null=True, blank=True),
                      keep_default=False)


        # Changing field 'MuffinModel.too_many_questions'
        db.alter_column('suthern_muffinmodel', 'too_many_questions', self.gf('likert_field.models.LikertField')(null=True))

        # Changing field 'MuffinModel.too_few_questions'
        db.alter_column('suthern_muffinmodel', 'too_few_questions', self.gf('likert_field.models.LikertField')(null=True))

    models = {
        'suthern.muffinmodel': {
            'Meta': {'object_name': 'MuffinModel'},
            'fudge_is_yummy': ('likert_field.models.LikertField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'questions_should_not_be_optional': ('likert_field.models.LikertField', [], {'null': 'True'}),
            'too_few_questions': ('likert_field.models.LikertField', [], {'default': '3', 'blank': 'True'}),
            'too_many_questions': ('likert_field.models.LikertField', [], {'default': '3'})
        }
    }

    complete_apps = ['suthern']