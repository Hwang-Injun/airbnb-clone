from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.Reservation)
class ReservationAdmin(admin.ModelAdmin):
    pass

    list_display = (
        "room",
        "status",
        "check_in",
        "check_out",
        "guest",
        "status",
        "in_progress",
        "is_finished",
    )

    list_filter = ("status",)
