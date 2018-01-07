from django.db import models
from django.core.validators import RegexValidator

# Create your models here.


class URL(models.Model):
    """This class contains a reference to the URLField.

    It is part of a base of models comprising the webapp.

    """

    url = models.URLField(default='github.com/arikanev')

    def __str__(self):
        """Return human readable string of self.url."""
        return self.url


class Email(models.Model):
    """This class contains a reference to the EmailField.

    It is part of a base of models comprising the webapp.

    """

    email = models.EmailField(default='arikanevsky@gmail.com')

    def __str__(self):
        """Return human readable string of self.email."""
        return self.email


class Image(models.Model):
    """This class contains a reference to the ImageField.

    It is part of a base of models comprising the webapp.

    """
    uplpath = '%Y/%m/%d'
    dfltpath = 'Y/M/D/no_img.jpg'

    image = models.ImageField(upload_to=uplpath, default=dfltpath)

    def __str__(self):
        """Return human readable string of self.image."""
        return self.image.name


class Bio(models.Model):
    """This class contains a reference to the TextField.

    It is part of a base of models comprising the Page model.
    A core component of the webapp.

    """

    bio = models.TextField(default='Tell us about yourself. \
                           If you are concerned with internet anonymity, \
                           consider leaving this blank')

    def __str__(self):
        """Return human readable string of self.summary."""
        return self.summary


class User_ID(models.Model):
    """This class contains a reference to the CharField.

    It is part of a base of models comprising the Page model.
    A core component of the webapp.

    """

    user_id = models.CharField(validators=[RegexValidator(regex='^\w{4,6}$',
                               message='Length has to be 4',
                               code='nomatch')],
                               max_length=6)


class User(models.Model):
    """This class contains a reference to the CharField.

    It also establishes 4 one-to-one postgresql db relations for the
    Summary, Image, Email, User_ID, and URL classes.

    """

    bio = models.ForeignKey(Bio, on_delete=models.CASCADE)

    # one to one
    image = models.ForeignKey(Image, on_delete=models.CASCADE)

    # one to one
    email = models.ForeignKey(Email, on_delete=models.CASCADE)

    # one to one
    user_id = models.ForeignKey(User_ID, on_delete=models.CASCADE)

    # one to one
    url = models.ForeignKey(URL, on_delete=models.CASCADE)

    def __str__(self):
        """Return human readable string of self.summary."""
        user_description = list([self.bio,
                                 self.image,
                                 self.email,
                                 self.user_id,
                                 self.url])
        return str(user_description)
