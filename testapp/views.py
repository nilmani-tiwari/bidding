from django.shortcuts import render

# Create your views here.


def test_speech(request):
    if request.method == "POST":
      
        audio=request.FILES["audio"]
        print(1111111111111111111111,audio)
    return render(request,"test/test_speech_record.html")