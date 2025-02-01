from django.shortcuts import render, redirect
from .models import Transaction
from django.db.models import Sum

def transaction_list(request):
    transactions = Transaction.objects.all()
    total_income = Transaction.objects.filter(category='income').aggregate(Sum('amount')).get('amount__sum', 0)
    total_expense = Transaction.objects.filter(category='expense').aggregate(Sum('amount')).get('amount__sum', 0)
    if total_income is None or total_expense is None:
        savings = 0  # or any default value you prefer
    else:
        savings = total_income - total_expense

    
    return render(request, 'finance/transaction_list.html', {
        'transactions' : transactions,
        'total_income' : total_income,
        "total_expense": total_expense,
        'savings' : savings,
    })

def add_transaction(request):
    if request.method == 'POST':
        title = request.POST['title']
        amount = request.POST['amount']
        category = request.POST['category']
        date = request.POST['date']
        # Corrected the method syntax
        Transaction.objects.create(title=title, amount=amount, category=category, date=date)
        return redirect('transaction_list')
    return render(request, 'finance/add_transaction.html')


def delete_transaction(request, transaction_id):
    transaction = Transaction.objects.get(id=transaction_id)
    transaction.delete()
    return redirect('transaction_list')
    


# Create your views here.
