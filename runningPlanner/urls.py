from django.contrib import admin
from django.urls import path

from viewer.models import TrainingPlan, Shoe, RunParameter

admin.site.register(TrainingPlan)
admin.site.register(Shoe)
admin.site.register(RunParameter)

urlpatterns = [
    path('admin/', admin.site.urls),
]