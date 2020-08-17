from django.shortcuts import render
import subprocess
from .models import Sayings
from .forms import IndexForm


def index(request):
    output = ''
    if request.method == "POST":
        form = IndexForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            Sayings.objects.create(
                text=data.get('text')
            )
            text = data.get('text')

            # process = subprocess.Popen(
            #     ["cowsay", text],
            #     # text=True,
            #     stdout=subprocess.PIPE)
            # # output = process.stdout
            # while True:
            #     line = process.stdout.readline().decode().rstrip('\n')
            #     if not line:
            #         break
            #     output.append(line)
            output = subprocess.check_output(
                ["cowsay", text],
                text=True)
            print(output)
    form = IndexForm()
    return render(request, "index.html", {
        "title": "Cowsay App",
        "form": form,
        "output": output})


def history_view(request):
    sayings = Sayings.objects.all()[:10]
    return render(
        request, "history.html", {"title": "Cowsay App", "data": sayings})
