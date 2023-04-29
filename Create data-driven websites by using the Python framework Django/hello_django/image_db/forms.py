# from django import forms

# from .models import Images


# class ImageForm(forms.ModelForm):
#     class Meta:
#         model = Images
#         fields = ('django_image',)


#         def save(self,commit=True):
#             print("--------- saving-------------")
#             image = self.cleaned_data['django_image'].file.read()
#             imageModel = super().save(commit=False)
#             imageModel.db_image = image
#             if commit:
#                 imageModel.save()
#             return imageModel
from django import forms
from .models import Images

class ImageForm(forms.ModelForm):
    django_image = forms.ImageField()
    db_image = forms.CharField(widget=forms.HiddenInput(),required=False)

    class Meta:
        model = Images
        fields = ('django_image', 'db_image')

    def save(self, commit=True):
        instance = super(ImageForm, self).save(commit=False)

        # Read the binary data from the uploaded file
        image_binary = self.cleaned_data['django_image'].file.read()

        # Save the binary data to the binary field
        instance.db_image = image_binary

        if commit:
            instance.save()
        return instance
