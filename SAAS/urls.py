from django.urls import path

from .views import (
 	saasHome, packageDetails, packageCheckout, userPackageView,
	logInView, regView,
	aboutusView, supportView, logout_user
)

urlpatterns = [
	##landing page
	path("", saasHome, name="landing"),
	# log in and reg 
	path("login/", logInView, name="login"),
	path("registration/", regView, name="registration"),
	path("logout/", logout_user, name="logout"),

	# Package
	path("package-details/<int:id>/", packageDetails, name="package-details"),
	path("package-checkout/<int:id>/", packageCheckout, name="package-checkout"),
	path("user-package/<int:id>/",userPackageView, name="userPackage"), 

	# footer pages
	# about us
	path("aboutus/", aboutusView, name="aboutus"),
	# support
	path("support/", supportView, name="support"),
]