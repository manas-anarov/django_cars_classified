# Generated by Django 2.2.12 on 2020-06-04 13:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('django_classified', '0003_auto_20180717_1107'),
        ('restreklama', '0002_categoryforcar'),
    ]

    operations = [
        migrations.AddField(
            model_name='categoryforcar',
            name='item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='django_classified.Item'),
            preserve_default=False,
        ),
    ]
