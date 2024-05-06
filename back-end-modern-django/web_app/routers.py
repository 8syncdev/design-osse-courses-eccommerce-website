# Load Env to protect secret routes
from dotenv import load_dotenv
from dev_core.settings.settings import BASE_DIR
load_dotenv(BASE_DIR / '.env')
import os
# API View
from .routers_dev.api_view_dev.auth.auth_signup_av import AuthSignUpAV
from .routers_dev.api_view_dev.auth.auth_signin_av import AuthSignInAV
from .routers_dev.api_view_dev.auth.auth_token_av import AuthTokenAV


# ----------------------------------------------------------------
# Register View Sets
from rest_framework.routers import DefaultRouter
from .routers_dev.view_set_dev.user_vs import UserVS
from .routers_dev.view_set_dev.course_vs import CourseVS
from .routers_dev.view_set_dev.lesson_vs import LessonVS
from .routers_dev.view_set_dev.detail_lesson_vs import DetailLessonVS
from typing import *
from dev_core.settings.settings import API_ROUTE

router = DefaultRouter()
'''
    users/ : list, create
    users/{pk}/ : retrieve, update, destroy
'''
router.register(f'{API_ROUTE}/users', UserVS, basename='user-vs')
'''
    courses/ : list, create
    courses/{pk}/ : retrieve, update, destroy
'''
router.register(f'{API_ROUTE}/courses', CourseVS, basename='course-vs')
'''
    lessons/ : list, create
    lessons/{pk}/ : retrieve, update, destroy
'''
router.register(f'{API_ROUTE}/lessons', LessonVS, basename='lesson-vs')
'''
    detail-lessons/ : list, create
    detail-lessons/{pk}/ : retrieve, update, destroy
'''
router.register(f'{API_ROUTE}/detail-lessons', DetailLessonVS, basename='detail-lesson-vs')

# ROUTE_NAME_LITERALS = '/courses/' | '/lessons/' | '/detail-lessons/' | '/users/'


# ----------------------------------------------------------------
#--------------------------------------------------------------
import random
import json
from django.utils.translation import gettext as _
from django.utils.safestring import mark_safe
from django.http import HttpRequest


def dashboard_callback(request: HttpRequest, context):
    # print(request.get_full_path())
    WEEKDAYS = [
        "Mon",
        "Tue",
        "Wed",
        "Thu",
        "Fri",
        "Sat",
        "Sun",
    ]

    positive = [[1, random.randrange(8, 28)] for i in range(1, 28)]
    negative = [[-1, -random.randrange(8, 28)] for i in range(1, 28)]
    average = [r[1] - random.randint(3, 5) for r in positive]
    performance_positive = [[1, random.randrange(8, 28)] for i in range(1, 28)]
    performance_negative = [[-1, -random.randrange(8, 28)] for i in range(1, 28)]

    context.update(
        {
            "navigation": [
                {
                    "title": _("Dashboard"),
                    "link": "/",
                    "active": True
                },
                {
                    "title": _("Analytics"),
                    "link": "#"
                },
                {
                    "title": _("Settings"),
                    "link": "#"
                },
            ],
            "filters": [
                {
                    "title": _("All"),
                    "link": "#",
                    "active": True
                },
                {
                    "title": _("New"),
                    "link": "#",
                },
            ],
            "kpi": [
                {
                    "title": "Product A Performance",
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps({"labels": [WEEKDAYS[day % 7] for day in range(1, 28)], "datasets": [{"data": average, "borderColor": "#9333ea"}]}),
                },
                {
                    "title": "Product B Performance",
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                },
                {
                    "title": "Product C Performance",
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                },
            ],
            "progress": [
                {"title": "Social marketing e-book", "description": " $1,234.56", "value": random.randint(10, 90)},
                {"title": "Freelancing tasks", "description": " $1,234.56", "value": random.randint(10, 90)},
                {"title": "Development coaching", "description": " $1,234.56", "value": random.randint(10, 90)},
                {"title": "Product consulting", "description": " $1,234.56", "value": random.randint(10, 90)},
                {"title": "Other income", "description": " $1,234.56", "value": random.randint(10, 90)},
            ],
            "chart": json.dumps(
                {
                    "labels": [WEEKDAYS[day % 7] for day in range(1, 28)],
                    "datasets": [
                        {
                            "label": "Example 1",
                            "type": "line",
                            "data": average,
                            "backgroundColor": "#f0abfc",
                            "borderColor": "#f0abfc",
                        },
                        {
                            "label": "Example 2",
                            "data": positive,
                            "backgroundColor": "#9333ea",
                        },
                        {
                            "label": "Example 3",
                            "data": negative,
                            "backgroundColor": "#f43f5e",
                        },
                    ],
                }
            ),
            "performance": [
                {
                    "title": _("Last week revenue"),
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps({"labels": [WEEKDAYS[day % 7] for day in range(1, 28)], "datasets": [{"data": performance_positive, "borderColor": "#9333ea"}]}),
                },
                {
                    "title": _("Last week expenses"),
                    "metric": "$1,234.56",
                    "footer": mark_safe(
                        '<strong class="text-green-600 font-medium">+3.14%</strong>&nbsp;progress from last week'
                    ),
                    "chart": json.dumps({"labels": [WEEKDAYS[day % 7] for day in range(1, 28)], "datasets": [{"data": performance_negative, "borderColor": "#f43f5e"}]}),
                },
            ]
        },
    )

    return context

