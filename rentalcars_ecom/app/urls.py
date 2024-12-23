from .import views
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as  auth_view
from .forms import LoginForm, MyPasswordChangeForm, MySetPasswordForm, MyPasswordResetForm
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug:val>', views.CategoryView.as_view(), name='category'),
    path("productdetail/<int:pk>", views.Productdetail.as_view(), name="productdetail"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("registration/", views.CustomerRegistrationView.as_view(),
         name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(#Helps bypass in views.py instead of doing a lot of work in views
        template_name = 'app/login.html', authentication_form= LoginForm), 
         name='login'),
    path('profile/', views.ProfileView.as_view(), name='profile'),#as_view is only used when working with classes
    path('address/', views.address, name='address'),
    path('updateAdress/<int:pk>', views.UpdateAdress.as_view(), name='updateAdress'),
    path('passwordchange/', auth_view.PasswordChangeView.as_view(template_name = 'app/changepassword.html', 
        form_class= MyPasswordChangeForm, success_url='/passwordchangedone'), name= 'changepassword'),
    path('passwordchangedone/', auth_view.PasswordChangeDoneView.as_view(template_name = 'app/passwordchangedone.html', 
          ), name= 'passwordchangedone'),
    path('logout/', auth_view.LogoutView.as_view(next_page = 'login'), name='logout'),
      path(
        'do-logout/',
        TemplateView.as_view(template_name='app/logout.html'),
        name='do-logout',
    ),
    path('password-reset/', auth_view.PasswordResetView.as_view
         (template_name = 'app/password_reset.html', form_class =MyPasswordResetForm), 
         name='password_reset'), 
    path('password-reset/done/', auth_view.PasswordResetDoneView.as_view
         (template_name = 'app/password_reset_done.html'), 
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/', auth_view.PasswordResetConfirmView.as_view
         (template_name = 'app/password_reset_confirm.html', form_class =MySetPasswordForm), 
         name='password_reset_confirm'), 
    path('password-reset-complete/', auth_view.PasswordResetCompleteView.as_view
         (template_name = 'app/password_reset_complete.html'), 
         name='password_reset_complete'),
]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)#for displaying pics for the products
