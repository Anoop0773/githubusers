from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.


class api_calls(models.Model):
	username_filter = models.CharField(max_length=500, default='-1')
	min_followers_filter = models.CharField(max_length=500, default='-1')
	min_repos_filter = models.CharField(max_length=500, default='-1')
	language_filter = models.CharField(max_length=500, default='-1')
	location_filter = models.CharField(max_length=500, default='-1')
	inserted_datetime = models.DateTimeField(auto_now_add=True)

	class Meta:
		ordering = ["inserted_datetime"]



class user_data(models.Model):
	api_calls = models.ForeignKey(api_calls, on_delete=models.CASCADE)
	login = models.CharField(max_length=250)
	user_id = models.IntegerField()
	avatar_url = models.CharField(max_length=5000,default='-1')
	user_type = models.CharField(max_length=100,default='-1')
	name = models.CharField(max_length=500, default='-1')
	company = models.CharField(max_length=500, default='-1')
	location = models.CharField(max_length=500, default='-1')
	email = models.CharField(max_length=500, default='-1')
	public_repos = models.IntegerField(default=0)
	public_gists = models.IntegerField(default=0)
	following = models.IntegerField(default=0)
	followers = models.IntegerField(default=0)
	inserted_datetime = models.DateTimeField(auto_now_add=True)
	
	
	class Meta:
		ordering = ["inserted_datetime"]

	def __str__(self):
		return '{0}, {1}'.format(self.login, self.user_id)

	def thumbnail(self):
		if self.avatar_url:
			return mark_safe('<img src="%s" style="width: 45px; height:45px;" />' % (self.avatar_url))
		else:
			return 'No Image Found'
	thumbnail.short_description = 'Thumbnail'
	thumbnail.allow_tags = True



# {
#   "login": "thomaslee",
#   "id": 93216,
#   "node_id": "MDQ6VXNlcjkzMjE2",
#   "avatar_url": "https://avatars2.githubusercontent.com/u/93216?v=4",
#   "gravatar_id": "",
#   "url": "https://api.github.com/users/thomaslee",
#   "html_url": "https://github.com/thomaslee",
#   "followers_url": "https://api.github.com/users/thomaslee/followers",
#   "following_url": "https://api.github.com/users/thomaslee/following{/other_user}",
#   "gists_url": "https://api.github.com/users/thomaslee/gists{/gist_id}",
#   "starred_url": "https://api.github.com/users/thomaslee/starred{/owner}{/repo}",
#   "subscriptions_url": "https://api.github.com/users/thomaslee/subscriptions",
#   "organizations_url": "https://api.github.com/users/thomaslee/orgs",
#   "repos_url": "https://api.github.com/users/thomaslee/repos",
#   "events_url": "https://api.github.com/users/thomaslee/events{/privacy}",
#   "received_events_url": "https://api.github.com/users/thomaslee/received_events",
#   "type": "User",
#   "site_admin": false,
#   "name": "Tom Lee",
#   "company": "@InVisionApp ",
#   "blog": "http://tomlee.co",
#   "location": "Portland, OR, USA",
#   "email": null,
#   "hireable": null,
#   "bio": null,
#   "public_repos": 132,
#   "public_gists": 29,
#   "followers": 68,
#   "following": 42,
#   "created_at": "2009-06-08T15:14:30Z",
#   "updated_at": "2018-07-25T20:54:44Z"
# }