from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import viewsets
from base.models import User, UserAddress
from .serializers import User_serializer, UserAddress_serializer

@api_view(["GET"])
def get_data(request):
    user = User.objects.all()
    serializer = User_serializer(user, many=True) #many=True is used when we have multiple items to be sent in response. otherwise set to false
    return Response(serializer.data)

@api_view(["GET"])
def get_address_data(request):
    user = UserAddress.objects.all()
    serializer = UserAddress_serializer(user, many=True) #many=True is used when we have multiple items to be sent in response. otherwise set to false
    return Response(serializer.data)

@api_view(["POST"])
def post_data(request):
    serializer = User_serializer(data=request.data)  #send data posted to request to serializer for validation
    if serializer.is_valid(): #validates
        serializer.save() #saves data into DB
    return Response(serializer.data) #returns the data that was posted

@api_view(["POST"])
def post_address_data(request):
    user_serializer = User_serializer(data=request.data)

    if user_serializer.is_valid():
        user = user_serializer.save()

        # Extract address data from request data
        address_data = request.data.pop('user_address', None)
        if address_data:
            address_data['user_id'] = user.user_id  # Assign user_id to the address
            address_serializer = UserAddress_serializer(data=address_data)
            if address_serializer.is_valid():
                address_serializer.save()
            else:
                # Delete the user if address data is invalid
                user.delete()
                return Response(address_serializer.errors, status=400)

        return Response(user_serializer.data, status=201)
    else:
        return Response(user_serializer.errors, status=400)


@api_view(["GET"])
def get_specific_user__address(request, user_id):
    try:
        user = User.objects.get(user_id=user_id)
        address = UserAddress.objects.get(user_id=user_id)
        serialized_address = UserAddress_serializer(address)
        return Response(serialized_address.data)
    except User.DoesNotExist:
        return Response({"error": "User not found"}, status=404)
