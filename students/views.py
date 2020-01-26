from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView


class StudentRegistrationView(CreateView):
    template_name = 'students/student/registration.html'
    form_class = UserCreationForm
    success_url = reverse_lazy('student_course_list')

    def form_valid(self, form):
        result = super(
            StudentRegistrationView,
            self
        ).form_valid(form)

        data = form.cleaned_data
        user = authenticate(
            username=data['username'],
            password=data['password1']
        )
        login(self.request, user)
        return result