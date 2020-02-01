from django.db import models


class LatLong(models.Model):
    """
    lattitude and longitudinal points for a location
    """

    lat = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )
    location_key = models.ForeignKey(
        'core.Location',
        related_name='lat_longs',
        null=False,
        on_delete=models.CASCADE,
    )
    long = models.DecimalField(
        max_digits=9,
        decimal_places=6,
        blank=True,
        null=True,
    )


class Location(models.Model):
    block = models.CharField(
        max_length=255,
        blank=False,
    )
    cutting_permit = models.CharField(
        max_length=255,
        blank=False,
    )
    license = models.CharField(
        max_length=255,
        blank=False,
    )
    name = models.CharField(
        max_length=255,
        blank=False,
    )

    def __str__(self):
        return str(self.name)


class PlotData(models.Model):
    """
    Input data for a particular plot
    """

    SPECIES_PL = 'PL'
    SPECIES_SX = 'SX'
    SPECIES_BL = 'BL'
    SPECIES_FD = 'FD'
    SPECIES_CHOICES = [
        (SPECIES_PL, 'Pine'),
        (SPECIES_SX, 'Spruce'),
        (SPECIES_BL, 'Balsam'),
        (SPECIES_FD, 'Douglas Fir'),
    ]

    dbh = models.IntegerField(
        blank=False,
        null=False,
    )
    gross_piece_size = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        blank=False,
        null=False,
    )
    height = models.IntegerField(
        blank=False,
        null=False,
    )
    net_piece_size = models.DecimalField(
        max_digits=9,
        decimal_places=3,
        blank=False,
        null=False,
    )
    plot_key = models.ForeignKey(
        'core.Plot',
        related_name='plot_datas',
        null=False,
        on_delete=models.CASCADE,
    )
    species = models.CharField(
        max_length=255,
        blank=False,
        choices=SPECIES_CHOICES,
        default=SPECIES_PL,
    )
    tree = models.IntegerField(
        blank=True,
        null=True,
    )

    def __str__(self):
        return str(self.species)


class Plot(models.Model):
    """
    Information on each plot
    """

    location = models.ForeignKey(
        'core.Location',
        related_name='plot',
        null=False,
        on_delete=models.CASCADE,
    )
    plot_number = models.IntegerField(
        blank=False,
        null=False,
    )
    userkey = models.ForeignKey(
        'users.User',
        related_name='plot',
        null=False,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return str(self.userkey) + "-" + str(self.location) + "-Plot" + str(self.plot_number)
