====================================================================
                    DJANGO IMPORT CHEAT SHEET
====================================================================

####################################################################
# 1. MODELS & DATABASE
####################################################################

from django.db import models

# Aggregation
from django.db.models import Avg, Sum, Count, Max, Min

# Query Expressions
from django.db.models import Q, F, Value

# Database Functions
from django.db.models.functions import Lower, Upper, Length, Now

# Transactions
from django.db import transaction

####################################################################
# 2. MODEL VALIDATORS
####################################################################

from django.core.validators import (
    MinValueValidator,
    MaxValueValidator,
    MinLengthValidator,
    MaxLengthValidator,
    EmailValidator,
    RegexValidator,
)

####################################################################
# 3. MODEL EXCEPTIONS
####################################################################

from django.core.exceptions import (
    ValidationError,
    ObjectDoesNotExist,
    PermissionDenied,
)

####################################################################
# 4. DJANGO ADMIN
####################################################################

from django.contrib import admin
from django.contrib.admin import ModelAdmin, TabularInline, StackedInline

####################################################################
# 5. URLS
####################################################################

from django.urls import (
    path,
    include,
    reverse,
    reverse_lazy,
)

####################################################################
# 6. VIEWS & SHORTCUTS
####################################################################

from django.shortcuts import (
    render,
    redirect,
    get_object_or_404,
)

####################################################################
# 7. HTTP RESPONSES
####################################################################

from django.http import (
    HttpResponse,
    JsonResponse,
    Http404,
    HttpResponseRedirect,
)

####################################################################
# 8. CLASS-BASED VIEWS
####################################################################

from django.views import View

from django.views.generic import (
    TemplateView,
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)

####################################################################
# 9. FORMS
####################################################################

from django import forms
from django.forms import ModelForm

####################################################################
# 10. AUTHENTICATION
####################################################################

from django.contrib.auth import (
    authenticate,
    login,
    logout,
)

from django.contrib.auth.models import User

from django.contrib.auth.decorators import (
    login_required,
    permission_required,
)

from django.contrib.auth.mixins import (
    LoginRequiredMixin,
)

####################################################################
# 11. MESSAGES
####################################################################

from django.contrib import messages

####################################################################
# 12. FILES & IMAGES
####################################################################

from django.core.files.storage import default_storage
from django.core.files.base import ContentFile

####################################################################
# 13. EMAIL
####################################################################

from django.core.mail import (
    send_mail,
    send_mass_mail,
    EmailMessage,
    EmailMultiAlternatives,
)

####################################################################
# 14. TEMPLATES
####################################################################

from django.template.loader import render_to_string

####################################################################
# 15. HTML UTILITIES
####################################################################

from django.utils.html import format_html

####################################################################
# 16. DATES & TIME
####################################################################

from django.utils import timezone

from datetime import (
    date,
    datetime,
    timedelta,
)

####################################################################
# 17. PAGINATION
####################################################################

from django.core.paginator import (
    Paginator,
    EmptyPage,
    PageNotAnInteger,
)

####################################################################
# 18. SIGNALS
####################################################################

from django.db.models.signals import (
    post_save,
    pre_save,
    post_delete,
)

from django.dispatch import receiver

####################################################################
# 19. CACHE
####################################################################

from django.core.cache import cache

####################################################################
# 20. SERIALIZATION
####################################################################

from django.core import serializers

####################################################################
# 21. MANAGEMENT COMMANDS
####################################################################

from django.core.management.base import BaseCommand

####################################################################
# 22. TESTING
####################################################################

from django.test import TestCase, Client

####################################################################
# 23. DJANGO REST FRAMEWORK (DRF)
####################################################################

# API Views
from rest_framework.views import APIView

# Generic Views
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView,
    ListCreateAPIView,
    RetrieveUpdateAPIView,
    RetrieveDestroyAPIView,
    RetrieveUpdateDestroyAPIView,
)

# ViewSets
from rest_framework.viewsets import (
    ViewSet,
    ModelViewSet,
    ReadOnlyModelViewSet,
)

# Response
from rest_framework.response import Response

# Status Codes
from rest_framework import status

# Decorators
from rest_framework.decorators import (
    api_view,
    permission_classes,
    authentication_classes,
)

# Permissions
from rest_framework.permissions import (
    AllowAny,
    IsAuthenticated,
    IsAdminUser,
    IsAuthenticatedOrReadOnly,
)

# Authentication
from rest_framework.authentication import (
    TokenAuthentication,
    SessionAuthentication,
    BasicAuthentication,
)

# Serializers
from rest_framework import serializers

# Pagination
from rest_framework.pagination import (
    PageNumberPagination,
    LimitOffsetPagination,
)

# Filters
from rest_framework.filters import (
    SearchFilter,
    OrderingFilter,
)

####################################################################
# 24. DJANGO FILTER
####################################################################

from django_filters.rest_framework import DjangoFilterBackend

####################################################################
# 25. JWT AUTHENTICATION
####################################################################

from rest_framework_simplejwt.tokens import RefreshToken

####################################################################
# 26. URL ENCODING
####################################################################

from urllib.parse import urlencode

####################################################################
# 27. JSON
####################################################################

import json

####################################################################
# 28. UUID
####################################################################

import uuid

####################################################################
# 29. OS & PATHS
####################################################################

import os
from pathlib import Path

####################################################################
# 30. RANDOM & MATH
####################################################################

import random
import math

####################################################################
# 31. REGULAR EXPRESSIONS
####################################################################

import re

####################################################################
# 32. LOGGING
####################################################################

import logging

logger = logging.getLogger(__name__)

####################################################################
# 33. TYPING (Python)
####################################################################

from typing import (
    List,
    Dict,
    Tuple,
    Optional,
)

====================================================================
                  MOST USED IMPORTS (Daily)
====================================================================

# Models
from django.db import models

# Views
from django.shortcuts import render, redirect, get_object_or_404

# URLs
from django.urls import path, reverse

# Admin
from django.contrib import admin

# Forms
from django import forms

# HTML
from django.utils.html import format_html

# Database Aggregation
from django.db.models import Avg, Count, Sum

# HTTP
from django.http import JsonResponse, HttpResponse

# Authentication
from django.contrib.auth import authenticate, login, logout

# DRF
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

# Email
from django.core.mail import send_mail

====================================================================