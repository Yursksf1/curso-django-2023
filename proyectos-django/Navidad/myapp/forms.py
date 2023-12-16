from django import forms


class RecetaForm(forms.Form):
    receta = forms.CharField(label="Nombre", max_length=50)
    decripcion = forms.CharField(label="Descripcion", max_length=200)
    puntuacion = forms.IntegerField(label="Puntuacion")