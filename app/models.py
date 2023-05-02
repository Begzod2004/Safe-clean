from django.db import models



class UnitOfMeasure(models.Model): # O'lchov birligi uchun
    name = models.CharField(max_length=50)
    value = models.PositiveIntegerField()
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Image(models.Model): 
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/picture/', blank=True, null=True)
    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/category/', blank=True, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class Service(models.Model):
    name = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.FloatField()
    unit_of_measure = models.ForeignKey(UnitOfMeasure, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    images = models.ManyToManyField(Image, blank=True)

    def __str__(self):
        return self.name
    

class Client(models.Model):
    fio = models.CharField(max_length=150, verbose_name="Toliq ism familyasi")
    phone_number1 = models.IntegerField()
    phone_number2 = models.IntegerField()

    def __str__(self):
        return self.fio

STATUS = (
    ('Created', 'Created'),
    ('Paid', 'Paid'),
    ('Rejected', 'Rejected')
)


VIOW = (
    ('Kordi', 'Kordi'),
    ('Kormadi', 'Kormadi')
)


class Order(models.Model):
    name = models.CharField(max_length=50)
    price = models.FloatField()
    quantity = models.IntegerField()
    status = models.CharField(choices=STATUS, max_length=20)
    created = models.DateField(auto_now=True)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    status_viowed = models.CharField(choices=VIOW, max_length=20)

    def __str__(self):
        return self.name
    

class OrderDetails(models.Model):
    lacation = models.CharField(max_length=150)
    craeted = models.DateField(auto_now=True)
    order_id = models.ForeignKey(Order, on_delete=models.CASCADE)

    def __str__(self):
        return self.lacation
    

class ImageOrgan(models.Model): 
    name = models.CharField(max_length=50)
    image = models.ImageField(upload_to='media/picture/', blank=True, null=True)
    
    def __str__(self):
        return self.name



class Creater(models.Model): 
    fio = models.CharField(max_length=50, verbose_name="Toliq isim familyasi")
    picture = models.ImageField(upload_to='media/creaters/', blank=True, null=True)
    less_info = models.CharField(max_length=100)
    def __str__(self):
        return self.fio



class Contact(models.Model): 
    phone_number = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    telegram = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    youtube = models.CharField(max_length=50)
    facebook = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    def __str__(self):
        return self.fio


class Organation(models.Model):
    name = models.CharField(max_length=59)
    logo = models.ImageField(upload_to='media/logo/', blank=True, null=True)
    description = models.TextField()
    image = models.ForeignKey(ImageOrgan, on_delete=models.CASCADE)
    creaters = models.ForeignKey(Creater, on_delete=models.CASCADE)
    cantact = models.ForeignKey(Contact, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Vakansiya(models.Model):
    fio = models.CharField(max_length=50, verbose_name="Toliq isim familyasi")    
    phone_number = models.CharField(max_length=50)
    vakansiya_name = models.CharField(max_length=50)
    description = models.TextField()
    status_viowed = models.CharField(choices=VIOW, max_length=20)
    is_active = models.BooleanField(default=True)
    craeted = models.DateField(auto_now=True)

    def __str__(self):
        return self.fio
    

