# forms/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import WheelSpecification
from .serializers import WheelSpecificationSerializer

# POST Endpoint: Create WheelSpecification
class WheelSpecificationCreateView(APIView):
     # Get method: Get WheelSpecification
    def get(self, request):
        # Allowed filter keys
        allowed_keys = ['formNumber', 'submittedBy', 'submittedDate']
        filters = {}

        # Check for any invalid keys
        for key in request.query_params.keys():
            if key not in allowed_keys:
                return Response({
                    "success": False,
                    "message": f"Invalid query parameter: '{key}'. Allowed parameters are: {allowed_keys}."
                }, status=status.HTTP_400_BAD_REQUEST)

        # Build filters dict only for valid keys
        for key in allowed_keys:
            value = request.query_params.get(key)
            if value:
                filters[key] = value

        # Apply filters if present; else return all
        queryset = WheelSpecification.objects.filter(**filters) if filters else WheelSpecification.objects.all()

        # If no data found, return meaningful message
        if not queryset.exists():
            return Response({
                "success": True,
                "message": "No wheel specification forms found matching the given criteria.",
                "data": []
            }, status=status.HTTP_200_OK)

        # Serialize the queryset
        serializer = WheelSpecificationSerializer(queryset, many=True)

        # Final Response
        return Response({
            "success": True,
            "message": "Wheel specification forms fetched successfully.",
            # here i am returning complete data but according to your requirement you can send only required data
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    # POST method: Create WheelSpecification
    def post(self, request):
        serializer = WheelSpecificationSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
                
                "data": {
                    "formNumber": serializer.data['formNumber'],
                    "status": serializer.data['status'],
                    "submittedBy": serializer.data['submittedBy'],
                    "submittedDate": serializer.data['submittedDate'],
                    
                },
                "message": "Wheel specification submitted successfully.",
                "success": True,
                
            }, status=status.HTTP_201_CREATED)
        return Response({
            "success": False,
            "message": "Validation failed",
            "errors": serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)
