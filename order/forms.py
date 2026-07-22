from django.forms import ModelForm

class ProductForm(ModelForm):
    class Meta:
        fields = ["name","price","stock"]