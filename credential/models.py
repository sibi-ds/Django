"""This module contains classes
which are used to store credentials
and store user access details
"""
from django.db import models


class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=45, unique=True)
    description = models.TextField()


class Employee(models.Model):
    employee_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=45, unique=True)
    projects = models.ManyToManyField(Project, related_name='employees',
                                      blank=True)


class Vault(models.Model):
    vault_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    email_address = models.EmailField(max_length=45)
    password = models.CharField(max_length=45)
    description = models.TextField()
    access_level = models.CharField(max_length=45)
    project = models.OneToOneField(Project, on_delete=models.CASCADE,
                                   to_field='project_id')


class Component(models.Model):
    component_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=45)
    description = models.TextField()
    access_level = models.CharField(max_length=45)
    vault = models.ForeignKey(Vault, to_field='vault_id',
                              on_delete=models.CASCADE,
                              related_name='components')


class Item(models.Model):
    item_id = models.AutoField(primary_key=True)
    key = models.CharField(max_length=45)
    value = models.CharField(max_length=45)
    component = models.ForeignKey(Component, on_delete=models.CASCADE,
                                  to_field='component_id',
                                  related_name='items')


class VaultAccess(models.Model):
    class Meta:
        unique_together = (('vault', 'employee'),)

    vault = models.ForeignKey(Vault, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, to_field='email_address',
                                 db_column='email_address',
                                 on_delete=models.CASCADE)


class ComponentAccess(models.Model):
    class Meta:
        unique_together = (('component', 'employee'),)

    component = models.ForeignKey(Component, on_delete=models.CASCADE)
    employee = models.ForeignKey(Employee, to_field='email_address',
                                 db_column='email_address',
                                 on_delete=models.CASCADE)
