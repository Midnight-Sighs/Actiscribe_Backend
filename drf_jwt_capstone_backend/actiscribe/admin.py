from django.contrib import admin
from .models import Resident
from .models import Note
from .models import Activity
from .models import Participation
from .models import Assessment


# Register your models here.

admin.site.register(Resident)
admin.site.register(Note)
admin.site.register(Activity)
admin.site.register(Participation)
admin.site.register(Assessment)
