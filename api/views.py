from django.shortcuts import render
import json
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import Contact, ContactSerializer

class ContactsView(APIView):
    def get(self, request, contact_id=None):

        if contact_id is not None:
            contact = Contact.objects.get(id=contact_id)
            serializer = ContactSerializer(contact, many=False)
            return Response(serializer.data)
        else:
            contacts = Contact.objects.all()
            serializer = ContactSerializer(contacts, many=True)
            return Response(serializer.data)
        
    def post(self, request, contact_id=None):
        
        if contact_id is not None:
            contact = Contact.objects.filter(id=contact_id)
            data =request.data
            contact.update(full_name=data['full_name'],email=data['email'],address=data['address'], phone=data['phone'])
            return Response( status=status.HTTP_200_OK)
            #if serializer.is_valid():
            #    contact.update(email=data.email, phone=data.email)
                
            #else:
                #return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
        else:
            
            serializer = ContactSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            else:
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
    
       
    def delete(self, request, contact_id):
        
        contact = Contact.objects.get(id=contact_id)
        contact.delete()
        
        return Response(status=status.HTTP_204_NO_CONTENT)
        
