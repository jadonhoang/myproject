from django.shortcuts import render
from django.contrib import admin
from .models import DashboardPanel
import requests
import pygal
import json


def home(request):
    print('viewing home')

    context = {
    }

    return render(request, 'pages/home.html', context)


def allrepos(request):
    print('viewing repos')

    response = requests.get("https://api.github.com/users/jadonhoang/repos")
    repo_list = response.json()
    context = {
        'github_repos' : repo_list,
    }

    return render(request, 'pages/all_repos.html', context)


def repos_size(request):
    print('viewing repos size')

    response = requests.get("https://api.github.com/users/jadonhoang/repos")
    repo_list = response.json()

    chart = pygal.Gauge()
    chart.range = [0, 20]
    

    for repo_dict in repo_list:
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)
     
    chart_svg_as_datauri = chart.render_data_uri()
    
    context = {
        'github_repos' : repo_list,
        "rendered_chart_svg_as_datauri" : chart_svg_as_datauri,
    }

    return render(request, 'pages/repos_sizes.html', context)


def view_panels(request):
    print('viewing panels')
    dboard_panels = DashboardPanel.objects.all()
    
    context = {
        "all_panels" : dboard_panels,
    }

    return render(request, "pages/home_panels.html", context)


def panel_details(request, panel_id):
    panel = DashboardPanel.objects.get(id=panel_id)

    repo_name = panel.repo_name

    response = requests.get("https://api.github.com/repos/jadonhoang/" + repo_name + "/languages")
    languages = response.json()

    if(panel.panel_type == "piechart"):
        chart = pygal.Pie()
    elif(panel.panel_type == "barchart"):
        chart = pygal.Bar()

    for language in languages:
        value = languages[language]
        label = language
        chart.add(label, value)

    chart_svg = chart.render_data_uri()

    context = {
        "panels" : panel,
        "rendered_chart_svg" : chart_svg,
        "repo_name" : repo_name,
    }

    return render(request, "pages/panel_details.html", context)








