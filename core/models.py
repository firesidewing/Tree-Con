from django.db import models


class LatLong(models.Model):
    """
    lattitude and longitudinal points for a location
    """

    lat = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True,)
    location_key = models.ForeignKey(
        "core.Location", related_name="lat_longs", null=False, on_delete=models.CASCADE,
    )
    long = models.DecimalField(max_digits=9, decimal_places=6, blank=True, null=True,)


class Location(models.Model):
    block = models.CharField(max_length=255, blank=False,)
    cutting_permit = models.CharField(max_length=255, blank=False,)
    license = models.CharField(max_length=255, blank=False,)
    name = models.CharField(max_length=255, blank=False,)
    baf = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False, default=0
    )
    bec = models.ForeignKey(
        "core.Zone",
        related_name="zone",
        null=False,
        on_delete=models.CASCADE,
        default=0,
    )

    def __str__(self):
        return str(self.name + " - " + self.bec.name)


class Zone(models.Model):
    short = models.CharField(max_length=10)
    name = models.CharField(max_length=100)

    def __str__(self):
        return str(self.name)


class PlotData(models.Model):
    """
    Input data for a particular plot
    """

    dbh = models.IntegerField(blank=False, null=False,)
    height = models.IntegerField(blank=False, null=False,)
    gross_piece_size = models.DecimalField(
        max_digits=9, decimal_places=3, blank=False, null=False,
    )
    net_piece_size = models.DecimalField(
        max_digits=9, decimal_places=3, blank=False, null=False,
    )
    plot_key = models.ForeignKey(
        "core.Plot", related_name="plot_datas", null=False, on_delete=models.CASCADE,
    )
    tree_species = models.ForeignKey(
        "core.Species", related_name="tree_species", on_delete=models.CASCADE, default=0
    )
    tree = models.IntegerField(blank=True, null=True,)
    blowdown = models.BooleanField(default=0, null=False, blank=False)
    alive = models.BooleanField(default=True, null=True, blank=True)

    def __str__(self):
        return str(self.tree_species)


class Plot(models.Model):
    """
    Information on each plot
    """

    TIMBER = [
        ("Pi/Sx", "Pi/Sx"),
        ("Sx/Pi", "Sx/Pi"),
        ("Sx/Bl", "Sx/Bl"),
    ]

    location = models.ForeignKey(
        "core.Location", related_name="plot", null=False, on_delete=models.CASCADE,
    )
    plot_number = models.IntegerField(blank=False, null=False,)
    userkey = models.ForeignKey(
        "users.User", related_name="plot", null=False, on_delete=models.CASCADE,
    )
    slope = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, blank=False, null=False
    )
    gross_volume_ha = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, blank=False, null=False
    )
    net_volume_ha = models.DecimalField(
        max_digits=9, decimal_places=2, default=0, blank=False, null=False
    )
    timber_type = models.CharField(max_length=100, choices=TIMBER, default="Pi/Sx")

    def __str__(self):
        return (
            str(self.userkey)
            + "-"
            + str(self.location)
            + "-Plot"
            + str(self.plot_number)
        )


class Species(models.Model):
    """
    information and constants relative to each species
    """

    species_name = models.CharField(max_length=255, blank=False)

    loss_factor = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False, default=0
    )
    loss_factor_dead = models.DecimalField(
        max_digits=12, decimal_places=2, blank=False, null=False, default=0
    )

    bec = models.CharField(max_length=20, blank=True, null=True)

    vol_type = models.CharField(max_length=20, blank=True, null=True)

    vol_const_a = models.FloatField(blank=True, null=True)

    vol_const_b = models.FloatField(blank=True, null=True)

    vol_const_c = models.FloatField(blank=True, null=True)

    delta = models.FloatField(blank=True, null=True)

    sigma_squared = models.FloatField(blank=True, null=True)

    def __str__(self):
        return str(self.species_name)
