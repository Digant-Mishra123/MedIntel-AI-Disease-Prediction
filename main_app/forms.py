# from django import forms
# from django.contrib.auth.models import User
# from .models import patient  # Assuming your model is named `Patient`

# class PatientSignupForm(forms.ModelForm):
#     password = forms.CharField(widget=forms.PasswordInput, label="Password")
#     password1 = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

#     class Meta:
#         model = patient
#         fields = ['user', 'name', 'age', 'gender', 'address', 'mobile_no', 'password', 'password1']
    
#     def clean_age(self):
#         age = self.cleaned_data.get('age')
#         if age < 1:
#             raise forms.ValidationError("Patient's age must be at least 1 year old.")
#         return age

#     def clean_email(self):
#         email = self.cleaned_data.get('email')
#         if User.objects.filter(email=email).exists():
#             raise forms.ValidationError("Email is already taken.")
#         return email

#     def clean_username(self):
#         username = self.cleaned_data.get('username')
#         if User.objects.filter(username=username).exists():
#             raise forms.ValidationError("Username is already taken.")
#         return username

#     def clean(self):
#         cleaned_data = super().clean()
#         password = cleaned_data.get("password")
#         password1 = cleaned_data.get("password1")
#         if password and password1 and password != password1:
#             raise forms.ValidationError("Passwords do not match.")
#         return cleaned_data
