from django.shortcuts import render
from rest_framework import status
from rest_framework.serializers import SerializerMetaclass
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
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
# permission_class = [IsAuthenticated]   - means it requires authentication

# if method =="GET"
# elif method == "POST"  --can make multiple methods on the same URL

# class ResidentList(APIView):

#     permission_class = [IsAuthenticated]

#     def get(self, request):
#         residents = Resident.objects.all()
#         serializer = ResidentSerializer(residents, many=True)
#         return Response(serializer.data)


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
def get_resident_byId(request, id):
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
        resident.is_active = False
        resident.is_archived = True
        serializer = ResidentSerializer(resident, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def get_notes_byResident(request, id):
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
def get_notes_byId(request, note_id):
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