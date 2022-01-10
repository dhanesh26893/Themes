from django.urls import path
from .views import (CompanyDetailView,
                    CompanyLoginView,
                    CompanyPeopleView,
                    CompanySettingsView,
                    CompanySignupView,
                    CompanyTaskDetailView,
                    CompanyTaskView)

app_name = "theme"

urlpatterns = [ 
    path('detail/',CompanyDetailView.as_view(),name="company-detail"),
    path('login/',CompanyLoginView.as_view(),name="company-login"),
    path('people/',CompanyPeopleView.as_view(),name="company-people"),
    path('settings/',CompanySettingsView.as_view(),name="company-setting"),
    path('signup/',CompanySignupView.as_view(),name="company-signup"),
    path('task/',CompanyTaskView.as_view(),name="company-task"),
    path('task/detail/',CompanyTaskDetailView.as_view(),name="company-task-detail")
]