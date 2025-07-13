# forms/serializers.py
from rest_framework import serializers
from .models import WheelSpecification, WheelSpecificationFields

# Nested fields serializer
class WheelSpecificationFieldsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WheelSpecificationFields
        exclude = ['spec']

# Main serializer with nested `fields`
class WheelSpecificationSerializer(serializers.ModelSerializer):
    fields = WheelSpecificationFieldsSerializer()

    class Meta:
        model = WheelSpecification
        fields = ['formNumber', 'submittedBy', 'submittedDate', 'fields', 'status']

    def create(self, validated_data):
        fields_data = validated_data.pop('fields')  # extract nested
        spec = WheelSpecification.objects.create(**validated_data)  # main object
        WheelSpecificationFields.objects.create(spec=spec, **fields_data)  # nested fields
        return spec
