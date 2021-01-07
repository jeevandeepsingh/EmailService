# EmailServiceDjangoAssignment-EmailService Documentation

EMail API Used in Project :

  1. SendGrid
  2. Mailjet

Step 1 - ​ Setting the Environment variable

    ● Change your working directory to DjangoProject
   ![](screenshot/image1.png)
   
    ● Activate virtual environment (‘venv’)
      1. Type the following command to activate it.
      2. $source venv/bin/activate
   ![](screenshot/image2png)
      
      3. (venv) right before the root user indicate that the virtual environment is activated

Step 2 - ​ Setting the environment variable of Sendgrid, Mailjet

    ● Change the directory to “mailapplication/emailapi/”
   ![](screenshot/image3.png)
   
    ● Type the below command to set the environment variable
      $ source ./sendgrid.env
      $ source ./mailjet.env
   ![](screenshot/image4.png)

Step 3 - ​ Run the Django Server

    ● Change the directory to mailapplication “cd ..”
   ![](screenshot/image5.png)
    
    ● Type the below command to run server
      $ python manage.py runserver
  ![](screenshot/image6.png)
    
    ● Go to Browser run URL “​http://127.0.0.1:8000/​”
![](screenshot/image7.png)

Step 4 - ​ User Input Format

    ● If there is only one email then
  ![](screenshot/image8.png)
   
   
    ● If there are multiple emails then separate them by “,”(Comma)
  ![](screenshot/image9.png)
   
    ● Enter all the Details “All details are required” & Submit.
  ![](screenshot/image10.png)
    
    ● If the email successfully sends then you get this message.
  ![](screenshot/image11.png)
    
    ● If an error occurred during the process then you get this message
  ![](screenshot/image12.png)
