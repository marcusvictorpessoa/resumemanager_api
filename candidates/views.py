from django.shortcuts import render

# Create your views here.
from rest_framework import mixins, viewsets, status
from rest_framework.response import Response
from .serializers import CandidateSerializer
from .models import Candidate
import uuid

class CandidatesController(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    queryset = Candidate.objects.all()
    serializer_class = CandidateSerializer

    # generate uuid hash of the resume before save in DB - DONE

    def create(self, request, *args, **kwargs):
        try:
            #new_filename = uuid.uuid4()
            request.data.get('resume').name = f'{uuid.uuid4()}.pdf'
        except:
            return Response({'detail': 'Erro ao gerar nome único do currículo'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return super().create(request, *args, **kwargs)

    '''def list(self, request, *args, **kwargs):
        candidates = self.filter_queryset(Candidate.objects.filter(deleted=False))
        results = self.paginate_queryset(candidates)
        serializer = self.get_serializer(results, many=True)
        return self.get_paginated_response(serializer.data)
        #return super().list(request, *args, **kwargs)

    def retrieve(self, request, *args, **kwargs):
        candidate = self.get_object()
        if candidate.deleted:
            return Response({'Candidato deletado'}, status=status.HTTP_400_BAD_REQUEST)
        return super().retrieve(request, *args, **kwargs)
    
    def update(self, request, *args, **kwargs):
        candidate = self.get_object()
        if candidate.deleted:
            return Response({'Candidato deletado'}, status=status.HTTP_400_BAD_REQUEST)
        return super().update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        candidate = self.get_object()
        if candidate.deleted:
            return Response({'Candidato deletado'}, status=status.HTTP_400_BAD_REQUEST)
        return super().partial_update(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        candidate = self.get_object()
        if candidate.deleted:
            return Response({'Candidato já deletado'}, status=status.HTTP_400_BAD_REQUEST)
        candidate.deleted = True
        candidate.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
        #return super().destroy(request, *args, **kwargs)'''