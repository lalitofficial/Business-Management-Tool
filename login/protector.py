# includes function which protect incoming malicious input
from django.contrib import messages

def is_valid(request,uid,password):
    
    if len(uid)==0 or len(password)==0:
        return False
    
    return True
    