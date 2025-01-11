# from django.urls import path,include
# from . import views
# from rest_framework import routers

# r = routers.DefaultRouter()
# r.register('', views.CompanyRegistrationView)

# rr = routers.DefaultRouter()
# rr.register('', views.PersonRegistrationView)
# urlpatterns = [
#     path('registration/user/', include(rr.urls)),

#     # path('registration/user/', PersonRegistrationView.as_view(), name='register-user'),
#     # path('registration/company/', CompanyRegistrationView.as_view(), name='register-company'),
#     path('registration/company/', include(r.urls)),
#     # path('login/',LoginAPI.as_view(),name='login user')
# ]
from django.urls import path,include
from . import  views
from .views import ( CompanySignupView,
 PersonSignupView,
 CustomAuthToken, LogoutView , sign_in )

app_name = 'accountss'

urlpatterns = [
    path('signup/company/', CompanySignupView.as_view()),
    path('signup/user/', PersonSignupView.as_view()),
    path('signup/', views.Signup,name='signup'),
    path('OTPValidate/',views.OTPCODE,name='otp code'),
    # path('login/',CustomAuthToken.as_view(), name='auth-token'),
    path('login/',views.sign_in, name='login'),
    path('logout/', LogoutView.as_view(), name='logout-view'),

]