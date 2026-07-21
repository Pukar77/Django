from django.http import HttpResponse

def post_detail(request, post_id):
    return HttpResponse(f"Showing detail of the post {post_id}")

def user_profile(request, username):
    return HttpResponse(f"Showing the detail of the user {username}")

