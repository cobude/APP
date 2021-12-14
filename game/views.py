from django.http import HttpResponse

# Create your views here.

def index(request):
    line1 = '<h1 style="text-align:center">橘子大作战</h1>'
    line2 = '<img src="http://p7.itc.cn/q_70/images03/20201204/ccbe9c0452db451cb505ae2b27ef10d8.jpeg" width=2000>'
    return HttpResponse(line1+line2)
