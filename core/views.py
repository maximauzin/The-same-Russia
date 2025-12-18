from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import logout
from django.db import transaction, models
from .models import News, TeamMember, Partner, HistoryLine, NewsImage
from .forms import NewsForm, TeamMemberForm, PartnerForm, HistoryLineForm

def logout_view(request):
    logout(request)
    return redirect(request.META.get('HTTP_REFERER', 'home'))

def is_admin(user):
    return user.is_authenticated and user.is_staff

# --- НОВОСТИ ---
def news_list(request):
    news = News.objects.all().order_by('-created_at')
    template_name = 'manage/news_list.html' if is_admin(request.user) else 'core/news.html'
    return render(request, template_name, {'news_list': news})

@user_passes_test(is_admin)
def news_add(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            with transaction.atomic():
                news_item = form.save(commit=False)
                # Обложка берется напрямую из формы
                if 'image' in request.FILES:
                    news_item.image = request.FILES['image']
                news_item.save()
                
                # Добавляем фото в галерею (все файлы из 'photos')
                files = request.FILES.getlist('photos')
                for i, f in enumerate(files):
                    NewsImage.objects.create(news=news_item, image=f, order=i) 
            
            return redirect('news')
    else:
        form = NewsForm()
    return render(request, 'manage/news_form.html', {'form': form})

@user_passes_test(is_admin)
def news_edit(request, pk):
    news = get_object_or_404(News, pk=pk)
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES, instance=news)
        if form.is_valid():
            with transaction.atomic():
                news_item = form.save()
                
                # 1. Удаление фото
                delete_ids = request.POST.getlist('delete_images[]')
                NewsImage.objects.filter(id__in=delete_ids).delete()
                
                # 2. Обновление порядка существующих фото
                ordered_existing_ids = [int(x) for x in request.POST.getlist('existing_order[]') if x.isdigit()]
                for i, img_id in enumerate(ordered_existing_ids):
                    NewsImage.objects.filter(id=img_id, news=news_item).update(order=i)

                # 3. Добавление новых фото
                new_files_order_temp_ids = request.POST.getlist('new_files_order[]')
                new_files_map = {f.name: f for f in request.FILES.getlist('photos')}
                
                max_order = NewsImage.objects.filter(news=news_item).aggregate(models.Max('order'))['order__max'] or -1

                for temp_id in new_files_order_temp_ids:
                    original_filename = '_'.join(temp_id.split('_')[2:])
                    if original_filename in new_files_map:
                        NewsImage.objects.create(
                            news=news_item, 
                            image=new_files_map[original_filename], 
                            order=max_order + 1
                        )
                        max_order += 1

            return redirect('news')
    else:
        form = NewsForm(instance=news)
    return render(request, 'manage/news_form.html', {'form': form})

@user_passes_test(is_admin)
def news_delete(request, pk):
    get_object_or_404(News, pk=pk).delete()
    return redirect('news')

# --- КОМАНДА --- (без изменений)
def team_list(request):
    members = TeamMember.objects.all()
    template_name = 'manage/team_list.html' if is_admin(request.user) else 'core/team.html'
    return render(request, template_name, {'members': members})

@user_passes_test(is_admin)
def team_add(request):
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('team')
    else:
        form = TeamMemberForm()
    return render(request, 'manage/team_form.html', {'form': form, 'title': 'Новый участник'})

@user_passes_test(is_admin)
def team_edit(request, pk):
    member = get_object_or_404(TeamMember, pk=pk)
    if request.method == 'POST':
        form = TeamMemberForm(request.POST, request.FILES, instance=member)
        if form.is_valid():
            form.save()
            return redirect('team')
    else:
        form = TeamMemberForm(instance=member)
    return render(request, 'manage/team_form.html', {'form': form, 'title': 'Редактирование'})

@user_passes_test(is_admin)
def team_delete(request, pk):
    get_object_or_404(TeamMember, pk=pk).delete()
    return redirect('team')

# --- ИСТОРИЯ --- (без изменений)
def history_list(request):
    lines = HistoryLine.objects.all()
    template_name = 'manage/history_list.html' if is_admin(request.user) else 'core/history.html'
    return render(request, template_name, {'lines': lines})

@user_passes_test(is_admin)
def history_add(request):
    if request.method == 'POST':
        form = HistoryLineForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = HistoryLineForm()
    return render(request, 'manage/history_form.html', {'form': form})

@user_passes_test(is_admin)
def history_edit(request, pk):
    line = get_object_or_404(HistoryLine, pk=pk)
    if request.method == 'POST':
        form = HistoryLineForm(request.POST, request.FILES, instance=line)
        if form.is_valid():
            form.save()
            return redirect('history')
    else:
        form = HistoryLineForm(instance=line)
    return render(request, 'manage/history_form.html', {'form': form})

@user_passes_test(is_admin)
def history_delete(request, pk):
    get_object_or_404(HistoryLine, pk=pk).delete()
    return redirect('history')

# --- ПАРТНЕРЫ --- (без изменений)
def partner_list(request):
    partners = Partner.objects.all()
    template_name = 'manage/partner_list.html' if is_admin(request.user) else 'core/partners.html'
    return render(request, template_name, {'partners': partners})

@user_passes_test(is_admin)
def partner_add(request):
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('partners')
    else:
        form = PartnerForm()
    return render(request, 'manage/partner_form.html', {'form': form})

@user_passes_test(is_admin)
def partner_edit(request, pk):
    partner = get_object_or_404(Partner, pk=pk)
    if request.method == 'POST':
        form = PartnerForm(request.POST, request.FILES, instance=partner)
        if form.is_valid():
            form.save()
            return redirect('partners')
    else:
        form = PartnerForm(instance=partner)
    return render(request, 'manage/partner_form.html', {'form': form})

@user_passes_test(is_admin)
def partner_delete(request, pk):
    get_object_or_404(Partner, pk=pk).delete()
    return redirect('partners')

# --- ПРОЧЕЕ ---
def home(request):
    news = News.objects.all().order_by('-created_at')[:3]
    history_lines = HistoryLine.objects.all()[:3]
    partners = Partner.objects.all()
    return render(request, 'core/home.html', {
        'news_list': news,
        'history_lines': history_lines,
        'partners': partners
    })

def news_detail(request, pk):
    news = get_object_or_404(News, pk=pk)
    return render(request, 'core/news_detail.html', {'news': news})

def history_detail(request, pk):
    line = get_object_or_404(HistoryLine, pk=pk)
    return render(request, 'core/history_detail.html', {'line': line})

def contacts(request):
    return render(request, 'core/contacts.html')