from django.shortcuts import render
import requests
import pygal

# Two example views. Change or delete as necessary.
def home(request):
    print('viewing home')

    context = {
        'example_context_variable': 'Change me.',
    }

    return render(request, 'pages/home.html', context)

def about(request):
    print('viewing about')
    context = {
    }

    return render(request, 'pages/about.html', context)


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
        chart_svg_as_datauri = chart.render_data_uri()
        value = repo_dict["size"]
        label = repo_dict["name"]
        chart.add(label, value)
    
    print(chart_svg_as_datauri)
    
    
        

    context = {
        'github_repos' : repo_list,
        "rendered_chart_svg_as_datauri" : chart_svg_as_datauri,
    }

    return render(request, 'pages/repos_sizes.html', context)


def languages_used(request):
    print('viewing languages used')

    response = requests.get("https://api.github.com/users/jadonhoang/repos")
    repo_list = response.json()
    
    context = {
        
    }

    return render(request, 'pages/languages_used.html', context)

