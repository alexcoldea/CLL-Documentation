# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2021-11-10 17:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('clinicalcode', '0047_auto_20211019_0955'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='historicalphenotypetagmap',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='historicalphenotypetagmap',
            name='history_user',
        ),
        migrations.RemoveField(
            model_name='historicalphenotypetagmap',
            name='phenotype',
        ),
        migrations.RemoveField(
            model_name='historicalphenotypetagmap',
            name='tag',
        ),
        migrations.RemoveField(
            model_name='phenotypetagmap',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='phenotypetagmap',
            name='phenotype',
        ),
        migrations.RemoveField(
            model_name='phenotypetagmap',
            name='tag',
        ),
        migrations.DeleteModel(name='HistoricalPhenotypeTagMap', ),
        migrations.DeleteModel(name='PhenotypeTagMap', ),
    ]