from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
from .models import Send


def image_upload(request):
    if request.method == "POST":
        email = request.POST["email"]
        review = request.POST["review"]
        try:
            image_file = request.FILES["image_file"]
            Send.objects.create(email = email, review = review, file=image_file)
            #fs = FileSystemStorage()
            #filename = fs.save(image_file.name, image_file)
            #image_url = fs.url(filename)
            #print(request.FILES["image_file"])
        except:
            Send.objects.create(email = email, review = review)
        data = {
            'send' : True,
        }

        return render(request, "reviews/create_review.html", context=data)
    data = {
        'send' : False,
    }
    
    return render(request, "reviews/create_review.html", context=data)
