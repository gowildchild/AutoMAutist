#################### ########### ######## ####### ####### ###### ## * ..
####### AutoMAutist - Digital Autism Assistant, Coach and Caretaker       d..
######       .                                                        *  d8..
##### e            d8 *            e    e  .   e        +   8   ,e  d8   d8 *
#### d8b   88__88_d88__ e88~-_    d8b  d8b    d8b__ 88 ____d8____"_d88 __d8__
### /Y88b  88  88 888  d888   i  d888bdY88b  /Y8b   88  88 88   88 C8    88 .
## /  Y88b 88  88 888  8888   | / Y88Y Y888b/  Y8b  88  88 88   88 Y8b   88 *
# /____Y88b88  88 888  Y888   '/   YY   Y8b/____Y8b 88  88 88   88  88D  88 .
#/      Y88"8_-88 "88_/ "88_-~/      *   Y/8b    \Yb"8_-88 "8_/ 8\_8P   "8_/
#        \        +          /           /.......
#
#        +                       https://github.com/gowildchild/AutoMAutist
#               Copyright (c)2009-2026 by Gunther Voet, All Rights Reserved
############################################################## #  #   #  *  .
# Released under strict Non-Commercial Open-Source License Terms.
from django.urls import path
from core.views import home_dashboard, domotica_dashboard, mount_new_policy_token
from core.domotica.views import execute_token_auth_endpoint
from core.mood import views as mood_views
from core.assist import views as assist_views
#from . import views

urlpatterns = [
    # ==========================================================
    # 1. CORE BACKEND FAILOVER API ENDPOINTS
    # ==========================================================
    # This is the endpoint Home Assistant or external edge clients POST to
    #path('api/trigger', views.execute_token_auth_endpoint, name='api-token-trigger'),
    path('api/trigger', execute_token_auth_endpoint, name='api-token-trigger'),
    path('api/trigger/', execute_token_auth_endpoint, name='api-token-trigger-slash'),

    path('api/cast/toggle', mood_views.toggle_cast_assist, name='api-cast-toggle'),
    path('api/cast/toggle/', mood_views.toggle_cast_assist, name='api-cast-toggle-slash'),
    path('api/mood/tags', mood_views.manage_emotional_tags, name='api-mood-tags'),
    path('api/mood/tags/', mood_views.manage_emotional_tags, name='api-mood-tags-slash'),

    path('api/mood/log', mood_views.ingest_mood_telemetry, name='api-mood-log'),
    path('api/mood/log/', mood_views.ingest_mood_telemetry, name='api-mood-log-slash'),

    path('mood/monitor/', mood_views.public_mood_dashboard, name='mood-monitor'),
    path('mood/monitor', mood_views.public_mood_dashboard, name='mood-monitor-no-slash'),
    path('assist/card/', assist_views.international_assist_card_view, name='assist-card'),
    path('assist/card', assist_views.international_assist_card_view, name='assist-card-no-slash'),
    path('assist/card/export/', assist_views.export_assist_card_config_view, name='assist-card-export'),

    # ==========================================================
    # 2. INTERACTIVE ADMINISTRATIVE INTERFACE OVERRIDES
    # ==========================================================
    # The primary landing grid console pane (Home Assistant Ingress entry)
    # path('', views.admin_dashboard, name='admin-dashboard'),
    path('', home_dashboard, name='admin-dashboard'),
    path('domotica/', domotica_dashboard, name='domotica-dashboard'),
    path('domotica', domotica_dashboard, name='domotica-dashboard-no-slash'),

    # Form processing target endpoint executing token generation configurations
    #path('device/provision', views.mount_new_policy_token, name='provision-token-device'),
    path('device/provision', mount_new_policy_token, name='provision-token-device'),
    path('device/provision/', mount_new_policy_token, name='provision-token-device-slash'),
]
