from .forms import ContactForm
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from django.core.mail import EmailMessage, send_mail


class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        # It should return an HttpResponse.

        message = '{name} / {email} said: \n{subject}\n\n{content}'.format(
            name=form.cleaned_data.get('name'),
            email=form.cleaned_data.get('email'),
            subject=form.cleaned_data.get('subject'),
            content=form.cleaned_data.get('content')       
            )

        email = EmailMessage(
            form.cleaned_data.get('subject'),
            message,
            'WebFormContactSantMarys@gmail.com',
            ['reddevil_cero@hotmail.com'],
            headers={'Reply-To': form.cleaned_data.get('email')}
        )
        email.send()
        return super(ContactView, self).form_valid(form)

    def get_success_url(self):
            return reverse_lazy('contact')+'?ok'