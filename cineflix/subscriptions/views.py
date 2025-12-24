from django.shortcuts import render,redirect

from django.views import View

from .models import SubscriptionPlans

from .forms import SubscriptionForm

# Create your views here.

class SubscriptionsView(View):

    template = 'subscriptions/subscription-list.html'

    def get(self,request,*args,**kwargs):

        plans = SubscriptionPlans.objects.all()

        data = {'plans':plans}

        return render(request,self.template,context=data)
    
class SubscriptionsCreateView(View):

    form_class = SubscriptionForm

    template = 'subscriptions/subscription-create.html'

    def get(self,request,*args,**kwargs):

        form = self.form_class()

        data ={'page': 'Create Subscription' ,
               'form':form}

        return render(request,self.template,context=data)
    
    def post(self,request,*args,**kwargs):

        form = self.form_class(request.POST,request.FILES)

        if form.is_valid():

            form.save()

            return redirect('subscription-list')
        
        print("FORM ERRORS:", form.errors)

        data ={'page': 'Create Subscription' ,
               'form':form}

        return render(request,self.template,context=data)
    
class SubscriptionDeleteView(View):

    def get(self,request,*args,**kwargs):

        uuid = kwargs.get('uuid')

        subscription_plans = SubscriptionPlans.objects.get(uuid=uuid)
        
        #hard delete
        # movie.delete()
        # soft delete
        subscription_plans.active_status=False

        subscription_plans.save()

        return redirect('subscription-list')

