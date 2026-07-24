from .models import Mission
from .study_resources import STUDY_RESOURCES, CERT_ORDER

CERT_GROUPS = [
    {'code': 'ZCU', 'label': 'ZCU'},
    {'code': 'ZCS', 'label': 'ZCS'},
    {'code': 'ZCP', 'label': 'ZCP'},
    {'code': 'ZCE', 'label': 'ZCE'},
]

def extra_missions_menu(request):
    try:
        missions = Mission.objects.filter(active=True, track=Mission.TRACK_EXTRA).order_by('order', 'title')
    except Exception:
        missions = []
    return {'extra_missions_menu': missions}

def study_resources_menu(request):
    return {'study_resources_menu': STUDY_RESOURCES, 'cert_study_menu': CERT_ORDER}

def main_phases_menu(request):
    grouped = []
    try:
        for group in CERT_GROUPS:
            phases = Mission.objects.filter(active=True, track=Mission.TRACK_MAIN, certification=group['code']).order_by('order', 'title')
            grouped.append({**group, 'phases': phases})
    except Exception:
        grouped = [{**g, 'phases': []} for g in CERT_GROUPS]
    return {'certification_groups_menu': grouped}
