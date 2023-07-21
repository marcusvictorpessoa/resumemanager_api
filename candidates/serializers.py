from rest_framework import serializers

from .models import Candidate

class CandidateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Candidate
        fields = (
            'id',
            'name',
            'phone',
            'experience_area',
            'resume',
            'resume_avaliation',
            'note',
            'created_at',
            'updated_at',
            'deleted'
        )
        extra_kwargs = {
            'id': {'read_only': True},
            'note': {'required': False},
            'created_at': {'read_only': True},
            'updated_at': {'read_only': True},
            'deleted': {'read_only': True}
        }