from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse


def merge_unique_numbers(request):
    data = request.Post.getlist("numbers[]", [])
    merge_numbers = sorted(set(map(int,data)))
    return JsonResponse({"merge_numbers": merge_numbers})