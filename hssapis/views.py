from re import T
from rest_framework.response import Response
from rest_framework.decorators import api_view
from . import models
from . import serializers

# Create your views here.

@api_view(['GET'])
def get_apis(request):
    routes = [
        'api/people/faculties',
        'api/people/students',
        'api/people/staff',

        'api/events/conf-workshops-presentations',
        'api/events/awards',
        'api/events/talks',

        'api/research',

        'api/acads',
        'api/committees',

        'api/home',
        'api/home/announcements/',
        'api/home/news/',
        'api/home/phd_awarded/',
    ]
    return Response(routes)

# Home
@api_view(['GET'])
def get_home(request):
    return Response("Home")

@api_view(['GET'])
def get_announcements(request):
    return Response(serializers.AnnouncementSerializer(models.Announcement.objects.all(), many=True).data)

@api_view(['GET'])
def get_news(request):
    return Response(serializers.NewsSerializer(models.News.objects.all(), many=True).data)

@api_view(['GET'])
def get_phd_awarded(request):
    return Response(serializers.Phd_awardedSerializer(models.Phd_awarded.objects.all(), many=True).data)

# Research
@api_view(['GET'])
def get_projects(request):
    proj_on = serializers.ProjectSerializer(models.Project.objects.filter(completed=False), many=True).data
    proj_completed = serializers.ProjectSerializer(models.Project.objects.filter(completed=True), many=True).data
    return Response([proj_on, proj_completed])

# About - Committees
@api_view(['GET'])
def get_committees(request):
    dapc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DAPC"), many=True).data
    drc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DRC"), many=True).data
    dsmc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DSMC"), many=True).data
    dwmc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DWMC"), many=True).data
    safety = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="Safety"), many=True).data
    dfsc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DFSC"), many=True).data
    dfac = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DFAC"), many=True).data
    dac = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DAC"), many=True).data
    dpc = serializers.CommitteePersonSerializer(models.CommitteePerson.objects.filter(committee__icontains="DPC"), many=True).data
    return Response([dapc, drc, dsmc, dwmc, safety, dfsc, dfac, dac, dpc])


# People 
@api_view(['GET'])
def get_students(request):
    students = models.Student.objects.all()
    serializer = serializers.StudentSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_staff(request):
    staff = models.Office_staff.objects.all()
    serializer = serializers.StaffSerializer(staff, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_faculties(request):
    faculty_list = models.Faculty.objects.all()
    serializer = serializers.FacultySerializer(faculty_list, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_people(request):
    return Response("People")


# Events
@api_view(['GET'])
def get_talks(request):
    past_talks = serializers.Past_TalkSerializer(models.Past_Talk.objects.all(), many=True).data
    special_talk = serializers.Special_TalkSerializer(models.Special_Talk.objects.all(), many=True).data
    return Response([past_talks, special_talk])

@api_view(['GET'])
def get_awards(request):
    awards = serializers.AwardSerializer(models.Award.objects.all(), many=True).data
    return Response(awards)

@api_view(['GET'])
def get_work(request):
    work_list = serializers.Conf_Work_PresSerializer(models.Conf_Work_Pres.objects.filter(type="Workshop"), many=True).data
    conf_list = serializers.Conf_Work_PresSerializer(models.Conf_Work_Pres.objects.filter(type="Conference"), many=True).data
    pres_list = serializers.Conf_Work_PresSerializer(models.Conf_Work_Pres.objects.filter(type="Presentation"), many=True).data
    return Response([work_list, pres_list, conf_list])

@api_view(['GET'])
def get_events(request):
    return Response("Events")