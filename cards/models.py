from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MinValueValidator, MaxValueValidator


class Card(models.Model):
    RACES = (
        ('Survivors', 'Survivors'),
        ('Automatons', 'Automatons'),
        ('Outworlders', 'Outworlders'),
        ('Old Ones', 'Old Ones'),
        ("Vish'Kul", "Vish-Kul"),
        ('The Altered', 'The Altered'),
    )
    name = models.CharField(max_length=255)
    race = models.CharField(max_length=255, choices=RACES, blank=True, null=True,
                              help_text="Race")
    energy_cost = models.IntegerField(default=0, blank=True, null=True,
                                      help_text="Energy Cost")
    effect = models.TextField(blank=True, null=True, help_text="Effect")
    comment = models.TextField(blank=True, null=True,
                               help_text="Additional Comments")
    created = models.DateTimeField(auto_now=True)
    created_by = models.ForeignKey(User, blank=True, null=True)
    rarity = models.PositiveIntegerField(default=1, blank=True, null=True,
                                         help_text="1-5",
                                         validators=[MinValueValidator(1),
                                                     MaxValueValidator(5)]
                                         )

    def __unicode__(self):
        return self.name.title()


class AttackDefenseCard(Card):
    hp = models.IntegerField(default=0, blank=True, null=True,
                             help_text="HP")
    attack = models.IntegerField(default=0, blank=True, null=True,
                                 help_text="Attack")
    defense = models.IntegerField(default=0, blank=True, null=True,
                                  help_text="Defense")


class CreatureCard(AttackDefenseCard):
    summoning_cost = models.IntegerField(default=0, blank=True, null=True,
                                         help_text="Summoning Cost")
    guardian = models.BooleanField(default=False,
                                   help_text="Guardian")


class GodCard(CreatureCard):
    pass


class EquipmentCard(AttackDefenseCard):
    carry_weight = models.IntegerField(default=0, blank=True, null=True,
                                       help_text="Carry Weight")
    frame_mounted = models.BooleanField(default=False,
                                        help_text="Frame Mounted")


class MagicCard(Card):
    magic_cost = models.IntegerField(default=0, blank=True, null=True,
                                     help_text="Magic Cost")
    celestial_body = models.BooleanField(default=False,
                                         help_text="Celestial Body")
