from django.db import models
from django.urls import reverse # Used to generate URLs by reversing the URL patterns

# def helper_datefield_to_year (datefield):
#     result = str(datefield)
#     if result=='' or result=='None':
#       return '-'
#     else:
#       return datefield.year

# def helper_datefield_to_text (datefield):
#     result = str(datefield)
#     if result=='' or result=='None':
#         result = '-'
#     return result

class Country(models.Model):
    name = models.CharField(max_length=100)
    flag = models.ImageField(upload_to='images/', null=True, blank=True, default='a000.png') # http://pluto.serverenmin.com:8000/media???? http://pluto.serverenmin.com:8000/media/%23
    def get_absolute_url(self):
        return reverse('country_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.name}'
#        return f'{self.name} <img src="0000"></img>' # As predicted: Plain text 

class Composer(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    year_of_birth = models.CharField(max_length=12, default='', help_text='Year as text') # E.g. "1732",  "1620-30", or "unknown"
    year_of_death = models.CharField(max_length=12, default='', help_text='Year as text') # E.g. "1732",  "1620-30", or "unknown"

#     date_of_birth = models.DateField(null=True, blank=True)
#     date_of_death = models.DateField('Died', null=True, blank=True)

    country = models.ForeignKey('Country', on_delete=models.SET_NULL, null=True)
#     class Meta:
#         ordering = ['last_name', 'first_name']
#     def get_year_information(self):
#         return self.get_birth_year
        
    def get_lifespan (self):
#        return f'{helper_datefield_to_year(self.date_of_birth)}-{helper_datefield_to_year(self.date_of_death)}'
        return f'{self.year_of_birth}-{self.year_of_death}'
        
#     def get_birth_text(self):
# #        return helper_datefield_to_text (self.date_of_birth)
#       return self.year_of_birth
#     def get_death_text(self):
# #        return helper_datefield_to_text (self.date_of_death)
#       return self.year_of_death

    def get_absolute_url(self):
        return reverse('composer_detail', args=[str(self.id)])
    def __str__(self):
#        return f'{self.last_name}, {self.first_name}, ({self.get_birth_text()})-({self.get_death_text()})'
        return f'{self.last_name}, {self.first_name}'
        
class CompositionCategory(models.Model):
    name = models.CharField(max_length=100) # E.g. symphony
    def __str__(self):
        return f'{self.name}'
        
class Composition(models.Model):
    name = models.CharField(max_length=100) # E.g. mass in D-minor
    summary = models.TextField(max_length=1000, help_text='Enter a brief description', blank=True, null=True)
    year = models.CharField(max_length=12, default='', help_text='Year as text') # E.g. "1732",  "1620-30", or "unknown"
    i_opus = models.IntegerField (default=0) # Opus number if >0
    i_category = models.IntegerField (default=0) # E.g. symphony number if >0
    composer = models.ForeignKey('Composer', on_delete=models.SET_NULL, null=True)
    compositioncategory = models.ForeignKey('CompositionCategory', on_delete=models.SET_NULL, null=True)
    def get_text_category (self):
      if (self.i_category>0):
        return f'{self.compositioncategory.name} no. {self.i_category}'
      else:
        return ''
    def get_text_opus (self):
      if (self.i_opus>0):
        return f'opus {self.i_opus}'
      else:
        return ''
    def get_absolute_url(self):
        return reverse('composition_detail', args=[str(self.id)])
    def get_text_without_composer(self):
        return f'{self.name} - {self.get_text_category()} {self.get_text_opus()} ({self.year})'
    def __str__(self):
        return f'{self.composer}: {self.name} - {self.get_text_category()} {self.get_text_opus()} ({self.year})'
#        return f'{self.get_text_without_composer} by {self.composer.name}'

class CollectionCategory(models.Model):
    name = models.CharField(max_length=100) # E.g. "lp", "cd", "flac_catalog", "concert", "tv_program", "kontrapunkt"
    def __str__(self):
        return f'{self.name}'

class Collection(models.Model):
    name = models.CharField(max_length=100) # E.g. kontrapunkt1988 0301, Vinylplate nr 88, Konsert Olavshallen 12 april 1993. KUN NAVN, INGEN KOBLINGER I DATABASEN
    summary = models.TextField(max_length=1000, help_text='Enter a brief description', blank=True, null=True)
    collectioncategory = models.ForeignKey('CollectionCategory', on_delete=models.SET_NULL, null=True)
    def get_absolute_url(self):
        return reverse('collection_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.name}'

class Piece(models.Model):
    name = models.CharField(max_length=100) # E.g. First movement
    composition = models.ForeignKey('Composition', on_delete=models.SET_NULL, null=True)
    i_sequence = models.IntegerField (default=0)
    def get_absolute_url(self):
        return reverse('piece_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.name}'

class PieceInstance(models.Model):
    comment = models.CharField(max_length=100, default="", blank=True, null=True) # E.g. "Very good performance"
    collection = models.ForeignKey('Collection', on_delete=models.SET_NULL, null=True)
    piece = models.ForeignKey('Piece', on_delete=models.SET_NULL, null=True)
    def get_absolute_url(self):
        return reverse('pieceinstance_detail', args=[str(self.id)])
    def __str__(self):
        return f'{self.name}'



