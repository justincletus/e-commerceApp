from paypalcheckoutsdk.core import PayPalHttpClient, SandboxEnvironment
from django.conf import settings
import razorpay

def getClient(request):

    paypal_client_id = settings.PAYPAL_CLIENT_ID
    paypal_secret_id = settings.PAYPAL_SECRET_ID

    env = SandboxEnvironment(client_id=paypal_client_id, client_secret=paypal_secret_id)
    client = PayPalHttpClient(env)
    return client

def getRazorClient(request):
    razor_client_id = settings.RAZOR_CLIENT_ID
    razor_secret_id = settings.RAZOR_SECRET_ID
    
    client = razorpay.Client(auth=(str(razor_client_id), str(razor_secret_id)))
    client.set_app_details({
        "title": "Megachips",
        "version": "v1"
    })
    
    return client



