from django.db import models



class Department(models.Model):
    department_id = models.CharField(max_length=2, primary_key=True, unique=True)
    department_name = models.CharField(max_length=40)

    def __str__(self):
        return self.department_id


# Model Adeo
class Model(models.Model):
    model_id = models.CharField(max_length=10, primary_key=True, unique=True)
    model_fr_name = models.CharField(max_length=200)
    model_en_name = models.CharField(max_length=200)
    model_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.model_id


# Attribute
class Attribute(models.Model):
    attribute_id = models.CharField(max_length=9, primary_key=True, unique=True)
    attribute_limited = models.BooleanField()
    attribute_fr_name = models.CharField(max_length=200)
    attribute_en_name = models.CharField(max_length=200)
    attribute_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.attribute_id


# Value
class Value(models.Model):
    value_id = models.CharField(max_length=10, primary_key=True, unique=True)
    value_fr_name = models.CharField(max_length=200)
    value_en_name = models.CharField(max_length=200)
    value_ru_name = models.CharField(max_length=200)

    def __str__(self):
        return self.value_id

#LMCode
class LMCode(models.Model):
    lmcode_id = models.CharField(max_length=8, primary_key=True, unique=True)
    lmcode_name = models.CharField(max_length=200)
    lmcode_avs = models.DateField()
    lmcode_model = models.ForeignKey(Model)
    lmcode_department = models.ForeignKey(Department)

    def __str__(self):
        return self.lmcode_id

#Link - принадлежность значений и атрибутов к моделям. Одной записи соответствует одно значение
class Link(models.Model):
    link_model = models.ForeignKey(Model)
    link_attribute = models.ForeignKey(Attribute)
    link_value = models.ForeignKey(Value)
    link_name = str(link_model) + " + " + str(link_attribute) + " + " + str(link_value)

    def __str__(self):
        return self.link_name

"""
#LMCodeValue
class LMCodeValue(models.Model):
    lmcode_id = models.ForeignKey(LMCode)
    attribute_id = models.ForeignKey(Attribute)
    value_id = models.ForeignKey(Value, default=None)
    value_not_limited = models.DecimalField(default=None)
    name = str(lmcode_id) + " - " + str(attribute_id)

    def __str__(self):
        return self.name
"""