from django.db import models


# Create your models here.

class FoodCategory(models.Model):
    food_category_name = models.CharField(max_length=100, null=False, unique=True)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['food_category_name']

    def __str__(self):
        return "{} {}".format(self.food_category_name, self.isActive)


class Food(models.Model):
    category = models.OneToOneField(FoodCategory, on_delete=models.CASCADE)
    food_name = models.CharField(max_length=200, null=False, unique=True)
    title = models.CharField(max_length=200)
    slug = models.SlugField(null=False, unique=True)
    photo = models.ImageField('item_photo', upload_to="img/food_item",
                              null=True, width_field='width_field',
                              height_field='height_field')
    width_field = models.IntegerField(default=0)
    height_field = models.IntegerField(default=0)
    price = models.FloatField(default=0.0)
    isActive = models.BooleanField(default=True)

    class Meta:
        ordering = ['category', 'food_name', 'slug']

    def __str__(self):
        return "{} {} {} {} {} {}".format(self.category,
                                          self.food_name,
                                          self.title,
                                          self.slug,
                                          self.price,
                                          self.isActive)
