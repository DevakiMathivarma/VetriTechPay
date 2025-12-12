from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from django.shortcuts import redirect
from django.urls import reverse
    
class CustomSocialAdapter(DefaultSocialAccountAdapter):

    def get_login_redirect_url(self, request):
        user = request.user

        # If user has NOT completed KYC
        if not hasattr(user, "testkyc"):     # update based on your model
            return "/test_view/"

        # If KYC completed
        return "/vpay_dashboard/"
