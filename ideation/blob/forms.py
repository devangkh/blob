from django import forms

class BlobTextForm(forms.Form):
	blobtext = forms.CharField()