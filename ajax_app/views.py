# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.template import loader


from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    # response = HttpResponse(json.dumps({"ajax": "cross"}))
    # response["Access-Control-Allow-Origin"] = "*"
    # response["Access-Control-Allow-Methods"] = "POST, GET, OPTIONS"
    # response["Access-Control-Max-Age"] = "1000"
    # response["Access-Control-Allow-Headers"] = "*"
    # return response
    template = loader.get_template('ajax_cors.html')
    return HttpResponse(template.render())

    # return HttpResponseRedirect('http://www.baidu.com')
    # return HttpResponseRedirect('http://www.baidu.com')

    # return HttpResponse("Hello, world. You're at the polls index.")