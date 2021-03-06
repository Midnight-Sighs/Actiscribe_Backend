from rest_framework import serializers
from .models import Resident
from .models import Note
from .models import Activity
from .models import Participation
from .models import Assessment

class ResidentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Resident
        fields = ['id','r_first_name', 'r_last_name', 'r_other_identifier', 'is_active', 'is_archived', 'last_assessment']

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ['id','resident_id', 'note_date', 'content']

class ActivitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Activity
        fields = ['id', 'name','description', 'is_active', 'is_archived', 'dow_one', 'dow_two', 'dow_three']

class ParticipationSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Participation
        fields = ['id', 'activity_id', 'resident_id', 'date']

class AssessmentSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Assessment
        fields = ['nickname', 'games_yn', 'books_yn', 'music_yn', 'crafts_yn', 'arts_yn', 'learning_yn', 'gardening_yn', 'sports_yn', 'exercise_yn', 'outside_yn', 'animals_yn', 'socializing_yn','work','volunteer','parents','siblings', 'close_family','spouse', 'children', 'technology','city_or_country', 'travel','alone_fun','social_fun','one_thing']

