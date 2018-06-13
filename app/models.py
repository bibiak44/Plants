from django.db import models
from django.utils import timezone

from django.forms import ModelForm
from django.db import models
from model_utils import Choices


class Plant(models.Model):

    typ_vyber = (
        ('1', 'Trvalka'),
        ('2', 'Cibulovina'),
        ('3', 'Trava'),
        ('4', 'Ker'),
        ('5', 'Popinavy ker'),
        ('6', 'Popinavka'),
        ('7', 'Strom'),
    )

    farba_vyber = (
        ('1', 'Biela'),
        ('2', 'Zlta'),
        ('3', 'Oranzova'),
        ('4','Cervena'),
        ('5', 'Ruzova'),
        ('6', 'Fialova'),
        ('7', 'Zelena'),
        ('8', 'Modra'),
        ('9', 'Hneda'),
    )

    pouzitie_vyber = (
        ('1', 'Vypln'),
        ('2', 'Kostra'),
        ('3', 'Dominanta'),
        ('4', 'Formalna vysadba'),
        ('5', 'Neformalna vysadba'),
        ('6', 'Podrast'),
        ('7', 'Podopokryvna'),
        ('8', 'Soliter'),
        ('9', 'Zivy plot'),
    )

    kvitnutie_vyber = (
        ('1', 'Januar'),
        ('2', 'Februar'),
        ('3', 'Marec'),
        ('4', 'April'),
        ('5', 'Maj'),
        ('6', 'Jun'),
        ('7', 'Jul'),
        ('8', 'August'),
        ('9', 'September'),
        ('10', 'Oktober'),
        ('11', 'November'),
        ('12', 'December'),
    )

    stanovisko_vyber = (
        ('1', 'Volna plocha'),
        ('2', 'Porast'),
        ('3', 'Okraje porastov'),
        ('4', 'Zahon'),
        ('5', 'Kamenista vysadba'),
        ('6', 'Alpinium'),
        ('7', 'Okraje vod'),
        ('8', 'Voda'),
        ('9', 'Travy'),
    )

    slnko_vyber = (
        ('1', 'Priame slnko'),
        ('2', 'Polotien'),
        ('3', 'Tien'),
        ('4', 'Chulostive na mraz'),
        ('5', 'Nezalezi')
    )

    vlaha_vyber = (
        ('1', 'Suche stanoviste'),
        ('2', 'Pravidelna zavlaha'),
        ('3', 'Dostatok vlahy'),
    )

    rod_lat = models.CharField('Rod latinsky',max_length=30)
    druh_lat = models.CharField('Druh latinsky',max_length=30, blank=True)
    kultivar = models.CharField('Kultivar',max_length=30, blank=True)
    rod_sk  = models.CharField('Rod slovensky',max_length=30, blank=True, default='neuvedene')
    druh_sk = models.CharField('Druh slovensky',max_length=30, blank=True, default='neuvedene')
    typ = models.CharField('Typ', max_length=1, choices=typ_vyber,null=True, blank=True)
    vyska = models.FloatField('Vyska [m]', null=True, blank=True)
    rozpon = models.IntegerField('Rozpon', null=True, blank=True)
    farba = models.CharField('Farba', max_length=1, choices=farba_vyber, null=True, blank=True)
    pouzitie = models.CharField('Pouzitie', max_length=1, choices=pouzitie_vyber, null=True, blank=True)
    kvitnutie_od = models.CharField('Kvitnutie od', max_length=2, choices=kvitnutie_vyber, null=True, blank=True)
    kvitnutie_do = models.CharField('Kvitnutie do', max_length=2, choices=kvitnutie_vyber, null=True, blank=True)
    stanovisko = models.CharField('Stanovisko', max_length=1, choices=stanovisko_vyber, null=True, blank=True)
    slnko = models.CharField('Slnko', max_length=1, choices=slnko_vyber, null=True, blank=True)
    vlaha = models.CharField('Vlaha', max_length=1, choices=vlaha_vyber, null=True, blank=True)
    fotka = models.ImageField(null=True, blank=True)
    poznamka = models.TextField(null=True, blank=True)

    def __str__(self):
        try:
            label_plant = self.rod_lat + ' ' + self.druh_lat + ' ' + self.kultivar + ' ' + self.farba
        except TypeError:
            label_plant = self.rod_lat + ' ' + self.druh_lat
        return label_plant


class Plant1(models.Model):

    rod_lat = models.CharField('Rod latinsky',max_length=30)
    druh_lat = models.CharField('Druh latinsky',max_length=30, blank=True)
    kultivar = models.CharField('Kultivar',max_length=30, blank=True)
    rod_sk  = models.CharField('Rod slovensky',max_length=30, blank=True, default='neuvedene')
    druh_sk = models.CharField('Druh slovensky',max_length=30, blank=True, default='neuvedene')
    typ = models.CharField('Typ', max_length=30, null=True, blank=True)
    vyska = models.FloatField('Vyska [m]', null=True, blank=True)
    rozpon = models.IntegerField('Rozpon', null=True, blank=True)
    farba = models.CharField('Farba', max_length=30, null=True, blank=True)
    pouzitie = models.CharField('Pouzitie', max_length=30, null=True, blank=True)
    kvitnutie_od = models.IntegerField('Kvitnutie od', null=True, blank=True)
    kvitnutie_do = models.IntegerField('Kvitnutie do', null=True, blank=True)
    stanovisko = models.CharField('Stanovisko', max_length=30, null=True, blank=True)
    slnko = models.CharField('Slnko', max_length=30, null=True, blank=True)
    vlaha = models.CharField('Vlaha', max_length=30, null=True, blank=True)
    fotka = models.ImageField(null=True, blank=True)
    poznamka = models.TextField(null=True, blank=True)

    def __str__(self):
        try:
            label_plant = self.rod_lat + ' ' + self.druh_lat + ' ' + self.kultivar
        except TypeError:
            label_plant = self.rod_lat + ' ' + self.druh_lat
        return label_plant
