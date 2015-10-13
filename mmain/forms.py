from mmain.models import Cereal, Manufacturer
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, HTML, Layout, Div
from crispy_forms.bootstrap import FormActions

class UserSignUp(forms.Form):  
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class UserLogin(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(widget=forms.PasswordInput(), required=True)

class Search(forms.Form):
    search = forms.CharField(required=False)

class CreateCerealForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = '__all__'
        
    def __init__(self, *args, **kwargs):
        super(CreateCerealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/create_cereal/'

        self.helper.layout.append(
                FormActions(
                    Submit('submit', 'Submit', css_class="btn-primary")
                )  
            )


class UpdateCerealForm(forms.ModelForm):
    class Meta:
        model = Cereal
        fields = ['manufacturer', 'cereal_type', 'calories', 'protein', 'fat', 'sodium', 'dietary_fiber', 'carbs', 'sugars', 'display_shelf', 'potassium', 'vitamins_and_minerals', 'serving_size_weight', 'potassium', 'cups_per_serving']

    def __init__(self, *args, **kwargs):
        super(UpdateCerealForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/update_cereal/%s/' % self.instance.pk 

        self.helper.layout.append(
                FormActions(
                    Submit('submit', 'Submit', css_class="btn-primary")
                )  
            )


class CreateManufacturerForm(forms.ModelForm):
    class Meta:
        model = Manufacturer
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(CreateManufacturerForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_action = '/create_manufacturer/'

        self.helper.layout.append(
                FormActions(
                    Submit('submit', 'Submit', css_class="btn-primary")
                )  
            )

