from django.db import models
import uuid
from users.models import Profile
from datetime import datetime
# Create your models here.



class Project(models.Model):
    owner = models.ForeignKey(
        Profile,null=True,blank=True,on_delete=models.CASCADE
    )
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True,editable=False)
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    featured_image = models.ImageField(null=True,blank=True,default="default.jpg")
    demo_link = models.CharField(max_length=20000,null=True,blank=True)
    source_link = models.CharField(max_length=20000,null=True,blank=True)
    tags = models.ManyToManyField('Tag',blank=True)
    vote_total = models.IntegerField(default=0,null=True,blank=True)
    vote_ratio = models.IntegerField(default=0,null=True,blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering=['-created','-vote_ratio','-vote_total','title']


    @property
    def imageUrl(self):
        try:
            url = self.featured_image.url
        except:
            url = ''
        return url

    @property
    def reviewers(self):
        queryset = self.review_set.all().values_list('owner__id',flat=True)
        return queryset

    @property
    def getVoteCount(self):
        reviews = self.review_set.all()
        upVote = reviews.filter(value="up").count()
        totalVotes = reviews.count()
        ratio = (upVote//totalVotes)*100
        self.vote_total = totalVotes
        self.vote_ratio = ratio
        self.save()

    def __str__(self):
        return self.title

class Review(models.Model):
    vote_type = (
        ('up','Up Vote'),
        ('down','Down Vote'),
    )
    owner = models.ForeignKey(Profile,on_delete=models.CASCADE,null=True)
    project = models.ForeignKey(Project,on_delete=models.CASCADE)
    body  = models.TextField(null=True,blank = True)
    value = models.CharField(max_length=200,choices = vote_type)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True,editable=False)

    class Meta:
        unique_together = [['owner','project']]
    def __str__(self):
        return self.value

class Tag(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now_add=True)
    id = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True,editable=False)

    def __str__(self):
        return self.name



# adding posts for feed

class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.CharField(max_length = 100)
    image = models.ImageField(null=True,blank=True,default="default.jpg")
    caption = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)
    no_of_like = models.IntegerField(null=True,default=0)
    liked_by = []

    def __str__(self):
        return self.user


class LikePost(models.Model):
    post_id = models.CharField(max_length = 500)
    username = models.CharField(max_length=100)

    def __str__(self):
        return self.username


# Job Postings

class Jobs(models.Model):
    id          = models.UUIDField(default = uuid.uuid4, unique=True,primary_key=True,editable=False)
    title       = models.CharField(null=False,max_length = 500)
    location    = models.CharField(null=True,max_length = 500)
    featured_image = models.ImageField(null=True,blank=True,default="default-job.jpg")
    description = models.CharField(null=False,max_length = 5000)
    requirements = models.CharField(null=False,max_length = 5000)
    job_type = models.CharField(null=False,max_length = 100)
    company_name = models.CharField(null=False,max_length = 100)
    tags = models.ManyToManyField('Tag',blank=True)
    is_remote   = models.BooleanField()
    is_featured = models.BooleanField()
    apply_link = models.URLField(max_length = 20000)
    demo_video = models.URLField(max_length = 20000)

    def __str__(self):
        return self.title
