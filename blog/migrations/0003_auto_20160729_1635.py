# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20160729_0652'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='create',
            new_name='created',
        ),
    ]
