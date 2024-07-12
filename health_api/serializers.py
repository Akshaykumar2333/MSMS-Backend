from rest_framework import serializers
from .models import SymptomDescription, Precaution, Workout, Description, Medication, Diet

class SymptomDescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = SymptomDescription
        fields = '__all__'

class PrecautionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precaution
        fields = '__all__'

class WorkoutSerializer(serializers.ModelSerializer):
    class Meta:
        model = Workout
        fields = '__all__'

class DescriptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Description
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class DietSerializer(serializers.ModelSerializer):
    class Meta:
        model = Diet
        fields = '__all__'
