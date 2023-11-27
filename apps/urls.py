from django.urls import path, include


urlpatterns = [
    path('', include("apps.core.urls")),
    path('', include("apps.sponsors.urls")),
    path('', include("apps.students.urls")),
    path('qwerty/', include("apps.students.urls")),
    path('metsenat/', include("apps.sponsors.urls")),
]