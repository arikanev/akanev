from django.db import models

# Create your models here.


class URL(models.Model):
    """This class contains a reference to the URLField.

    It is part of a base of models comprising the Bio app.

    """

    url = models.URLField(default='github.com/arikanev')

    def __str__(self):
        """Return human readable string of self.url."""
        return self.url


class Email(models.Model):
    """This class contains a reference to the EmailField.

    It is part of a base of models comprising the Bio app.

    """

    email = models.EmailField(default='arikanevsky@gmail.com')

    def __str__(self):
        """Return human readable string of self.email."""
        return self.email


class Image(models.Model):
    """This class contains a reference to the ImageField.

    It is part of a base of models comprising the Bio app.

    """

    image = models.ImageField(upload_to='page_images/%Y/%m/%d',
                              default='page_images/Y/M/D/no_img.jpg')

    def __str__(self):
        """Return human readable string of self.image."""
        return self.image.name


class Page(models.Model):
    """This class contains a reference to the CharField.

    It also establishes 3 one-to-one db relations for the
    Image, Email, and URL classes.

    """

    summary = models.TextField()

    # one to one
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    # one to one
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    # one to one
    url = models.ForeignKey(URL, on_delete=models.CASCADE)

    def __str__(self):
        """Return human readable string of self.summary."""
        return self.summary
