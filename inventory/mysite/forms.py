from django import forms
from mysite.models import StoreManager,Inventory

class StoreManagerForm(forms.ModelForm):

    class Meta:
        model = StoreManager
        fields = ('username', 'password','email')
        widgets = {
        'password': forms.PasswordInput(),
    }

class InventoryForm(forms.ModelForm):
    class Meta:
        model = Inventory
        fields = ('productName','vendor','MRP','batchNum','quantity','status')
