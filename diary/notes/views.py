from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import DiaryEntry
from .serializers import DiarySerializer

@api_view(['GET', 'POST'])
def diary_entries(request):
    '''
    List all diary entries or create a new diary entry
    '''
    if request.method == 'GET':
        entries = DiaryEntry.objects.all()
        serializer = DiarySerializer(entries, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = DiarySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])
def diary_entry_detail(request, pk):
    '''
    Retrieve, update or delete a diary entry
    '''
    try:
        entry = DiaryEntry.objects.get(pk=pk)
    except DiaryEntry.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DiarySerializer(entry)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DiarySerializer(entry, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        entry.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# from rest_framework.parsers import JSONParser
# from django.views.decorators.csrf import csrf_exempt
# from django.http import HttpResponse, JsonResponse
# from .serializers import DiarySerializer
# from .models import DiaryEntry

# @csrf_exempt
# def diary_entries(request):
#     '''
#     List all diary entries or create a new diary entry
#     '''
#     if request.method == 'GET':
#         entries = DiaryEntry.objects.all()
#         serializer = DiarySerializer(entries, many=True)
#         return JsonResponse(serializer.data, safe=False)
    
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = DiarySerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=201)
#         return JsonResponse(serializer.errors, status=400)

# @csrf_exempt
# def diary_entry_detail(request, pk):
#     '''
#     Retrieve, update or delete a diary entry
#     '''
#     try:
#         entry = DiaryEntry.objects.get(pk=pk)
#     except DiaryEntry.DoesNotExist:
#         return HttpResponse(status=404)  

#     if request.method == 'PUT':
#         data = JSONParser().parse(request)  
#         serializer = DiarySerializer(entry, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JsonResponse(serializer.data, status=200)
#         return JsonResponse(serializer.errors, status=400)

#     elif request.method == 'DELETE':
#         entry.delete()
#         return HttpResponse(status=204) 