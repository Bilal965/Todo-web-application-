
from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from todo.serializers import CrudSerializer,UpdateTodoSerializer,ViewTodoSerializer
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from todo.models import Todo

from rest_framework import status
class CreateTodo(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def post(self,request,format=None):
        data=request.data
        print(data)
        serializer=CrudSerializer(data=data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"message":"Todo Created Successfully"},status=status.HTTP_201_CREATED)


class RudTodo(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def put(self,request,myid,format=None):
        todo=Todo.objects.get(id=myid)
        serializer=UpdateTodoSerializer(todo,data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({"Message":"Updated Todo Successfully"},status=status.HTTP_202_ACCEPTED)

    def get(self,request,myid,format=None):
        todo=Todo.objects.get(id=myid)
        serializer=ViewTodoSerializer(todo)
        return Response(serializer.data)

    def delete(self,request,myid,format=None):
        todo=Todo.objects.get(id=myid)
        todo.delete()
        return Response({"Message":"Deleted Successfully"},status=status.HTTP_202_ACCEPTED)

class Alltodo(APIView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [IsAuthenticated]
    def get(self,request,format=None):
        alltodo=Todo.objects.all()
        serializer=ViewTodoSerializer(alltodo,many=True)
        return Response(serializer.data,status=status.HTTP_200_OK)

    




