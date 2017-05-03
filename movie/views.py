from django.shortcuts import render
import os,django
from TwitterAPI import TwitterAPI,TwitterRequestError,TwitterConnectionError
import json
from movie.models import table,age_gender
from django.db.models import Count,Avg
from django.http import HttpResponse
import requests
import numpy

raw_data = open('/Users/apple/Desktop/6889/project/web/movie/static/userrate.txt', 'rb')
X = numpy.loadtxt(raw_data, delimiter=",")
raw_data = open('/Users/apple/Desktop/6889/project/web/movie/static/prediction.txt', 'rb')
pred = numpy.loadtxt(raw_data, delimiter=",")
raw_data = open('/Users/apple/Desktop/6889/project/web/movie/static/movies.csv', 'r')
movies = numpy.loadtxt(raw_data, dtype=str, delimiter="\n")
Users = X[:,0]
userdict = {}
number = 0
for i in range(len(Users)):
    if Users[i] in userdict:
        print 'ok'
    else:
        userdict[Users[i]]=number
        number += 1


def stream(request):
    url="http://text-processing.com/api/sentiment/"
    url1="http://api.ai-applied.nl/api/demographics_api/?request="
    consumer_key = 'NIQpSybvhSANztWysLINzu4qn'
    consumer_secret = '8udQR80ylsGUaTsj3l2YF9vvfKxFxNZO1SA78HuVgWjV01TVO3'
    access_token_key = '839610378145378304-LV4rTa0hiS6UEEm9fvUtRXV5f0vYX2Q'
    access_token_secret = 'FMFTc4IQnVVqwb56Q3oC3ybwXYCCuhuQlMg9w4AykXUca'
    api = TwitterAPI(consumer_key, consumer_secret, access_token_key, access_token_secret)
    api_key="42ad8ee03a9baf60fd8e8cc9c28912634a2360f663e2e644bb1103e3c2b16e61"

    while True:
        
        try:
            iterator = api.request('statuses/filter', {'track':keyword,'lang':'en'}).get_iterator()
            for item in iterator:
                if item['coordinates']<>None:
                    print item
                    fo=open('/Users/apple/Desktop/6889/project/web/movie/static/where.js','r+')
                    fo.seek(-2,2)
                    fo.write('\t'+str(item['coordinates']['coordinates'])+',\n];')
                    fo.flush()
                    fo.close()
                if 'text' in item and 'user'  in item:
                    try:
                        r={
                            "data":{
                                "api_key":api_key,
                                "call":{
                                    "return_original":True,
                                    "data":[
                                        {
                                            "text":str(item['text']),
                                            "language_iso":"eng",
                                            "user":str(item['user']['name']),
             
                                        }
                                            ]
                                        }
                                    }
                            }
                        r=json.dumps(r)
                        response = requests.request("GET", url1+r)
                        age_gender.objects.create(
                            age = str(json.loads(response.content.decode("utf-8"))["response"]["data"][0]["age"]),
                            gender = str(json.loads(response.content.decode("utf-8"))["response"]["data"][0]["gender"]),
                            )

                        table.objects.create(
                            name = item['user']['id'], 
                            content = item['text'], 
                            result = json.loads((requests.post(url, data='text='+str(item['text'])).content).encode('utf-8'))["label"],
                            neg = json.loads((requests.post(url, data='text='+str(item['text'])).content).encode('utf-8'))["probability"]['neg'],
                            neu = json.loads((requests.post(url, data='text='+str(item['text'])).content).encode('utf-8'))["probability"]['neutral'],
                            pos = json.loads((requests.post(url, data='text='+str(item['text'])).content).encode('utf-8'))["probability"]['pos'],
                            )
                            
                    except:
                        continue
                elif 'disconnect' in item:
                    event = item['disconnect']
                    if event['code'] in [2,5,6,7]:
                    # something needs to be fixed before re-connecting
                        raise Exception(event['reason'])
                    else:
                    # temporary interruption, re-try request
                        break
        except TwitterRequestError as e:
            if e.status_code < 500:
            # something needs to be fixed before re-connecting
                pass
            else:
            # temporary interruption, re-try request
                pass
        except TwitterConnectionError:
        # temporary interruption, re-try request
            pass

def where(request):
    
    return render(request, 'where.html')

def index0(request):
    
    return render(request, 'main.html')

def hidden_figures(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Hidden Figures'
    return render(request, 'hidden_figures.html')

def get_out(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Get Out movie'
    return render(request, 'get_out.html')

def sleepless(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Sleepless movie'
    return render(request, 'sleepless.html')

def patriots_day(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Patriots Day'
    return render(request, 'patriots_day.html')

def alien_covenant(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Alien: Covenant'
    return render(request, 'alien_covenant.html')

def aftermath(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Aftermath movie'
    return render(request, 'aftermath.html')

def going_in_style(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Going in Style'
    return render(request, 'going_in_style.html')

def a_monster_calls(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='A Monster Calls'
    return render(request, 'a_monster_calls.html')

def the_bye_bye_man(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='The Bye Bye Man'
    return render(request, 'the_bye_bye_man.html')

def unforgettable(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Unforgettable movie'
    return render(request, 'unforgettable.html')

def a_cure_for_wellness(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='A Cure for Wellness'
    return render(request, 'a_cure_for_wellness.html')

def the_circle(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='The Circle'
    return render(request, 'the_circle.html')

def the_promise(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='The Promise'
    return render(request, 'the_promise.html')

def the_lost_city_of_z(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='The Lost City of Z'
    return render(request, 'the_lost_city_of_z.html')

def colossal(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Colossal movie'
    return render(request, 'colossal.html')

def below_her_mouth(request):
    table.objects.all().delete()
    age_gender.objects.all().delete()
    global keyword
    keyword='Below Her Mouth'
    return render(request, 'below_her_mouth.html')

def recommendation(request):
    return render(request, 'recommendation.html')

def post(request):
    if request.method == "POST":
        userid  = int(request.POST.get('name'))
        ans = []
        try:

            usernum = userdict[userid]
            allratings = pred[usernum][0:16]
            ratings = reversed(sorted(range(len(allratings)), key=lambda i: allratings[i]))
            for i in ratings:
                index = int(i)
                movie = movies[index]
                ans.append(movie)
            return HttpResponse(json.dumps(ans))
        except:
            ans=[0,0,0,0,0]
            return HttpResponse(json.dumps(ans))


def add(request):
    ret0=float(str(table.objects.all().aggregate(Avg('pos'))['pos__avg']))*10.0+float(str(table.objects.all().aggregate(Avg('neu'))['neu__avg']))*4.0
    ret1=table.objects.filter(result='pos').aggregate(Count('id'))['id__count']
    ret2=table.objects.filter(result='neutral').aggregate(Count('id'))['id__count']
    ret3=table.objects.filter(result='neg').aggregate(Count('id'))['id__count']
    ret4=table.objects.all().aggregate(Count('id'))['id__count']
    ret5=table.objects.all().aggregate(Avg('pos'))['pos__avg']
    ret6=table.objects.all().aggregate(Avg('neu'))['neu__avg']
    ret7=table.objects.all().aggregate(Avg('neg'))['neg__avg']

    return HttpResponse('Rating: '+str(ret0)+"\n"+'positive: '+str(ret1)+'\n'+'neutral: '+str(ret2)+'\n'+'negative: '+str(ret3)+'\n'+'sum: '+str(ret4)+'\n'+'Avg.positive posibility: '+str(ret5)+'\n'+'Avg.neutral posibility: '+str(ret6)+'\n'+'Avg.negative posibility: '+str(ret7))

def addlist(request):
    ret1=age_gender.objects.filter(age='12-20').aggregate(Count('id'))['id__count']
    ret2=age_gender.objects.filter(age='21-30').aggregate(Count('id'))['id__count']+age_gender.objects.filter(age='unknown').aggregate(Count('id'))['id__count']
    ret3=age_gender.objects.filter(age='31-40').aggregate(Count('id'))['id__count']
    ret4=age_gender.objects.filter(age='41-55').aggregate(Count('id'))['id__count']
    ret5=age_gender.objects.filter(age='56-65').aggregate(Count('id'))['id__count']
    ret6=age_gender.objects.filter(gender='male').aggregate(Count('id'))['id__count']+age_gender.objects.filter(gender='unknown').aggregate(Count('id'))['id__count']
    ret7=age_gender.objects.filter(gender='female').aggregate(Count('id'))['id__count']
    return HttpResponse('12-20: '+str(ret1)+"\n"+'21-30: '+str(ret2)+'\n'+'31-40: '+str(ret3)+'\n'+'41-55: '+str(ret4)+'\n'+'56-65: '+str(ret5)+'\n'+'Male: '+str(ret6)+'\n'+'Female: '+str(ret7)+'\n')
    