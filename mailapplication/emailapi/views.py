from django.shortcuts import render
from mailjet_rest import Client
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

import os

# Create your views here.
def index(request):

    if(request.method == "POST"):
        
        # To check all mail are send or not. 
        flag = 1

        #Here we store all emails in our list using ',' seprator.
        emails  = request.POST.get("email","").split(",")
        #extract all info details. 
        info    = request.POST.get("info","")
        #extract all subject details.
        sub     = request.POST.get("subject","")
        
        #we will iterate for each email.
        for email in emails:
            print(email)
            try:

                # Initially we use Sendgrid email API to send mail.
                message = Mail(
                #This is register email for Sendgrid email Service.
                from_email='jeevandeepsingh1105@gmail.com',
                to_emails=email,
                subject=sub,
                html_content=info)

                # Here we make Sendgrid key as private by
                # store it actual value in sendgrid.env 
                # so when we require it's value we have to
                # load the data into SENDGRID_API_KEY by
                # using source ./sendgrid.env
                sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
                response = sg.send(message)
                print(response.status_code)
                #print(response.body)
                #print(response.headers)

            # IF we get any exception then variable 'e' will catch that exception. 
            # So to handle the exception or error we continue to send email using
            # second Email API that is Mailjet.
            except Exception as e:

                # Here we make Mailjet key as private by
                # store it actual value in mailjet.env 
                # so when we require it's value we have to
                # load the data into API_KEY,API_SECRET by
                # using source ./mailjet.env
                api_key = os.environ.get('API_KEY')
                api_secret = os.environ.get('API_SECRET')

                mailjet = Client(auth=(api_key, api_secret), version='v3.1')
                # print("-----------------------------------------------")
                # print(info)
                # print("-----------------------------------------------")
                
                data = {
                'Messages': [
                    {
                    "From": {
                        "Email": "singhjeevandeep1999@gmail.com",
                        "Name": "Jeevan Deep"
                    },
                    "To": [
                        {
                        "Email": email,
                        "Name": "Sample email"
                        }
                    ],
                    "Subject": sub,
                    "TextPart": "My first Mailjet email",
                    "HTMLPart": info,
                    "CustomID": "AppGettingStartedTest"
                    }
                ]
                }

                try:
                    result = mailjet.send.create(data=data)
                    print (result.status_code)
                    print (result.json())
                except Exception as exp:
                    #If our exception/error is not handle by both API then set false.    
                    flag = 0
                    print(exp)  
                    # print("-------------------------")   

        if(flag == 1):
            return render(request,'success.html')
        else:
            return render(request,'error.html')
            
    else:
        #Initially we return this page
        return render(request,'index.html')