# from django.shortcuts import render
# from django.views.generic import ListView, DetailView

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import ExpensesSerializer
# Create your views here.

class ExpensesList(APIView):
    """
    List all expenses, or create a new expenses.
    """
    def get(self, request, format=None):
        expenses = Expenses.objects.all()
        serializer = ExpensesSerializer(expenses, many=True)
        return Response(serializer.data)