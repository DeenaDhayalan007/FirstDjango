from django.shortcuts import render
from django.utils.translation import activate

from products.models import Product, Purchase
from .models import Csv
from .forms import CsvForm
import csv
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload_file(request):
    error_message=  None
    sucess_message = None
    form = CsvForm(request.POST or None , request.FILES or None)
    if form.is_valid():
        form.save()
        form = CsvForm()
        try:
            obj = Csv.objects.get(activated=False)
            with open(obj.file_name.path, 'r') as f:
                reader = csv.reader(f)

                for row in reader:
                    print(row)
                    user = User.objects.get(id=row[3])
                    prod,_ =Product.objects.get_or_create(name=row[0]) 
                    Purchase.objects.create(
                        product=prod,
                        price=int(row[2]),
                        quantity=int(row[1]),
                        salesman=user,
                        date=row[4],
                    )

            obj.activated = True
            obj.save();
            sucess_message = "Uploaded Sucessfully"
        except:
            error_message = "Upload Somethong went wrong..."
    context = {
        'form':form,
        'sucess_message':sucess_message,
        'error_message':error_message,
    }

    return render(request, 'csvs/upload.html',context)