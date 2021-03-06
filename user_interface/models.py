from django.db import models
from django.contrib.auth.models import AbstractUser
import re 

Rating_range=[
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
    ('5','5'),
]

class User(AbstractUser):
    pass


class InformationModel(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    fullName =models.CharField( max_length=50, blank=True,null=True)
    bio =models.CharField(max_length=50, blank=True,null=True)
    about=models.TextField(blank=True,null=True)
    address= models.CharField(max_length=100,blank=True,null=True)
    email=models.EmailField(max_length=100,blank=True,null=True)
    phone=models.CharField( max_length=15,blank=True,null=True)
    avatar=models.ImageField(upload_to='avatar/', blank=True,null=True)
    CV= models.FileField(upload_to='cv/', max_length=100,blank=True,null=True)

    #Social Link
    github= models.URLField(blank=True,null=True)
    linkedin=models.URLField(blank=True,null=True)
    others=models.URLField(blank=True,null=True)

    def __str__(self):
        return self.fullName

class EducationModel(models.Model):
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    title= models.CharField( max_length=50, blank=True,null=True)
    the_year =models.CharField(max_length=50 ,blank=True,null=True)
    institude= models.CharField(max_length=50 ,blank=True,null=True)
    description=models.TextField(blank=True,null=True)


    class Meta:
        ordering=['-the_year']
    def __str__(self):
        return f"{self.user} => {self.title} from {self.institude}"

class ExprienceModel(models.Model):
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    title= models.CharField( max_length=50, blank=True,null=True)
    the_year =models.CharField(max_length=50 ,blank=True,null=True)
    institude= models.CharField(max_length=50 ,blank=True,null=True)
    description=models.TextField(blank=True,null=True)


    class Meta:
        ordering=['-the_year']
    def __str__(self):
        return f"{self.user} => {self.title} from {self.institude}"

class ProjectModel(models.Model):
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    title= models.CharField( max_length=50, blank=True,null=True)
    slug=models.SlugField(max_length=500, blank=True,null=True)
    imageLink=models.URLField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    skillrank=models.CharField(choices=Rating_range,blank=True,null=True,max_length=10)


    class Meta:
        ordering=['-skillrank']
    def __str__(self):
        return f"{self.user} => {self.title}"

class SkillSetModel(models.Model):
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    title= models.CharField( max_length=50, blank=True,null=True)
    imageLink=models.URLField(blank=True,null=True)
    description=models.TextField(blank=True,null=True)
    projectRating=models.CharField(choices=Rating_range,default="2",blank=True,null=True, max_length=10)
    demo=models.URLField(blank=True,null=True)
    githubLink=models.URLField(blank=True,null=True)


    class Meta:
        ordering=['-projectRating']
    def __str__(self):
        return f"{self.user} => {self.title}"
    def get_project_absolute_url(self):
        return "/projects/{}".format(self.slug)
    
    def save(self,*args,**kwargs):
        self.slug=self.slug_generate()
        super(Project,self).save(*args,**kwargs)
    def slug_generate(self):
        slug= self.title.strip()
        slug=re.sub("","_",slug)
        return slug.lower()

class MessageModel(models.Model):
    user= models.ForeignKey(User,  on_delete=models.CASCADE)
    name= models.CharField( max_length=50, blank=False,null=False)
    slug=models.SlugField(max_length=500, blank=False,null=False)
    email=models.EmailField( max_length=254,blank=False,null=False)
    message=models.TextField(blank=False,null=False)
    send_time= models.DateTimeField( auto_now_add=True)
    subject=models.CharField(blank=False,null=True, max_length=50)
    is_read=models.BooleanField(default=False)

    class Meta:
        ordering=['-send_time']
    def __str__(self):
        return f"{self.user} => {self.subject}"


