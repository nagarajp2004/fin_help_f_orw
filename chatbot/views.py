from django.shortcuts import render
from .finacial_agent import get_financial_response
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json  # ✅ Import the missing json module

@api_view(['GET', 'POST'])
def financial_api(request):
    """
    API view to handle GET and POST requests.
    """
    if request.method == 'GET':
        query = request.GET.get('query', '')

        if not query:
            return Response({"error": "Query parameter is required"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            response = get_financial_response(query)
            return Response({'query': query, "response": response}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    elif request.method == 'POST':
     data = json.loads(request.body.decode('utf-8'))
     data = request.data
  
     query = data.get('query', '')
    
     if not query:
        return Response({"error": "Query field is required in POST"}, status=status.HTTP_400_BAD_REQUEST)

     try:
        response = get_financial_response(query)
        return Response({"query": query, "response": response}, status=status.HTTP_200_OK)
     except Exception as e:
        return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
