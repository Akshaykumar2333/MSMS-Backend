from django.db import models

class SymptomDescription(models.Model):
    disease = models.CharField(max_length=100)
    symptom_1 = models.CharField(max_length=255)
    symptom_2 = models.CharField(max_length=255, blank=True, null=True)
    symptom_3 = models.CharField(max_length=255, blank=True, null=True)
    symptom_4 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.disease

class Precaution(models.Model):
    disease = models.CharField(max_length=100)
    precaution_1 = models.CharField(max_length=255)
    precaution_2 = models.CharField(max_length=255, blank=True, null=True)
    precaution_3 = models.CharField(max_length=255, blank=True, null=True)
    precaution_4 = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.disease

class Workout(models.Model):
    disease = models.CharField(max_length=100)
    workout = models.CharField(max_length=255)

    def __str__(self):
        return self.disease

class Description(models.Model):
    disease = models.CharField(max_length=100)
    description = models.TextField()
    def __str__(self):
        return self.disease

class Medication(models.Model):
    disease = models.CharField(max_length=100)
    medication = models.TextField()

    def __str__(self):
        return self.disease

class Diet(models.Model):
    disease = models.CharField(max_length=100)
    diet = models.TextField()

    def __str__(self):
        return self.disease
