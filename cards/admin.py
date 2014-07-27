from django.contrib import admin

from cards.models import *

THOUSANDS = ['hp', 'attack', 'defense']


class _CustomSave(admin.ModelAdmin):
    search_fields = ['name']
    list_filter = ['race', 'created_by']
    def save_model(self, request, obj, form, change):
        obj.created_by = request.user
        for field in THOUSANDS:
            try:
                if getattr(obj, field) is not None and getattr(obj, field) < 1000:
                    setattr(obj, field, getattr(obj, field) * 1000)
            except AttributeError:
                pass
        obj.save()


class CreatureCardAdmin(_CustomSave):
    list_display = (
        'name', 'race', 'hp', 'energy_cost', 'summoning_cost', 'attack', 'defense',
        'guardian', 'rarity', 'created_by', 'created',
    )
    fieldsets = [
        (None,  {'fields': ['name', 'race',
                            'hp', 'energy_cost',
                            'summoning_cost', 'guardian',
                            'attack', 'defense',
                            'effect', 'rarity'],
                 }
        ),

        ('Comments', {'fields': ['comment'], 'classes': ['collapse']}),
    ]



class EquipmentCardAdmin(_CustomSave):
    list_display = (
        'name', 'race', 'hp', 'energy_cost', 'carry_weight', 'attack', 'defense',
        'frame_mounted', 'rarity', 'created_by', 'created',
    )
    fieldsets = [
        (None,  {'fields': ['name', 'race',
                            'hp', 'energy_cost',
                            'carry_weight', 'frame_mounted',
                            'attack', 'defense',
                            'effect', 'rarity'],
                 }
        ),
        ('Comments', {'fields': ['comment'], 'classes': ['collapse']}),
    ]


class MagicCardAdmin(_CustomSave):
    list_display = (
        'name', 'race', 'energy_cost', 'magic_cost',
        'rarity', 'created_by', 'created',
    )
    fieldsets = [
        (None,  {'fields': ['name', 'race',
                            'energy_cost', 'magic_cost',
                            'celestial_body',
                            'effect', 'rarity'],
                 }
        ),

        ('Comments', {'fields': ['comment'], 'classes': ['collapse']}),
    ]


admin.site.register(CreatureCard, CreatureCardAdmin)
admin.site.register(MagicCard, MagicCardAdmin)
admin.site.register(EquipmentCard, EquipmentCardAdmin)
admin.site.register(GodCard, CreatureCardAdmin)
