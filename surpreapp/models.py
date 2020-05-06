from django.db import models
from django.utils import timezone
from datetime import date

# Create your models here.
class Score(models.Model):
    startupname = models.CharField(db_column='startupname', max_length=100, blank=False, null=True)
    productname = models.CharField(db_column='productname', max_length=100, blank=False, null=True)
    sentimentscore = models.DecimalField(db_column='sentimentscore',max_digits=10, decimal_places=3, default=0)
    infostartupscore = models.DecimalField(db_column='infostartupscore',max_digits=10, decimal_places=3, default=0)
    infoplatformscore = models.DecimalField(db_column='infoplatformscore',max_digits=10, decimal_places=3, default=0)
    totalscore = models.DecimalField(db_column='totalscore',max_digits=10, decimal_places=3, default=0)
    status = models.CharField(db_column='status', max_length=40, blank=True, null=True)
    changeby = models.CharField(db_column='changeby', max_length=40, blank=True, null=True)
    changetime= models.DateTimeField(db_column='changetime', default=timezone.now)
    calculatedate= models.DateField(db_column='calculatedate', null=True, auto_now=False)
    scorecategory = models.CharField(db_column='scorecategory', max_length=40, blank=True, null=True)
    class Meta:
        db_table = 'score'
        verbose_name = 'Score'
        verbose_name_plural = 'Scores'
        ordering = ['startupname']
    def __unicode__(self):
        return self.startupname
    def __str__(self):
        if (self.startupname!=None or self.productname!=None):
            return str(self.startupname)+" - "+ str(self.productname)
        else:
            return ""

        

class Attribute(models.Model):
    name = models.TextField(db_column='name', max_length=500, blank=False)
    attributetype =  models.CharField(db_column='attributetype', max_length=100, blank=False, null=True)
    class Meta:
        db_table = 'attribute'
        verbose_name = 'Attribute'
        verbose_name_plural = 'Attributes'
        ordering = ['name']
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class AttributeScore(models.Model):
    name = models.TextField(db_column='name', max_length=500, blank=False)
    value = models.IntegerField(db_column='value',blank=False, default=0)
    attributetype =  models.CharField(db_column='attributetype', max_length=100, blank=False, null=True)
    score = models.ForeignKey(Score, on_delete=models.PROTECT, blank=True, null=True)
    class Meta:
        db_table = 'attributescore'
        verbose_name = 'Attribute Score'
        verbose_name_plural = 'Attribute Scores'
        ordering = ['name']
    def __unicode__(self):
        return self.name
    def __str__(self):
        return self.name

class Choice(models.Model):
    label = models.TextField(db_column='label', max_length=100, blank=False)
    value = models.IntegerField(db_column='value',blank=False, default=0)
    class Meta:
        db_table = 'choice'
        verbose_name = 'Choice'
        verbose_name_plural = 'Choices'
        ordering = ['label']
    def __unicode__(self):
        return self.label
    def __str__(self):
        return self.label

