from django import forms


class CommentForm(forms.Form):
    email = forms.EmailField(max_length=256, label='E-mail')
    first_name = forms.CharField(max_length=100, label='Nome')
    last_name = forms.CharField(max_length=100, label='Sobrenome')
    content = forms.CharField(
        max_length=800, widget=forms.Textarea, label='Comentário')

    def __init__(self, *args, **kargs):
        super().__init__(*args, **kargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholed': field
            })

            if field == 'content':
                self.fields[field].widget.attrs.update({'style': 'height: 200px;'})
