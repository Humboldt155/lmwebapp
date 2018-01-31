from django.db import models



class Department(models.Model):
    department_id = models.CharField(max_length=2, primary_key=True, unique=True)
    department_name = models.CharField(max_length=40)

    class Meta:
        ordering = ["department_id"]
        verbose_name = "отдел"
        verbose_name_plural = "отделы"

    def __str__(self):
        return self.department_id


# Model Adeo
class Model(models.Model):
    model_id = models.CharField(max_length=10, primary_key=True, unique=True)
    model_fr_name = models.CharField(max_length=200)
    model_en_name = models.CharField(max_length=200)
    model_ru_name = models.CharField(max_length=200)

    class Meta:
        ordering = ["model_id"]
        verbose_name = "модель Адео"
        verbose_name_plural = "модели Адео"

    def __str__(self):
        return self.model_id


# Attribute
class Attribute(models.Model):
    attribute_id = models.CharField(max_length=9, primary_key=True, unique=True)
    attribute_is_open = models.BooleanField()
    attribute_fr_name = models.CharField(max_length=200)
    attribute_en_name = models.CharField(max_length=200)
    attribute_ru_name = models.CharField(max_length=200)

    class Meta:
        ordering = ["attribute_id"]
        verbose_name = "атрибут"
        verbose_name_plural = "атрибуты"

    def __str__(self):
        return self.attribute_id


# Value
class Value(models.Model):
    value_id = models.CharField(max_length=10, primary_key=True, unique=True)
    value_fr_name = models.CharField(max_length=200)
    value_en_name = models.CharField(max_length=200)
    value_ru_name = models.CharField(max_length=200)

    class Meta:
        ordering = ["value_id"]
        verbose_name = "значение атрибута"
        verbose_name_plural = "значения атрибутов"

    def __str__(self):
        return self.value_id

#LMCode
class LMCode(models.Model):
    lmcode_id = models.CharField(max_length=8, primary_key=True, unique=True)
    lmcode_name = models.CharField(max_length=200)
    lmcode_avs = models.DateField()
    lmcode_model = models.ForeignKey(Model)
    lmcode_department = models.ForeignKey(Department)

    class Meta:
        ordering = ["lmcode_id"]
        verbose_name = "lm код"
        verbose_name_plural = "lm коды"

    def __str__(self):
        return self.lmcode_id

#Link - принадлежность значений и атрибутов к моделям. Одной записи соответствует одно значение
class Link(models.Model):
    link_model = models.ForeignKey(Model)
    link_attribute = models.ForeignKey(Attribute)
    link_value = models.ForeignKey(Value, blank=True)
    link_name = str(link_model) + " + " + str(link_attribute) + " + " + str(link_value)

    class Meta:
        ordering = ["link_value", "link_attribute", "link_model"]
        unique_together = ("link_model", "link_attribute", "link_value")
        verbose_name = "связь"
        verbose_name_plural = "связи"

    def __str__(self):
        return self.link_name

class Document(models.Model):
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)