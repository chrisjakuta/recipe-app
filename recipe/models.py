from django.db import models

class Ingredient(models.Model):
	name = models.CharField(max_length=200)
	articleNumber = models.IntegerField(unique=True)
	costPerUnity = models.DecimalField(max_digits=4, decimal_places=2)

	def __str__(self):
		return self.name

class Recipe(models.Model):
	name = models.CharField(max_length=200)
	ingredients = models.ManyToManyField(Ingredient, through='Recipe_Ingredient')

	def __str__(self):
		return self.name

class Recipe_Ingredient(models.Model):
	recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
	ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
	quantity = models.FloatField()

	GRAM = 'g'
	KILOGRAM = 'kg'
	LITER = 'l'
	CENTILITER = 'cl'

	UNITY_CHOICES = (
		(GRAM, 'Gram(s)'),
		(KILOGRAM, 'Kilogram(s)'),
		(LITER, 'Liter(s)'),
		(CENTILITER, 'Centiliter(s)'),
	)

	quantityUnit = models.CharField(
		max_length=2,
		choices=UNITY_CHOICES,
		default=GRAM,
	)