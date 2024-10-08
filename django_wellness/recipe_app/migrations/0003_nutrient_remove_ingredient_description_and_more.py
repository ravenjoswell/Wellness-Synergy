# Generated by Django 5.0.8 on 2024-08-11 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe_app', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Nutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=255)),
                ('quantity', models.FloatField()),
                ('unit', models.CharField(max_length=50)),
            ],
        ),
        migrations.RemoveField(
            model_name='ingredient',
            name='description',
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='description',
        ),
        migrations.AddField(
            model_name='ingredient',
            name='food',
            field=models.CharField(default='Unknown', max_length=255),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='measure',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='quantity',
            field=models.FloatField(default=0.0),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='text',
            field=models.TextField(default='Unknown'),
        ),
        migrations.AddField(
            model_name='ingredient',
            name='weight',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cautions',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='cuisine_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='diet_labels',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='dish_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='health_labels',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='image',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='recipe',
            name='meal_type',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.RemoveField(
            model_name='recipe',
            name='nutritional_facts',
        ),
        migrations.AddField(
            model_name='recipe',
            name='nutritional_facts',
            field=models.ManyToManyField(related_name='recipes', to='recipe_app.nutrient'),
        ),
    ]
