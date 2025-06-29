from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

class CheckFollowersView(APIView):
    def post(self, request):
        followers_data = request.FILES.get('followers_file')
        following_data = request.FILES.get('following_file')

        if not followers_data or not following_data:
            return Response({'error': 'Both files are required.'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            followers_json = json.load(followers_data)
            following_json = json.load(following_data)

            # Reuse your logic here:
            followers = [item['value'] for entry in followers_json for item in entry['string_list_data']]
            following = [item['value'] for entry in following_json['relationships_following'] for item in entry['string_list_data']]
            non_followers = [user for user in following if user not in followers]

            results = [
                {
                    "username": user,
                    "profile_url": f"https://www.instagram.com/{user}"
                }
                for user in non_followers
            ]

            return Response({'non_followers': results})

        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
