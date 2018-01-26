from django.db import models



class Department(models.Model):
    department_id = models.CharField(max_length=2, primary_key=True, unique=True)
    department_name = models.CharField(max_length=40)

    def __str__(self):
        return self.department_id



class Model(models.Model):
    model_id = models.CharField(max_length=10, primary_key=True, unique=True)
    model_fr_name = models.CharField(max_length=200)
    model_en_name = models.CharField(max_length=200)
    model_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.model_id



class Attribute(models.Model):
    attribute_id = models.CharField(max_length=9, primary_key=True, unique=True)
    attribute_fr_name = models.CharField(max_length=200)
    attribute_en_name = models.CharField(max_length=200)
    attribute_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.attribute_id



class Value(models.Model):
    value_id = models.CharField(max_length=10, primary_key=True, unique=True)
    value_fr_name = models.CharField(max_length=200)
    value_en_name = models.CharField(max_length=200)
    value_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.value_id