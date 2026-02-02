from django.db import models
from django_ckeditor_5.fields import CKEditor5Field

class ProjectGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Technology(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Project(models.Model):
    group = models.ForeignKey(ProjectGroup, on_delete=models.CASCADE, related_name='projects')
    title = models.CharField(max_length=200)
    technologies = models.ManyToManyField(Technology, blank=True)
    description = CKEditor5Field('Description', config_name='extends')
    github_link = models.URLField(max_length=200, blank=True)
    
    def __str__(self):
        return self.title

def project_image_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/projects/<project_title>/<filename>
    return f'projects/{instance.project.title}/{filename}'

class ProjectImage(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to=project_image_path)

    def __str__(self):
        return f"Image for {self.project.title}"