from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    image = models.ImageField(upload_to='projects')  # Dentro del directorio media donde guardamos,
    # las fotos de cada registro de proyecto, creará una carpeta llamada proyecto.
    created = models.DateTimeField(auto_now_add=True)  # Se añadirá hora cuando se cree por primera vez
    updated = models.DateTimeField(auto_now=True)  # Se ejecuta cada vez que se actualize
    url_opcional = models.URLField(null=True, blank=True)

    class Meta:
        ordering = ['-created']  # Ordenación de creación de más nuevo a más antiguo.

    def __str__(self):
        return self.title  # Mostrará con el título del proyecto la nueva creación de proyecto.
