from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import OR, IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes

from .models import Resident
from .models import Note
from .models import Activity
from .models import Participation
from .models import Assessment

from .serializers import ResidentSerializer
from .serializers import NoteSerializer
from .serializers import ActivitySerializer
from .serializers import ParticipationSerializer
from .serializers import AssessmentSerializer

from django.contrib.auth import get_user_model
User = get_user_model()


# permission_classes = [AllowAny]     - means anyone can access this endpoint


@api_view(['GET', 'POST',])
@permission_classes([IsAuthenticated])
def get_all_residents(request):

    if request.method == 'GET':
        residents = Resident.objects.filter(user_id = request.user.id).filter(is_active = True)
        serializer = ResidentSerializer(residents, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = ResidentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_archived_residents(request):
    residents = Resident.objects.filter(user_id = request.user.id).filter(is_archived = True)
    serializer = ResidentSerializer(residents, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'PATCH'])
@permission_classes([IsAuthenticated])
def get_resident_by_id(request, id):
    if request.method == 'GET':
        resident = Resident.objects.get(id = id)
        serializer = ResidentSerializer(resident)
        return Response(serializer.data)

    if request.method == 'PUT':
        resident = Resident.objects.get(id = id)
        serializer = ResidentSerializer(resident, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PATCH':
        resident = Resident.objects.get(id = id)
        resident.is_active = not resident.is_active
        resident.is_archived = not resident.is_archived
        serializer = ResidentSerializer(resident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_notes_by_resident(request, id):
    if request.method == 'GET':
        notes = Note.objects.filter(resident_id = id)
        serializer = NoteSerializer(notes, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = NoteSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(resident_id = id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def get_notes_by_id(request, note_id):
    if request.method == 'DELETE':
        note = Note.objects.get(id = note_id)
        note.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    if request.method == 'PUT':
        note = Note.objects.get(id = note_id)
        serializer = NoteSerializer(note, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_all_activities(request):
    if request.method == 'GET':
        activities = Activity.objects.filter(user = request.user)
        serializer = ActivitySerializer(activities, many=True)
        return Response (serializer.data)

    if request.method == 'POST':
        serializer = ActivitySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user = request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'DELETE', 'PATCH'])
@permission_classes([IsAuthenticated])
def edit_activities(request, id):
    if request.method=='PUT':
        activity = Activity.objects.get(id = id)
        serializer=ActivitySerializer(activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        
    if request.method=='DELETE':
        activity = Activity.objects.get(id = id)
        activity.delete()
        return Response(status=status.HTTP_202_ACCEPTED)

    if request.method=='PATCH':
        activity = Activity.objects.get(id = id)
        activity.is_active = not activity.is_active
        activity.is_archived = not activity.is_archived
        serializer = ActivitySerializer(activity, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(status=status.HTTP_202_ACCEPTED)
    return Response(status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def activities_by_dow(request, dow):
    if request.method == 'GET':
        activity_one = Activity.objects.all().filter(dow_one = dow)
        activity_two = Activity.objects.all().filter(dow_two = dow)
        activity_three = Activity.objects.all().filter(dow_three = dow)
        activity = activity_one | activity_two | activity_three
        serializer = ActivitySerializer(activity, many=True)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

@api_view(['GET', 'POST', 'DELETE', 'PUT'])
@permission_classes([IsAuthenticated])
def assessments(request, id):
    if request.method == 'GET':
        assessment = Assessment.objects.get(resident_id = id)
        serializer = AssessmentSerializer(assessment)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = AssessmentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(resident_id = id)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        assessment = Assessment.objects.get(resident_id = id)
        assessment.delete()
        return Response(status=status.HTTP_200_OK)

    if request.method == 'PUT':
        assessment = Assessment.objects.get(resident_id = id)
        serializer = AssessmentSerializer(assessment, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
