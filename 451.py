#oops in python
#polymorphism
#create notification system(email/sms).
class Email:
    def send(self):
        print(f"email notification has sent.")
class SMS:
    def send(self):
        print(f"sms notification has sent.") 
def notification_send(message):
    message.send() 

e1=Email()
s1=SMS()
notification_send(e1)
notification_send(s1) 
     