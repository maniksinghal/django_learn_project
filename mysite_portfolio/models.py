from django.db import models

#Create a model inheriting from Django's model


"""
Our portfolio would contain, say multiple courses
Each course having:
- An image (thumbnail)
- A title
- A description
- A target URL when we click the course.
"""
class Project(models.Model):
    #Google Django model field reference for more information
    title = models.CharField(max_length=100)
    description = models.CharField(max_length=250)

    #!! Working with images requires: pip3 install pillow
    #Update MEDIA_ROOT in settings.py (= BASE_DIR + media/)
    #Update MEDIA_URL in settings.py (Just any path-name)
    #Update urlpatterns (add a static) in urls.py (map Media URL to ROOT)
    image = models.ImageField(upload_to='mysite_portfolio/images/')
    # The image URL would be finally <root>/media_url/mysite_portfolio/images/

    url = models.URLField(blank=True)  #blank=True means the field is optional

    #Once the model is created, we need to inform about it to the database
    #python3 manage.py makemigrations   #Create a migration for this model
    #python3 manage.py migrate          #Migrate this model to the database
    #Checkout mysite_portfolio/migrations/__init__.py

    #Working with admin
    #Create admin credentials
    # - python3 manage.py createsuperuser  (changepassword maniksin)
    # - username: maniksin, password: default
    #   - can use python3 manage.py changepassword maniksin

    #Register my model to admin in admin.py

