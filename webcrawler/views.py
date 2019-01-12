from django.shortcuts import render
from django.http import HttpResponse
import requests
from bs4 import BeautifulSoup




# Create your views here.

def webcrawler_link(request ,template_name='webcrawler/searchengine.html'):
    return render(request, template_name)

def webcrawler_result(request, template_name='webcrawler/result.html'):
    global img_tags
    global link_tags
    user_url = request.POST.get('searcher')

    ##right now i am hardcoding to gale . but in production we can make it dynamic as it takes loads of time

    html_source = requests.get(user_url)
    plain_text = html_source.text
    soup_format = BeautifulSoup(plain_text,'html.parser')
    img_tags = soup_format.find_all('img') ##getting all the images
    print(soup_format.encode("utf-8"))

    ##getting all hyperlinks
    link_tags = [a.get('href') for a in soup_format.find_all('a', href=True)]




    return render(request, template_name, {'user_url':user_url,'plain_text':plain_text,'img_tags':img_tags,'link_tags': link_tags})

def webcrawler_images(request, template_name='webcrawler/images.html'):
    global img_tags

    return render(request,template_name,{'img_tags':img_tags})


def webcrawler_links(request, template_name='webcrawler/links.html'):
    global link_tags

    return render(request,template_name,{'link_tags':link_tags})
