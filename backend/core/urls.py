from django.urls import path
from . import views
from product.views import AllListing

urlpatterns = [
    path("", AllListing.as_view(), name="site_index"),
    path("signup", views.signup, name="signup"),
    path("login", views.UserLoginView.as_view(), name="login"),
    path("profile", views.ProfileDetails.as_view(), name="profile"),
    path("edit_profile", views.EditProfile.as_view(), name="edit_profile"),
]