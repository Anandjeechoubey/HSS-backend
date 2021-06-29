from django.db import models

# Create your models here.


## People ##
# Faculties
FacultyType = [
    ("Head Of Department","Head Of Department"),
    ("Professor","Professor"),
    ("Assistant Professor", "Assistant Professor"),
    ("Associate Professor", "Associate Professor"),
    ("Retired Faculty", "Retired Faculty"),
]

class Faculty(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    img = models.ImageField( upload_to='faculty/', blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    phone = models.CharField(max_length=10, null=True, blank=True)
    interests = models.TextField(null=True, blank=True)
    faculty_profile = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=20, choices = FacultyType, default="Professor")

    def __str__(self):
        return self.name

# Students 
StudentType = [
    ("Full Time", "Full Time"),
    ("Part Time", "Part Time"),
]
class Student(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    img = models.ImageField( upload_to='student/', blank=True, null=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    joined = models.IntegerField(null=True, blank=True)
    discipline = models.CharField(max_length=30, null=True, blank=True)
    research = models.CharField(max_length=200, null=True, blank=True)
    supervisor = models.CharField(max_length=200, null=True, blank=True)
    thesis = models.TextField(null=True, blank=True)
    student_profile = models.URLField(blank=True, null=True)
    type = models.CharField(max_length=20, choices= StudentType, default="Full Time")

    def __str__(self):
        return self.name


# Office Staff
class Office_staff(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    img = models.ImageField( upload_to='staff/', blank=True, null=True)
    designation = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name



## Home #
#Announcements
class Announcement(models.Model):
    date = models.CharField(max_length=25, null=True, blank=True)
    headline = models.CharField(max_length=200, null=True, blank=True)
    attachments = models.FileField(upload_to='announcements/', blank=True, null=True)

    def __str__(self):
        return self.headline + ' - ' + str(self.date)

class News(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    subtext = models.TextField(blank=True, null=True)
    img = models.ImageField( upload_to='news/', blank=True, null=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.headline

class Phd_awarded(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    thesis = models.TextField(blank=True, null=True)
    img = models.ImageField( upload_to='phd_awarded/', blank=True, null=True)
    disicpline = models.CharField(max_length=20, null=True, blank=True)
    supervisor = models.CharField(max_length=100, null=True, blank=True)
    link = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


## About #
# Committee People
CommitteeList = [
    ("Departmental Professorial Committee (DPC)","Departmental Professorial Committee (DPC)"),
    ("Departmental Administrative Committee (DAC)","Departmental Administrative Committee (DAC)"),
    ("Department Faculty Assessment Committee (DFAC)","Department Faculty Assessment Committee (DFAC)"),
    ("Departmental Faculty Search Committee (DFSC)","Departmental Faculty Search Committee (DFSC)"),
    ("Safety Committee","Safety Committee"),
    ("Department Web Management Committee (DWMC)","Department Web Management Committee (DWMC)"),
    ("Department Space Management Committee (DSMC)","Department Space Management Committee (DSMC)"),
    ("Department Research Committee (DRC)","Department Research Committee (DRC)"),
    ("Department Academic Programme Committee (DAPC)","Department Academic Programme Committee (DAPC)"),
]
class CommitteePerson(models.Model):
    committee = models.CharField(max_length=100, choices=CommitteeList, null=True, blank=True)
    name = models.CharField(max_length=40, null=True, blank=True)
    img = models.ImageField( upload_to='committee/', blank=True, null=True)
    designation = models.CharField(max_length=30, null=True, blank=True)

    def __str__(self):
        return self.name + " " + self.committee


## Research #
# Projects
class Project(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    durations = models.IntegerField(blank=True, null=True)
    project_by = models.CharField(max_length=30, null=True, blank=True)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.headline + ' - ' + self.project_by

## Events #
# Awards
class Award(models.Model):
    name = models.CharField(max_length=40, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' - '

#talks
class Past_Talk(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name + ' ' + self.date

class Special_Talk(models.Model):
    name = models.CharField(max_length=100, null=True, blank=True)
    date = models.CharField(max_length=25, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    img1 = models.ImageField( upload_to='special_talk/', blank=True, null=True)
    img2 = models.ImageField( upload_to='special_talk/', blank=True, null=True)
    img3 = models.ImageField( upload_to='special_talk/', blank=True, null=True)

    def __str__(self):
        return self.name + " " + self.date

# Conference / Workshop / Presentations
event_type = [
    ('Conference','Conference'),
    ('Workshop','Workshop'),
    ('Presentation','Presentation'),
]
class Conf_Work_Pres(models.Model):
    headline = models.CharField(max_length=100, null=True, blank=True)
    place = models.CharField(max_length=20, null=True, blank=True)
    date = models.CharField(max_length=25, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    type = models.CharField(max_length=20, choices=event_type, default="Conference")

    def __str__(self):
        return self.headline + ' ' + self.date