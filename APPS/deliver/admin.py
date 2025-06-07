from django.contrib import admin
from .models import DeliveryTasks
from .models import DeliveryItems
from .models import TemperatureLog
from .models import DispatchOrders
# Register your models here.
admin.site.register(DeliveryTasks)
admin.site.register(DeliveryItems)
admin.site.register(TemperatureLog)
admin.site.register(DispatchOrders)