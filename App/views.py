from django.shortcuts import render
from django.views import View
import json
# Create your views here.

class IndexView(View):

    def get(self,request,*args, **kwargs):

        with open('post_data.json', 'r') as f:
            data = json.load(f)
            print(data)
        context={}
        return render(request,'app/index.html',context)
