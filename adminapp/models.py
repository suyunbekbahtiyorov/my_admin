# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Faculty(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_faculty'
    def __str__(self):
        return self.name


class Group(models.Model):
    name = models.CharField(max_length=100)
    faculty = models.ForeignKey(Faculty, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_group'
    def __str__(self):
        return self.name


class Kafedra(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_kafedra'

    def __str__(self):
        return self.name


class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    group = models.ForeignKey(Group, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_student'


class Subject(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'adminapp_subject'
    def __str__(self):
        return self.name


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    kafedra = models.ForeignKey(Kafedra, models.DO_NOTHING, blank=True, null=True)
    subject = models.ForeignKey(Subject, models.DO_NOTHING, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'adminapp_teacher'
    def __str__(self):
        return self.first_name+" "+self.last_name
