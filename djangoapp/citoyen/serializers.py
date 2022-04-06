from rest_framework import serializers
from citoyen.models import Citoyen


class CitoyenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citoyen
        fields = ('infoId', 'numcin', 'nom', 'prenom', 'address', 'tel', 'infraction')
