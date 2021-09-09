from django import forms
from user.models import User

from django.contrib.auth.forms import UserCreationForm

class ProfileForm(forms.ModelForm):
	def __init__(self,*args,**kwargs):
		user = kwargs.pop('user')
		
		super(ProfileForm, self).__init__(*args,**kwargs)

		if not user.is_superuser:
			self.fields['username'].disabled = True
			# self.fields['username'].help_text = None
			self.fields['email'].disabled = True
			self.fields['is_author'].disabled = True
			self.fields['special_user'].disabled = True
	
	class Meta:
		model = User
		fields = ['first_name','last_name','email','username','is_author','special_user','profile_photo','facebook_id','youtube_id','twitter_id','instagram_id']



class SignupForm(UserCreationForm):
    email = forms.EmailField(max_length=200, help_text='Required')    

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')