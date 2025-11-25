from django.shortcuts import render
from django.core.paginator import Paginator

from .models import TeamMember, NewsArticle, Partner

def main(request):
    latest_news = NewsArticle.objects.all().order_by('-published_date')[:3]
    partners = Partner.objects.all()
    return render(request, 'main.html', {'latest_news': latest_news, 'partners': partners, 'page_type': 'main'})

def news_view(request):
    articles = NewsArticle.objects.all().order_by('-published_date')
    paginator = Paginator(articles, 10) 
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'news.html', {'page_obj': page_obj, 'page_type': 'news'})

def team_view(request):
    members = TeamMember.objects.all()
    return render(request, 'team.html', {'members': members, 'page_type': 'team'})

def history_lines_view(request):
    return render(request, 'history_lines.html')

def partner_view(request):
    return render(request, 'partner.html')

def contacts_view(request):
    return render(request, 'contacts.html')

def new_view(request):
    return render(request, 'new.html')