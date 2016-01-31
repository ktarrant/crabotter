from __future__ import unicode_literals

from django.db import models
from django.utils.encoding import python_2_unicode_compatible

# Create your models here.

# "_id" : { "$oid" : "516075ea96cc6208b3300133" }, 
#  "name": "I Love Ya, Tomorrow!", 
#  "ingredients": "Cake\n2 cups Sugar\n1 cup Vegetable Oil\n4 whole Eggs", 
#  "url": "http://thepioneerwoman.com/cooking/2012/09/i-love-ya-tomorrow/", 
#  "image": "http://static.thepioneerwoman.com/cooking/files/2012/09/sloppyjoes.jpg", 
#  "ts": {"$date": 1365276138898 }, 
#  "cookTime": "PT45M", 
#  "source": "thepioneerwoman", 
#  "recipeYield": "12", 
#  "datePublished": "2012-09-14", 
#  "prepTime": "PT20M", 
#  "description": "I'm never sure if you would like for me to post the recipes..."
@python_2_unicode_compatible  # only if you need to support Python 2
class Recipe(models.Model):
    name = models.CharField(max_length=256)
    ingredients = models.TextField('ingredients')
    url = models.URLField()
    imageUrl = models.URLField()
    ts = models.DateTimeField()
    cookTime = models.DurationField()
    source = models.CharField(max_length=64)
    recipeYield = models.IntegerField()
    datePublished = models.DateField('date published')
    prepTime = models.DurationField()
    description = models.TextField()

    def __str__(self):
        return self.name