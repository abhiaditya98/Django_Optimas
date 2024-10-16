# forms.py
from django import forms
from .models import ExistingRecords, SubmittedRecords

class RecordForm(forms.Form):
    field1 = forms.CharField(max_length=15, widget=forms.TextInput(attrs={'id': 'field1'}))
    location = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'id': 'location'}))

    def clean_field1(self):
        field1 = self.cleaned_data.get('field1')
        # if not ExistingRecords.objects.filter(field1=field1).exists():
        #     raise forms.ValidationError("Field1 value does not exist in the database.")
        return field1
# from django import forms
# from .models import ExistingRecords, SubmittedRecords
# class RecordForm(forms.ModelForm):
#     class Meta:
#         model = ExistingRecords
#         fields = ['field1']

#     def clean_field1(self):
#         field1 = self.cleaned_data.get('field1')
#         if field1:
#             # Check if field1 exists in the database
#             if ExistingRecords.objects.filter(field1=field1).exists():
#                 raise forms.ValidationError("Field 1 already exists.")
#             # Check if field1 is within the specified length
#             if not (9 <= len(field1) <= 15):
#                 raise forms.ValidationError("Field 1 must be between 9 and 15 characters.")
#         return field1