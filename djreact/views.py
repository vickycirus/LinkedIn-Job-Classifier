from django.http import JsonResponse
import json
from selenium import webdriver
import time
from firebase import firebase
from datetime import datetime

def index(request):
    
    allrelated=[]
    firebas=firebase.FirebaseApplication("https://linkedin-job-searcher-default-rtdb.firebaseio.com/",None)
    #give the path of the chromedriver
    browser=webdriver.Chrome(executable_path='C:/Users/vicky/chromedriver.exe')
    browser.get("https://www.linkedin.com")
    username=browser.find_element_by_id("session_key")
    #give your linkedin username
    username.send_keys('--------')


    password=browser.find_element_by_id("session_password")
    #give your linkedin password
    password.send_keys('-------')

    login_button=browser.find_element_by_class_name("sign-in-form__submit-button")
    login_button.click()

    c=0
    #Scrolling the page 50 times
    while(c<15):
        browser.execute_script("window.scrollTo(0,document.body.scrollHeight)")
        #You can change the sleep time
        time.sleep(1)
        c+=1
    p=0 
    s=""   
    l=[]


    #give your firebase path
    resultdata=firebas.get('/linkedin-job-searcher-default-rtdb/dataSample','')

    for i in resultdata:
        l.append(resultdata[i]['hello'])
    job=browser.find_elements_by_class_name('break-words')


    for i in job:
        k=i.get_attribute('innerText').lower()
        #You can add any number of tags
        jobslist=['#hiring','#hiringalerts','#recruitment','#jobsearch','#jobopportunity']


        posttext=k.split()
        p=0


        for z in range(len(posttext)):
            posttext[z]=posttext[z].lower()  


        for word in jobslist:
            if word in posttext:
                p=1


        if(p==1):
            if k not in l:
                data={'hello':k}
                firebas.post('/linkedin-job-searcher-default-rtdb/dataSample',data)    
                allrelated.append(k)   
    print(allrelated)         
    return JsonResponse({'courses': allrelated})


        




               
       

