from django.views.generic import TemplateView

class CompanyDetailView(TemplateView):
    template_name = "company-detail.html"

class CompanyLoginView(TemplateView):
    template_name = "company-login.html"

class CompanyPeopleView(TemplateView):
    template_name = "company-people.html"

class CompanySettingsView(TemplateView):
    template_name = "company-settings.html"

class CompanySignupView(TemplateView):
    template_name = "company-signup.html"

class CompanyTaskView(TemplateView):
    template_name = "company-task.html"

class CompanyTaskDetailView(TemplateView):
    template_name = "company-task-detail.html"