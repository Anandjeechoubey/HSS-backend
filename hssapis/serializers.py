from re import M
from django.db.models import fields
from rest_framework import serializers
from . import models

class FacultySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Faculty
        fields = '__all__'

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Student
        fields = '__all__'

class StaffSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Office_staff
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.News
        fields = '__all__'

class AnnouncementSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Announcement
        fields = '__all__'

class Phd_awardedSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Phd_awarded
        fields = '__all__'

class AwardSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Award
        fields = '__all__'

class CommitteePersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CommitteePerson
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Project
        fields = '__all__'

class Past_TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Past_Talk
        fields = '__all__'

class Special_TalkSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Special_Talk
        fields = '__all__'

class Conf_Work_PresSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Conf_Work_Pres
        fields = '__all__'