import re
from django import forms
from .models import RegisterModel
class Register(forms.ModelForm):

    class Meta:
        model = RegisterModel
        fields = "__all__"

    def clean(self):
        super(Register, self).clean()
        email = self.cleaned_data.get('email')
        print(email)
        url = self.cleaned_data.get('url')
        print(url)
        phone = self.cleaned_data.get('phone')
        print(phone)
        aadhar = self.cleaned_data.get('aadhar')
        print(aadhar)
        img = self.cleaned_data.get("img")
        print(img.size)
        if img:
            if img.size > 500 * 1024:
                raise forms.ValidationError("Invalid Image")
        else:
            raise forms.ValidationError("No image found")
        rphn = '[6789]\d{9}$'
        remail = '^[a-zA-Z0-9]+\.[a-zA-Z0-9-.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
        radhar = "^[^0-1]{1}\d{3}\d{4}\d{4}$"
        if re.match(remail, str(email)):
            pass
        else:
            raise forms.ValidationError("Invalid EmailID")
        if (re.search(rphn, str(phone))):
            pass
        else:
            raise forms.ValidationError("Invalid PhoneNO")
        if (re.match(radhar, str(aadhar))):
            pass
        else:
            raise forms.ValidationError("Invalid Aadhar")
        if str(url).endswith(".com") or str(url).endswith(".edu") or str(url).endswith(".org") or str(url).endswith(".in"):
            pass
        else:
            raise forms.ValidationError("Invalid URL")


