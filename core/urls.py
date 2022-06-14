from django.contrib import admin
from django.urls import path, include  # add this

urlpatterns = [
    path('admin/', admin.site.urls),          # Django admin route
    path("", include("apps.authentication.urls")), # Auth routes - login 
    path("", include("apps.home.urls")),       # Home routes
    path("", include("apps.administration.urls")), # Administration routes
]


handler404 = "apps.home.views.page_not_found_view"
handler404 = "apps.home.views.custom_error_403"
handler500 = 'apps.home.views.custom_error_500'