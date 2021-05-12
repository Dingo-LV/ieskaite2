from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, View, FormView
from deposit.models import Deposit
from deposit.form import DepositForm
from decimal import Decimal


class Add_deposit(View):

    def get(self, request):
        return render(
            template_name='add_deposit.html',
            request = request
        )

    def post(self,request):
        deposit = request.POST['deposit']
        term = request.POST['term']
        rate = request.POST['rate']

        rate = rate/100
        interest = deposit

        for i in range(term):
            interest += (interest * rate)
            i += 1

        interest = Decimal(interest)
        interest = round(interest, 2)
        interest -= deposit
        deposite = Deposit(
            deposit=deposit,
            term=term,
            rate=rate,
            interest=interest
        )


        deposite.save()
        context = Deposite
        return render(
            template_name='deposit_list',
            request = request,
            context=context,
        )

class DepositListView(ListView):

    model = Deposit
    template_name = 'deposit_list.html'
