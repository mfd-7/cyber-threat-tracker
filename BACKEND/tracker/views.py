from django.shortcuts import render
from django.http import JsonResponse
from .models import AttackLog
from .ml_service import predict_threat

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def honeypot_view(request):
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        ip_address = get_client_ip(request)

        threat_level = predict_threat(username, password)

        AttackLog.objects.create(
            ip_address=ip_address,
            username=username,
            password=password,
            threat_level=threat_level
        )

        return render(request, 'honeypot.html', {'error': True})

    return render(request, 'honeypot.html')

def dashboard_view(request):
    return render(request, 'dashboard.html')

def api_logs(request):
    logs = AttackLog.objects.order_by('-attack_time')[:20]
    data = [{
        'id': log.id,
        'ip_address': log.ip_address,
        'username': log.username,
        'password': log.password,
        'threat_level': log.threat_level,
        'attack_time': log.attack_time.strftime("%Y-%m-%d %H:%M:%S")
    } for log in logs]
    return JsonResponse({'logs': data})

def api_stats(request):
    logs = AttackLog.objects.all()
    total_attacks = logs.count()
    high_threats = logs.filter(threat_level='High Threat').count()
    low_threats = logs.filter(threat_level='Low Threat').count()

    ip_counts = {}
    for log in logs:
        ip_counts[log.ip_address] = ip_counts.get(log.ip_address, 0) + 1

    ips = list(ip_counts.keys())
    counts = list(ip_counts.values())

    return JsonResponse({
        'total_attacks': total_attacks,
        'high_threats': high_threats,
        'low_threats': low_threats,
        'ips': ips,
        'counts': counts
    })
