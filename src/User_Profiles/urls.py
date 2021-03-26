from django.urls import path
from .views import MyProfile, Received_Friend_Requests, Profile_List, Profile_Detail, Available_Profiles_To_Add, Send_Friend_Request, Remove_Friend, Accept_Friend_Request, Reject_Friend_Request

urlpatterns = [
    path('', Profile_List.as_view(), name='AllProfiles'),

    path('myprofile/', MyProfile, name='MyProfile'),

    path('addfriends/', Available_Profiles_To_Add, name='AddFriends'),
    path('receivedrequests/', Received_Friend_Requests, name='ReceivedRequests'),

    path('sendfriendrequest/', Send_Friend_Request, name='SendFriendRequest'),
    path('removefriend/', Remove_Friend, name='RemoveFriend'),

    path('<slug>/', Profile_Detail.as_view(), name='ProfileDetail'),

    path('acceptfriendrequest/', Accept_Friend_Request, name='AcceptFriendRequest'),
    path('rejectfriendrequest/', Reject_Friend_Request, name='RejectFriendRequest'),
]
