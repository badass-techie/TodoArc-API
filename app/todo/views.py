from django.shortcuts import render
from django.http.response import Http404
from django.shortcuts import render
from rest_framework.views import APIView
from .models import Todo
from .serializers import TodoSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
class TasksView(APIView):
    # get a single Todo
    def get_object(self, pk):
        try:
            return Todo.objects.get(pk=pk)
        except Todo.DoesNotExist:
            raise Http404

    # READ
    def get(self, request, pk=None):
        if pk:
            data = [self.get_object(pk)]  # READ a single Todo given the primary key
        else:
            data = Todo.objects.all()   # READ all Todos

        serializer = TodoSerializer(data, many=True)    # Serialize the data

        return Response(serializer.data)    # Return the serialized data

    # CREATE
    def post(self, request):
        data = request.data             # Get payload
        serializer = TodoSerializer(data=data)  # Serialize the data

        serializer.is_valid(raise_exception=True)   # Validate the data

        serializer.save()   # write to the database

        response = Response()

        response.data = {
            'message': 'Todo Created Successfully',
            'data': serializer.data
        }

        return response

    # UPDATE
    def put(self, request, pk):
        todo_to_update = Todo.objects.get(pk=pk)    # Get the Todo to update

        # Pass the instance to update to the serializer, and the data and also partial to the serializer
        # Passing partial will allow us to update without passing the entire Todo object
        serializer = TodoSerializer(instance=todo_to_update, data=request.data, partial=True)    

        serializer.is_valid(raise_exception=True)   # Validate the data

        serializer.save()   # write to the database

        response = Response()

        response.data = {
            'message': 'Todo Updated Successfully',
            'data': serializer.data
        }

        return response

    # DELETE
    def delete(self, request, pk):
        todo_to_delete =  Todo.objects.get(pk=pk)   # Get the Todo to delete

        todo_to_delete.delete()

        return Response({
            'message': 'Todo Deleted Successfully'
        })


class CompletedTasksView(APIView):
    def get(self, request):
        data = Todo.objects.filter(isCompleted=True)   # READ all completed Todos

        serializer = TodoSerializer(data, many=True)    # Serialize the data

        return Response(serializer.data)    # Return the serialized data
