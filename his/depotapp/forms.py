from django import forms
from models import *
import itertools

def anyTrue(predicate, sequence):
    return True in itertools.imap(predicate, sequence)
def endsWith(s, *endings):
    return anyTrue(s.endswith, endings)

class ProductForm(forms.ModelForm):
  
    class Meta:
        model = Product 
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ProductForm, self).__init__(*args, **kwargs)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price<=0:
            raise forms.ValidationError("Should be larger than 0")
        return price

    def clean_image_url(self):
        url  = self.cleaned_data['image_url']
        if not endsWith(url.lower(), '.jpg', '.png', '.gif'):
            raise forms.ValidationError("Should be end with .jpg, png or gif")
        return url