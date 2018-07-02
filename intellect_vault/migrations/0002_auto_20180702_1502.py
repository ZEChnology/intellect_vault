# Generated by Django 2.0.6 on 2018-07-02 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('intellect_vault', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Beat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Deity',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('additional_domains', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='District',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.City')),
            ],
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('deities', models.ManyToManyField(to='intellect_vault.Deity')),
            ],
        ),
        migrations.CreateModel(
            name='Encounter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('nature', models.CharField(choices=[('SCR', 'Scripted'), ('RND', 'Random')], default='SCR', max_length=3)),
                ('description', models.TextField()),
                ('sequence', models.TextField()),
                ('district', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.District')),
            ],
        ),
        migrations.CreateModel(
            name='Faction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('alignment', models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('NN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], default='NN', max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('rules', models.TextField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('appearance', models.TextField()),
                ('voice', models.TextField()),
                ('alignment', models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('NN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], default='NN', max_length=2)),
                ('encounters', models.ManyToManyField(to='intellect_vault.Encounter')),
                ('factions', models.ManyToManyField(to='intellect_vault.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='Nation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='NPC',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('appearance', models.TextField()),
                ('voice', models.TextField()),
                ('alignment', models.CharField(choices=[('LG', 'Lawful Good'), ('NG', 'Neutral Good'), ('CG', 'Chaotic Good'), ('LN', 'Lawful Neutral'), ('NN', 'True Neutral'), ('CN', 'Chaotic Neutral'), ('LE', 'Lawful Evil'), ('NE', 'Neutral Evil'), ('CE', 'Chaotic Evil')], default='NN', max_length=2)),
                ('encounters', models.ManyToManyField(to='intellect_vault.Encounter')),
                ('factions', models.ManyToManyField(to='intellect_vault.Faction')),
            ],
        ),
        migrations.CreateModel(
            name='Plot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('themes', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('world', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.World')),
            ],
        ),
        migrations.CreateModel(
            name='Wilds',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('region', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.Region')),
            ],
        ),
        migrations.AddField(
            model_name='nation',
            name='region',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.Region'),
        ),
        migrations.AddField(
            model_name='item',
            name='monsters',
            field=models.ManyToManyField(to='intellect_vault.Monster'),
        ),
        migrations.AddField(
            model_name='item',
            name='npcs',
            field=models.ManyToManyField(to='intellect_vault.NPC'),
        ),
        migrations.AddField(
            model_name='encounter',
            name='wilds',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.Wilds'),
        ),
        migrations.AddField(
            model_name='city',
            name='nation',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.Nation'),
        ),
        migrations.AddField(
            model_name='beat',
            name='plot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='intellect_vault.Plot'),
        ),
    ]
