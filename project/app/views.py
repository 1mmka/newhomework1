from django.shortcuts import render
from django.http import HttpResponse,HttpResponseNotFound,HttpResponseRedirect
from django.template.loader import get_template
from django.urls import reverse

# Create your views here.
def login(request): 
    if request.method == 'POST':
        request_data = request.POST
        check_keys = ['username','password']
        
        for key in check_keys:
            if key not in request_data.keys():
                template = get_template('registration.html')
                return HttpResponse(template.render(context=dict(),request=request))
            
        username = request_data['username']
        password = request_data['password']
        flag = False
        
        with open('information.txt','r') as file:
            for line in file:
                line = line.strip()
                temp = line.split(':')
                
                key,value = temp[0],temp[1]
                
                if (key == username) and (value == password):
                    flag = True
                    file.close()
                    break
                else:
                    flag = False
        
        if flag == True:
            return render(request,'hello.html')
        else:
            return render(request,'registration.html')
        
    elif request.method == 'GET':
        return render(request,'login.html')

def registration(request):
    if request.method == 'POST':
        registration_data = request.POST
        data_dict = {
            registration_data['username'] : registration_data['password']
        }
        
        with open('information.txt','a') as file: # использовал метод 'a' для append-a
            for key in data_dict:                 # при использовании 'w' каждый раз перезаписывался
                file.write(f'{key}:{data_dict.setdefault(key,"")}')
                file.write('\n')
            file.close()
    
    url = reverse('login')
    return HttpResponseRedirect(url)