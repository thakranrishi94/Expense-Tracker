from django.shortcuts import render
from .models import Transaction
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import TransactionSerializer
from rest_framework.views import APIView
from django.db.models import Sum


@api_view(['GET'])
def get_transaction(request):
    queryset=Transaction.objects.all()
    serializer=TransactionSerializer(queryset,many=True)
    return Response({
            'data' : serializer.data,
             'Total':queryset.aggregate(total=Sum('amount'))['total'] or 0
              })


class Transactions(APIView):
    def get(self,request):
        queryset=Transaction.objects.all()
        serializer=TransactionSerializer(queryset,many=True)
        return Response({
            'data' : serializer.data,
             'Total':queryset.aggregate(total=Sum('amount'))['total'] or 0
              })
    def post(self,request):
        data=request.data
        serializer=TransactionSerializer(data=data)
        if not serializer.is_valid():
            return Response({
                "Message":"Error Occured",
                "Errors: ":serializer.error_messages
            })
        serializer.save()
        return Response({
            'Message':"Data saved successfully",
            'Data':serializer.data
        })
    
    def put(self,request):
        data=request.data
        if not data.get('id'):
            return Response({"Message":"Id is required"})
        transaction=Transaction.objects.get(id=data.get('id'))
        serializer=TransactionSerializer(transaction,data=data,partial=False)
        if not serializer.is_valid():
            return Response({
                "Message":"Error Occured",
                "Errors: ":serializer.error_messages
            })
        serializer.save()
        return Response({
            "Message":"Saved Successfully",
            "Data":serializer.data
        })
        
    def patch(self,request):
        data=request.data
        if not data.get('id'):
            return Response({"Message":"Id is required"})
        transaction=Transaction.objects.get(id=data.get('id'))
        serializer=TransactionSerializer(transaction,data=data,partial=True)
        if not serializer.is_valid():
            return Response({
                "Message":"Error Occured",
                "Errors: ":serializer.error_messages
            })
        serializer.save()
        return Response({
            "Message":"Saved Successfully",
            "Data":serializer.data
        })
    def delete(self,request):
       data=request.data
       if not data.get('id'):
           return Response({"Message":"Id is required"})
       transaction=Transaction.objects.get(id=data.get('id')).delete()
       return Response({
           "Message":"Data deleted successfully",
           "Data":{}
       })
