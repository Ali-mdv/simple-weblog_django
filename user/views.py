from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from article.models import Article
from django.urls import reverse_lazy
from .mixins import FieldMixin, FormValidMixin ,AuthorAccessMixin ,SuperAccessUserMixin ,AuthorsMixin
from django.shortcuts import get_object_or_404
from user.models import User
from .forms import ProfileForm
from django.contrib.auth.views import LoginView ,PasswordChangeView
from django.urls import reverse

from django.http import HttpResponse
from django.contrib.auth import login, authenticate
from .forms import SignupForm
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from .tokens import account_activation_token
from django.core.mail import EmailMessage
# Create your views here.

#@login_required
#def home(request):
#return render(request,'registration/home.html')


class Home(LoginRequiredMixin,ListView):
    template_name = 'registration/home.html'

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Article.objects.all()
        else:
            return Article.objects.filter(author=self.request.user)


class CreateArticle(AuthorsMixin,FieldMixin,FormValidMixin,CreateView):
    model = Article
    template_name = 'registration/create-update.html'
    # success_url = reverse_lazy('account:home')


class UpdateArticle(AuthorsMixin,FieldMixin,FormValidMixin,UpdateView):
    model = Article
    template_name = 'registration/create-update.html'
    # success_url = reverse_lazy('account:home')

    def get_object(self):
        pk = self.kwargs.get('pk')
        return get_object_or_404(Article,pk=pk)


class DeleteArticle(SuperAccessUserMixin,DeleteView):
    model = Article
    template_name = 'registration/delete-article.html'
    success_url = reverse_lazy('account:home')



class Profile(LoginRequiredMixin,UpdateView):
    form_class = ProfileForm
    template_name = 'registration/profile.html'
    success_url = reverse_lazy('account:profile')

    def get_object(self):
        return User.objects.get(pk=self.request.user.pk)


    def get_form_kwargs(self):
        kwargs = super(Profile, self).get_form_kwargs()
        kwargs.update({'user':self.request.user})
        return kwargs



class Login(LoginView):
    def get_success_url(self):
        user = self.request.user

        if user.is_superuser or user.is_author:
            return reverse('account:home')
        else:
            return reverse('account:profile')


class Signup(CreateView):
    form_class = SignupForm
    template_name = 'registration/signup.html'

    def form_valid(self,form):
        user = form.save(commit=False)
        user.is_active = False
        user.save()
        current_site = get_current_site(self.request)
        mail_subject = 'فعال سازی حساب کاربری.'
        message = render_to_string('registration/acc_active_email.html', {
            'user': user,
            'domain': current_site.domain,
            'uid':urlsafe_base64_encode(force_bytes(user.pk)),
            'token':account_activation_token.make_token(user),
        })
        to_email = form.cleaned_data.get('email')
        email = EmailMessage(
                    mail_subject, message, to=[to_email]
        )
        email.send()
        return HttpResponse('ایمیل فعال سازی برای شما ارسال شد. برای فعال سازی حساب بر روی لینک کلیک کنید تا حساب کاربری شما فعال شود.')



def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        # return redirect('home')
        return HttpResponse('<p>حساب کاربری شما با موفقیت فعال شد برای ورود <a href="/login" >کلیک</a> کنید. </p>')
    else:
        return HttpResponse('<p>لینک فعال سازی منقضی شده است برای تکرار فراید <a href="/signup" >کلیک</a> کنید. </p>')