# Generated by Django 5.0.8 on 2024-08-13 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0009_alter_recipe_diet_labels_alter_recipe_health_labels_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='image',
            field=models.URLField(blank=True, max_length=5000, null=True),
        ),
    ]
