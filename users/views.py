from django.shortcuts import render
import requests
import json
from .models import *
# Create your views here.




def index(request):
    search_result = {}
    if 'username' in request.GET:
        username = request.GET['username']
        min_followes = request.GET['min_followes']
        min_repos = request.GET['min_repos']
        language = request.GET['language']
        location = request.GET['location']
        # url = 'https://api.github.com/users/%s' % username
        
        url = ''
        if username:
        	url = 'https://api.github.com/search/users?q='+username
        
        if min_followes:
        	url = url + '+followers:=' + min_followes
        
        if min_repos:
        	url = url + '+repos:=' + min_followes
 
        if language:
        	url = url + '+language:' + language

        if location:
        	url = url + '+location:' + location  

             	
         
        response = requests.get(url)
        search_was_successful = (response.status_code == 200)  # 200 = SUCCESS


        search_result = response.json()

        if search_was_successful:
            all_user_json = []
            all_lists = search_result['items']
            
            for item_url in all_lists:
                
                response_json = requests.get(item_url['url'])
                all_user_json.append(response_json.json())



            print('all_user_json',len(all_user_json))
            all_user_data = {}
            all_api_data = {}
            
            all_api_data['username_filter'] = username
            all_api_data['min_followers_filter'] = min_followes
            all_api_data['min_repos_filter'] = min_repos
            all_api_data['language_filter'] = language
            all_api_data['location_filter'] = location

            api_data = api_calls.objects.create(**all_api_data)
            api_data.save()
            api_data_id = api_data.pk

            for user_json in all_user_json:


                all_user_data['api_calls'] = api_data

                if user_json['login']:
                    all_user_data['login'] = user_json['login']

                if user_json['id']:
                    all_user_data['user_id'] = user_json['id']

                if user_json['avatar_url']:
                    all_user_data['avatar_url'] = user_json['avatar_url']

                if user_json['type']:
                    all_user_data['user_type'] = user_json['type']

                if user_json['name']:
                    all_user_data['name'] = user_json['name']

                if user_json['company']:
                    all_user_data['company'] = user_json['company']

                if user_json['location']:
                    all_user_data['location'] = user_json['location']

                if user_json['email']:
                    all_user_data['email'] = user_json['email']

                if user_json['public_repos']:
                    all_user_data['public_repos'] = user_json['public_repos']

                if user_json['public_gists']:
                    all_user_data['public_gists'] = user_json['public_gists']

                if user_json['following']:
                    all_user_data['following'] = user_json['following']

                if user_json['followers']:
                    all_user_data['followers'] = user_json['followers']

                exist_count = user_data.objects.filter(user_id=user_json['id']).count()
                if exist_count > 0:
                    user_data.objects.filter(user_id=user_json['id']).update(**all_user_data)
                else:
                    obj = user_data.objects.create(**all_user_data)
                    obj.save()



            search_result['size'] = len(all_lists)
            search_result['success'] = search_was_successful
            search_result['rate'] = {
                'limit': response.headers['X-RateLimit-Limit'],
                'remaining': response.headers['X-RateLimit-Remaining'],
            }
        else:
            search_result['message'] = 'Sorry!!,this query is not finding any users'

    return render(request, 'users/index.html', {'search_result': search_result})