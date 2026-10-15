from django.db import models

# Create your models here.
class ObjetoPerdido(models.Model):
    CATEGORIAS = [
        ('Electronico', 'Electronico'),
        ('Documento o tarjeta', 'Documento o tarjeta'),
        ('Bolso, mochila o maleta', 'Bolso, mochila o maleta'),
        ('Ropa y accesorios', 'Ropa y accesorios'),
        ('Llaves', 'Llaves'),
        ('Otro', 'Otro'),
    ]
    ESTADOS = [
        ('En custodia', 'En custodia'),
        ('Entregado a su dueño', 'Entregado a su dueño'),
        ('Donado', 'Donado'),
    ]

    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=60, verbose_name='Objeto')
    categoria = models.CharField(max_length=30, choices=CATEGORIAS, verbose_name='Categoria')
    descripcion = models.TextField(verbose_name='Descripcion')
    lugar_hallazgo = models.CharField(max_length=80, verbose_name='Lugar donde se encontro')
    fecha_hallazgo = models.DateField(verbose_name='Fecha del hallazgo (dd/mm/aaaa)')
    encontrado_por = models.CharField(max_length=60, verbose_name='Funcionario que lo encontro')
    correo_funcionario = models.EmailField(verbose_name='Correo del funcionario')
    valor_estimado = models.PositiveIntegerField(verbose_name='Valor estimado ($)')
    estado = models.CharField(max_length=30, choices=ESTADOS, default='En custodia', verbose_name='Estado')
    imagen = models.ImageField(upload_to='objetos/', verbose_name='Fotografia')

    def __str__(self):
        fila = 'Objeto: ' + self.nombre + ' - Estado: ' + self.estado
        return fila

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
