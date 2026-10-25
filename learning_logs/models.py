from django.db import models

"""Models são classes responsáveis por criar um objeto que referencia uma tabela em um banco de dados"""
# Create your models here.


class Topic(models.Model):
    """Topico sobre o assunto sobre o qual o usuario esteja estudando"""
    
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        """Devolve uma representação em string do modelo"""
        
        return self.text


class Entry(models.Model):
    
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        verbose_name_plural = 'entries'
        
    def __str__(self):
        return self.text[:50]+"..."