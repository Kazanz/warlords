# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Card'
        db.create_table(u'cards_card', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('race', self.gf('django.db.models.fields.CharField')(max_length=255, null=True, blank=True)),
            ('energy_cost', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('effect', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('comment', self.gf('django.db.models.fields.TextField')(null=True, blank=True)),
            ('created', self.gf('django.db.models.fields.DateTimeField')(auto_now=True, blank=True)),
            ('created_by', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'], null=True, blank=True)),
            ('rarity', self.gf('django.db.models.fields.PositiveIntegerField')(default=1, null=True, blank=True)),
        ))
        db.send_create_signal(u'cards', ['Card'])

        # Adding model 'AttackDefenseCard'
        db.create_table(u'cards_attackdefensecard', (
            (u'card_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cards.Card'], unique=True, primary_key=True)),
            ('hp', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('attack', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('defense', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
        ))
        db.send_create_signal(u'cards', ['AttackDefenseCard'])

        # Adding model 'CreatureCard'
        db.create_table(u'cards_creaturecard', (
            (u'attackdefensecard_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cards.AttackDefenseCard'], unique=True, primary_key=True)),
            ('summoning_cost', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('guardian', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cards', ['CreatureCard'])

        # Adding model 'GodCard'
        db.create_table(u'cards_godcard', (
            (u'creaturecard_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cards.CreatureCard'], unique=True, primary_key=True)),
        ))
        db.send_create_signal(u'cards', ['GodCard'])

        # Adding model 'EquipmentCard'
        db.create_table(u'cards_equipmentcard', (
            (u'attackdefensecard_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cards.AttackDefenseCard'], unique=True, primary_key=True)),
            ('carry_weight', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('frame_mounted', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cards', ['EquipmentCard'])

        # Adding model 'MagicCard'
        db.create_table(u'cards_magiccard', (
            (u'card_ptr', self.gf('django.db.models.fields.related.OneToOneField')(to=orm['cards.Card'], unique=True, primary_key=True)),
            ('magic_cost', self.gf('django.db.models.fields.IntegerField')(default=0, null=True, blank=True)),
            ('celestial_body', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal(u'cards', ['MagicCard'])


    def backwards(self, orm):
        # Deleting model 'Card'
        db.delete_table(u'cards_card')

        # Deleting model 'AttackDefenseCard'
        db.delete_table(u'cards_attackdefensecard')

        # Deleting model 'CreatureCard'
        db.delete_table(u'cards_creaturecard')

        # Deleting model 'GodCard'
        db.delete_table(u'cards_godcard')

        # Deleting model 'EquipmentCard'
        db.delete_table(u'cards_equipmentcard')

        # Deleting model 'MagicCard'
        db.delete_table(u'cards_magiccard')


    models = {
        u'auth.group': {
            'Meta': {'object_name': 'Group'},
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': u"orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        u'auth.permission': {
            'Meta': {'ordering': "(u'content_type__app_label', u'content_type__model', u'codename')", 'unique_together': "((u'content_type', u'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['contenttypes.ContentType']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        u'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Group']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'symmetrical': 'False', 'related_name': "u'user_set'", 'blank': 'True', 'to': u"orm['auth.Permission']"}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
        u'cards.attackdefensecard': {
            'Meta': {'object_name': 'AttackDefenseCard', '_ormbases': [u'cards.Card']},
            'attack': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'card_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cards.Card']", 'unique': 'True', 'primary_key': 'True'}),
            'defense': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'hp': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'cards.card': {
            'Meta': {'object_name': 'Card'},
            'comment': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'created': ('django.db.models.fields.DateTimeField', [], {'auto_now': 'True', 'blank': 'True'}),
            'created_by': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['auth.User']", 'null': 'True', 'blank': 'True'}),
            'effect': ('django.db.models.fields.TextField', [], {'null': 'True', 'blank': 'True'}),
            'energy_cost': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'race': ('django.db.models.fields.CharField', [], {'max_length': '255', 'null': 'True', 'blank': 'True'}),
            'rarity': ('django.db.models.fields.PositiveIntegerField', [], {'default': '1', 'null': 'True', 'blank': 'True'})
        },
        u'cards.creaturecard': {
            'Meta': {'object_name': 'CreatureCard', '_ormbases': [u'cards.AttackDefenseCard']},
            u'attackdefensecard_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cards.AttackDefenseCard']", 'unique': 'True', 'primary_key': 'True'}),
            'guardian': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summoning_cost': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'cards.equipmentcard': {
            'Meta': {'object_name': 'EquipmentCard', '_ormbases': [u'cards.AttackDefenseCard']},
            u'attackdefensecard_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cards.AttackDefenseCard']", 'unique': 'True', 'primary_key': 'True'}),
            'carry_weight': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'}),
            'frame_mounted': ('django.db.models.fields.BooleanField', [], {'default': 'False'})
        },
        u'cards.godcard': {
            'Meta': {'object_name': 'GodCard', '_ormbases': [u'cards.CreatureCard']},
            u'creaturecard_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cards.CreatureCard']", 'unique': 'True', 'primary_key': 'True'})
        },
        u'cards.magiccard': {
            'Meta': {'object_name': 'MagicCard', '_ormbases': [u'cards.Card']},
            u'card_ptr': ('django.db.models.fields.related.OneToOneField', [], {'to': u"orm['cards.Card']", 'unique': 'True', 'primary_key': 'True'}),
            'celestial_body': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'magic_cost': ('django.db.models.fields.IntegerField', [], {'default': '0', 'null': 'True', 'blank': 'True'})
        },
        u'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        }
    }

    complete_apps = ['cards']