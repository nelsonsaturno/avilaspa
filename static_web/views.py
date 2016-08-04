from django.views import generic


class HomeView(generic.TemplateView):
    template_name = "static_web/home.html"


class AboutView(generic.TemplateView):
    template_name = "static_web/about.html"


class ClasesView(generic.TemplateView):
    template_name = "static_web/classes.html"


class ContactView(generic.TemplateView):
    template_name = "static_web/contact.html"


class ScheduleView(generic.TemplateView):
    template_name = "static_web/schedule.html"


class TrainerView(generic.TemplateView):
    template_name = "static_web/trainer.html"
