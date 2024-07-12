# health_api/management/commands/load_csv_data.py

import csv
import os
from django.core.management.base import BaseCommand
from django.conf import settings
from health_api.models import SymptomDescription, Precaution, Workout, Description, Medication, Diet

class Command(BaseCommand):
    help = 'Load CSV data into models'

    def handle(self, *args, **kwargs):
        self.load_symptom_descriptions()
        self.load_precautions()
        self.load_workouts()
        self.load_descriptions()
        self.load_medications()
        self.load_diets()

    def load_symptom_descriptions(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/symtoms_df.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                SymptomDescription.objects.create(
                    disease=row['Disease'],
                    symptom_1=row['Symptom_1'],
                    symptom_2=row.get('Symptom_2'),
                    symptom_3=row.get('Symptom_3'),
                    symptom_4=row.get('Symptom_4')
                )
        print("Loaded Symptom Descriptions")

    def load_precautions(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/precautions_df.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Precaution.objects.create(
                    disease=row['Disease'],
                    precaution_1=row['Precaution_1'],
                    precaution_2=row.get('Precaution_2'),
                    precaution_3=row.get('Precaution_3'),
                    precaution_4=row.get('Precaution_4')
                )
        print("Loaded Precautions")

    def load_workouts(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/workout_df.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Workout.objects.create(
                    disease=row['disease'],
                    workout=row['workout']
                )
        print("Loaded Workouts")

    def load_descriptions(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/description.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Description.objects.create(
                    disease=row['Disease'],
                    description=row['Description']
                )
        print("Loaded Descriptions")

    def load_medications(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/medications.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Medication.objects.create(
                    disease=row['Disease'],
                    medication=row['Medication']
                )
        print("Loaded Medications")

    def load_diets(self):
        file_path = os.path.join(settings.BASE_DIR, 'health_api/data/diets.csv')
        with open(file_path, newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                Diet.objects.create(
                    disease=row['Disease'],
                    diet=row['Diet']
                )
        print("Loaded Diets")
