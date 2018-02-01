from django.db import models



class Department(models.Model):
    department_id = models.CharField(max_length=2, primary_key=True, unique=True)
    department_name = models.CharField(max_length=40)

    class Meta:
        ordering = ["department_id"]
        verbose_name = "LMRussia отдел"
        verbose_name_plural = "LMRussia_1 отделы"

    def __str__(self):
        return self.department_id

class SubDepartment(models.Model):
    sub_department_id = models.CharField(max_length=4, primary_key=True, unique=True)
    sub_department_name = models.CharField(max_length=60)
    department = models.ForeignKey(Department)

    class Meta:
        ordering = ["sub_department_id"]
        verbose_name = "LMRussia подотдел"
        verbose_name_plural = "LMRussia_2 потделы"

    def __str__(self):
        return self.sub_department_id

class DepartmentAdeo(models.Model):
    department_adeo_id = models.CharField(max_length=6, primary_key=True, unique=True)
    department_adeo_name = models.CharField(max_length=40)

    class Meta:
        ordering = ["department_adeo_id"]
        verbose_name = "Adeo отдел"
        verbose_name_plural = "Adeo_1 отделы"

    def __str__(self):
        return self.department_adeo_id

class SubDepartmentAdeo(models.Model):
    sub_department_adeo_id = models.CharField(max_length=12, primary_key=True, unique=True)
    sub_department_adeo_name = models.CharField(max_length=60)
    department_adeo = models.ForeignKey(DepartmentAdeo)

    class Meta:
        ordering = ["sub_department_adeo_id"]
        verbose_name = "Adeo подотдел"
        verbose_name_plural = "Adeo_2 потделы"

    def __str__(self):
        return self.sub_department_adeo_id

class ModelGroupAdeo(models.Model):
    model_group_adeo_id = models.CharField(max_length=14, primary_key=True, unique=True)
    model_group_adeo_name = models.CharField(max_length=60)
    sub_department_adeo = models.ForeignKey(SubDepartmentAdeo)

    class Meta:
        ordering = ["model_group_adeo_id"]
        verbose_name = "Adeo группа моделей"
        verbose_name_plural = "Adeo_3 группы моделей"

    def __str__(self):
        return self.model_group_adeo_id

# Model Adeo
class Model(models.Model):
    model_id = models.CharField(max_length=10, primary_key=True, unique=True)
    model_fr_name = models.CharField(max_length=200)
    model_en_name = models.CharField(max_length=200)
    model_ru_name = models.CharField(max_length=200)
    model_department_adeo = models.ForeignKey(DepartmentAdeo)
    model_sub_department_adeo = models.ForeignKey(SubDepartmentAdeo)
    model_group_adeo = models.ForeignKey(ModelGroupAdeo)

    class Meta:
        ordering = ["model_id"]
        verbose_name = "модель Адео"
        verbose_name_plural = "Structure_1 модели Адео"

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
        verbose_name_plural = "Structure_2 атрибуты"

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
        verbose_name_plural = "Structure_3 значения атрибутов"

    def __str__(self):
        return self.value_id

#LMCode
class LMCode(models.Model):
    lmcode_id = models.CharField(max_length=8, primary_key=True, unique=True)
    lmcode_name = models.CharField(max_length=200)
    lmcode_avs = models.DateField()
    lmcode_model = models.ForeignKey(Model)
    lmcode_department = models.ForeignKey(Department)
    lmcode_sub_department = models.ForeignKey(SubDepartment)

    class Meta:
        ordering = ["lmcode_id"]
        verbose_name = "lm код"
        verbose_name_plural = "Structure_4 lm коды"

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
    DOC_TYPES = (
        ('BDD', 'BDD_RMS'),
        ('LINK', 'Link file'),
    )
    type = models.CharField(max_length=5,
                            unique=True,
                            primary_key=True,
                            default='BDD',
                            choices=DOC_TYPES)
    description = models.CharField(max_length=255, blank=True)
    document = models.FileField(upload_to='documents/')
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.type

    class Meta:
        verbose_name = "документ Excel"
        verbose_name_plural = "документы Excel"
