from sgcommapp.models import *
from django.views.generic import View
from django.http import HttpResponseRedirect
from .services import SuperblyServices

class LogoutView(View):

    def get(self, request):
        response = SuperblyServices.Test_User_Login(request)
        if not response:
            return  HttpResponseRedirect("/")
        #remove user logged status
        Account.objects.filter(username=request.session['username']).update(logged = False)
        
        del request.session['user_id']
        del request.session['username']

        request.session.modified = True
        return HttpResponseRedirect('/')

    def post(self, request):
        pass
