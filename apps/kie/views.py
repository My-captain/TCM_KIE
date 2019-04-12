from django.shortcuts import render
from django.views.generic.base import View

from django.http import JsonResponse

from .extract_core import hmm_extract, nlpir_extract

# Create your views here.


class KIEView(View):
    def get(self, request):
        return render(request, "kie.html")

    def post(self, request):
        text_for_extract = request.POST["text_for_extract"]
        extract_algorithm = request.POST["extract_algorithm"]
        data = []
        if extract_algorithm == "HMM":
            data = hmm_extract(text_for_extract)
        elif extract_algorithm == "pynlpir":
            data = nlpir_extract(text_for_extract)
        return JsonResponse(data, safe=False)
