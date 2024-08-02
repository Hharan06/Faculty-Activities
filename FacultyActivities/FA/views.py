import base64
from django.db import connection
from django.http import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from .models import AdminLogin,FacultyLogin,SDP_attended,Invited_talks,SDP_organised
from datetime import datetime
from calendar import month_name
from django.db.models import Q 
from functools import reduce
from itertools import groupby
from operator import itemgetter

# Create your views here.
def home(request):
    return render(request,'home.html')

def admin(request):
    return render(request,'login.html')

def admin_login(request):
    if request.method=='POST':
        
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        admin_user=AdminLogin.objects.get(username=username)

        if admin_user.password==password:
            return render(request,'dashboard.html')
        else:
            return render(request, 'login.html', {'error_message': 'Invalid username or password.'})
    return render(request,'login.html')

def fac_login(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')
        
        admin_user=FacultyLogin.objects.get(username=username)

        if admin_user.password==password:
            return render(request,'fac_dash.html')
        else:
            return render(request, 'fac_login.html', {'error_message': 'Invalid username or password.'})
    return render(request,'fac_login.html')

def admin_dashboard(request):
    if request.method == 'POST':
        academic_year_from = request.POST.get('academicYearFrom')
        academic_year_to = request.POST.get('academicYearTo')
        category = request.POST.get('selectedCategory')

        if category == 'SDP Attended':
            if academic_year_from and academic_year_to != 'None':
                sdp_attended = SDP_attended.objects.filter(academic_year__range=[academic_year_from, academic_year_to])
            elif academic_year_from:
                sdp_attended = SDP_attended.objects.filter(academic_year=academic_year_from)
            else:
                sdp_attended = SDP_attended.objects.all()

           
            grouped_data = {}
            for obj in sdp_attended:
                academic_year = obj.academic_year
                if academic_year not in grouped_data:
                    grouped_data[academic_year] = []
                grouped_data[academic_year].append(obj)

            return render(request, 'table_sort.html', {'grouped_data': grouped_data})
        
        if category == 'Invited Talks':
            if academic_year_from and academic_year_to != 'None':
                invited_talks = Invited_talks.objects.filter(academic_year__range=[academic_year_from, academic_year_to])
            elif academic_year_from:
                invited_talks = Invited_talks.objects.filter(academic_year=academic_year_from)
            else:
                invited_talks = Invited_talks.objects.all()

            grouped_data = {}
            for obj in invited_talks:
                academic_year = obj.academic_year
                if academic_year not in grouped_data:
                    grouped_data[academic_year] = []
                grouped_data[academic_year].append(obj)

            return render(request, 'it_table_sort.html', {'grouped_data': grouped_data})
        
        if category == 'SDP Organized':
            if academic_year_from and academic_year_to != 'None':
                sdp_organised = SDP_organised.objects.filter(academic_year__range=[academic_year_from, academic_year_to])
            elif academic_year_from:
                sdp_organised = SDP_organised.objects.filter(academic_year=academic_year_from)
            else:
                sdp_organised = SDP_organised.objects.all()
            grouped_data = {}
            for obj in sdp_organised:
                academic_year = obj.academic_year
                if academic_year not in grouped_data:
                    grouped_data[academic_year] = []
                grouped_data[academic_year].append(obj)

            return render(request, 'so_table_sort.html', {'grouped_data': grouped_data})

    return render(request, 'dashboard.html')

def fac_dashboard(request):
    if request.method == 'POST':
        yearfrom = request.POST.get('academicYearFrom')
        request.session['academic_year_variable'] = yearfrom
        print(request.session['academic_year_variable'])

        category = request.POST.get('selectedCategory')

        if category == 'SDP Attended':
            sdp_attended = SDP_attended.objects.filter(academic_year=yearfrom)
            return render(request, 'table_enter.html',{'sdp_attended':sdp_attended})
        
        if category == 'Invited Talks':
            invited_talks = Invited_talks.objects.filter(academic_year=yearfrom)
            return render(request, 'it_table_enter.html',{'invited_talks':invited_talks})
        
        if category == 'SDP Organized':
            sdp_organised = SDP_organised.objects.filter(academic_year=yearfrom)
            return render(request, 'so_table_enter.html',{'sdp_organised':sdp_organised})

    return render(request, 'fac_login.html')

def detail_enter(request):
    if request.method == 'POST':
        staff_attended = request.POST.get('staff_attended')
        nature_of_event = request.POST.get('nature_of_event')
        type_of_event = request.POST.get('type_of_event')
        name_of_event = request.POST.get('name_of_event')
        conducted_by_place = request.POST.get('conducted_by_place')
        no_of_days = request.POST.get('no_of_days')
        duration = request.POST.get('duration')
        proof_document = request.FILES.get('proof_document')

        academic_year_variable = request.session.get('academic_year_variable')

        sdp_attended = SDP_attended()
        sdp_attended.staff_attended = staff_attended
        sdp_attended.nature_of_event = nature_of_event
        sdp_attended.type_of_event = type_of_event
        sdp_attended.name_of_event = name_of_event
        sdp_attended.conducted_by = conducted_by_place
        sdp_attended.no_of_days = no_of_days
        sdp_attended.duration = duration
        sdp_attended.proof_document = proof_document
        sdp_attended.academic_year = academic_year_variable

        sdp_attended.save()
        print(academic_year_variable)

        sdp_attended = SDP_attended.objects.filter(academic_year=academic_year_variable)

        return render(request, 'table_enter.html', {'sdp_attended': sdp_attended})
    else:
        return render(request, 'enter_details.html')
    
def it_detail_enter(request):
    if request.method == 'POST':
        faculty = request.POST.get('faculty')
        type_of_event = request.POST.get('type_of_event')
        name_of_event = request.POST.get('name_of_event')
        duration = request.POST.get('duration')
        venue = request.POST.get('venue')
        date = request.POST.get('date')
        topic_of_talk = request.POST.get('topic_of_talk')

        academic_year_variable = request.session.get('academic_year_variable')

        invited_talks = Invited_talks()
        invited_talks.faculty = faculty
        invited_talks.type_of_event = type_of_event
        invited_talks.name_of_event = name_of_event
        invited_talks.duration = duration
        invited_talks.venue = venue
        invited_talks.date = date
        invited_talks.topic_of_talk = topic_of_talk
        invited_talks.academic_year = academic_year_variable

        invited_talks.save()
        print(academic_year_variable)

        invited_talks = Invited_talks.objects.filter(academic_year=academic_year_variable)

        return render(request, 'it_table_enter.html', {'invited_talks': invited_talks})
    else:
        return render(request, 'it_enter_details.html')
    
def so_detail_enter(request):
    if request.method == 'POST':
        Name_of_coord = request.POST.get('name_coord')
        type_of_event = request.POST.get('type_of_event')
        name_of_event = request.POST.get('name_of_event')
        duration = request.POST.get('duration')
        no_of_participants = request.POST.get('no_of_participants')
        resource_persons= request.POST.get('resource_persons')
        sponsors = request.POST.get('sponsors')
        academic_year_variable = request.session.get('academic_year_variable')

        sdp_organised=SDP_organised()
        sdp_organised.name_coord=Name_of_coord
        sdp_organised.type_of_event = type_of_event
        sdp_organised.name_of_event = name_of_event
        sdp_organised.duration=duration
        sdp_organised.no_of_participants=no_of_participants
        sdp_organised.resource_persons=resource_persons
        sdp_organised.sponsors=sponsors
        sdp_organised.academic_year = academic_year_variable



        sdp_organised.save()

        sdp_organised= SDP_organised.objects.filter(academic_year=academic_year_variable)

        return render(request, 'so_table_enter.html', {'sdp_organised':sdp_organised})
    else:
        return render(request, 'so_enter_details.html')

def goback_facdash(request):
    return render(request,'fac_dash.html')

def handle_filters(request):
    try:
        if request.method == 'POST':
            faculty_name = request.POST.get('facultyName')
            event_type = request.POST.get('eventType')
            name_of_event = request.POST.get('nameoftheevent')
            nature_of_event = request.POST.get('natureOfEvent')
            conducted_by = request.POST.get('conductedBy')
            no_of_days = request.POST.get('noOfDays')
            days_option = request.POST.get('choose')
            start_month = request.POST.get('startmonth')
            end_month = request.POST.get('endmonth')
            sdp_attended_queryset = SDP_attended.objects.all()
            if faculty_name:
                sdp_attended_queryset = sdp_attended_queryset.filter(staff_attended__icontains=faculty_name)
            if event_type:
                sdp_attended_queryset = sdp_attended_queryset.filter(type_of_event__icontains=event_type)
            if name_of_event:
                sdp_attended_queryset = sdp_attended_queryset.filter(name_of_event__icontains=name_of_event)
            if nature_of_event:
                sdp_attended_queryset = sdp_attended_queryset.filter(nature_of_event__icontains=nature_of_event)
            if conducted_by:
                sdp_attended_queryset = sdp_attended_queryset.filter(conducted_by__icontains=conducted_by)
            if days_option:
                if days_option=='same':
                    sdp_attended_queryset = sdp_attended_queryset.filter(no_of_days__icontains=no_of_days)
                elif days_option == 'greaterthan':
                    try:
                        no_of_days_int = int(no_of_days)
                        sdp_attended_queryset = sdp_attended_queryset.filter(no_of_days__gt=no_of_days_int)
                    except ValueError:
                        print("Error: Invalid literal for int() with base 10:", no_of_days)
                elif days_option == 'lesserthan':
                    try:
                        no_of_days_int = int(no_of_days)
                        sdp_attended_queryset = sdp_attended_queryset.filter(no_of_days__lt=no_of_days_int)
                    except ValueError:
                        print("Error: Invalid literal for int() with base 10:", no_of_days)
                else:
                    pass
                
            if start_month and end_month:
                months = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December']
                if start_month in months and end_month in months:
                    start_month = start_month.capitalize()
                    end_month = end_month.capitalize()
                    filters = []
                    start_index = months.index(start_month)
                    end_index = months.index(end_month)
                    for i in range(start_index, end_index + 1):
                        filters.append(Q(duration__icontains=f'-{months[i]}-'))
                    combined_filter = reduce(lambda x, y: x | y, filters)
                    sdp_attended_queryset = sdp_attended_queryset.filter(combined_filter)
            
            grouped_data = {}
            sorted_queryset = sorted(sdp_attended_queryset, key=lambda x: x.academic_year)
            for year, group in groupby(sorted_queryset, key=lambda x: x.academic_year):
                grouped_data[year] = list(group)

            return render(request, 'table_sort.html', {'grouped_data': grouped_data})
    except Exception as e:
        print(e)  
        return HttpResponse("An error occurred.")
    
def it_handle_filters(request):
    if request.method == 'POST':
        faculty = request.POST.get('facultyName')
        type_of_event = request.POST.get('eventType')
        name_of_event = request.POST.get('nameoftheevent')
        start_month = request.POST.get('startmonth')
        end_month = request.POST.get('endmonth')
        venue = request.POST.get('venue')
        date =  request.POST.get('date')
        topic_of_talk = request.POST.get('topicOfTalk')

        invited_talks_queryset = Invited_talks.objects.all()
        if faculty:
            invited_talks_queryset = invited_talks_queryset.filter(faculty__icontains=faculty)
        if type_of_event:
            invited_talks_queryset = invited_talks_queryset.filter(type_of_event__icontains=type_of_event)
        if name_of_event:
            invited_talks_queryset = invited_talks_queryset.filter(name_of_event__icontains=name_of_event)
        if topic_of_talk:
            invited_talks_queryset = invited_talks_queryset.filter(topic_of_talk__icontains=topic_of_talk)
        if venue:
            invited_talks_queryset = invited_talks_queryset.filter(venue__icontains=venue)
        if start_month and end_month:
                months = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December']
                if start_month in months and end_month in months:
                    start_month = start_month.capitalize()
                    end_month = end_month.capitalize()
                    filters = []
                    start_index = months.index(start_month)
                    end_index = months.index(end_month)
                    for i in range(start_index, end_index + 1):
                        filters.append(Q(duration__icontains=f'-{months[i]}-'))
                    combined_filter = reduce(lambda x, y: x | y, filters)
                    invited_talks_queryset = invited_talks_queryset.filter(combined_filter)
        
        grouped_data = {}
        sorted_queryset = sorted(invited_talks_queryset, key=lambda x: x.academic_year)
        for year, group in groupby(sorted_queryset, key=lambda x: x.academic_year):
            grouped_data[year] = list(group)

        return render(request, 'it_table_sort.html', {'grouped_data': grouped_data})

def so_handle_filters(request):
    try:
        if request.method == 'POST':
            # Initialize queryset with all objects of your model
            sdp_organised_queryset = SDP_organised.objects.all()
            
            name_coord = request.POST.get('coordinatorName')
            type_of_event = request.POST.get('eventType')
            name_of_event = request.POST.get('nameoftheevent')
            no_of_participants = request.POST.get('noOfParticipants')
            resource_persons= request.POST.get('resourcePerson')
            sponsors = request.POST.get('sponsors')
            start_month = request.POST.get('startmonth')
            end_month = request.POST.get('endmonth')
            
            if name_coord:
                sdp_organised_queryset = sdp_organised_queryset.filter(name_coord__icontains=name_coord)
            if type_of_event:
                sdp_organised_queryset = sdp_organised_queryset.filter(type_of_event__icontains=type_of_event)
            if name_of_event:
                sdp_organised_queryset = sdp_organised_queryset.filter(name_of_event__icontains=name_of_event)
            if no_of_participants:
                sdp_organised_queryset = sdp_organised_queryset.filter(no_of_participants__icontains=no_of_participants)
            if resource_persons:
                sdp_organised_queryset = sdp_organised_queryset.filter(resource_persons__icontains=resource_persons)
            if sponsors:
                sdp_organised_queryset = sdp_organised_queryset.filter(sponsors__icontains=sponsors)
            if start_month and end_month:
                months = ['January', 'February', 'March', 'April', 'May', 'June', 
                          'July', 'August', 'September', 'October', 'November', 'December']
                if start_month in months and end_month in months:
                    start_month = start_month.capitalize()
                    end_month = end_month.capitalize()
                    filters = []
                    start_index = months.index(start_month)
                    end_index = months.index(end_month)
                    for i in range(start_index, end_index + 1):
                        filters.append(Q(duration__icontains=f'-{months[i]}-'))
                    combined_filter = reduce(lambda x, y: x | y, filters)
                    sdp_organised_queryset = sdp_organised_queryset.filter(combined_filter)
            
            grouped_data = {}
            sorted_queryset = sorted(sdp_organised_queryset, key=lambda x: x.academic_year)
            for year, group in groupby(sorted_queryset, key=lambda x: x.academic_year):
                grouped_data[year] = list(group)
    
            return render(request, 'so_table_sort.html', {'grouped_data': grouped_data})

    except Exception as e:
        print(e)  
        return HttpResponse("An error occurred.")
    
def it_autosuggest(request):
    # Fetch distinct values from the InvitedTalk model
    faculty_name = list(Invited_talks.objects.values_list('facultyName', flat=True).distinct())
    event_type = list(Invited_talks.objects.values_list('eventType', flat=True).distinct())
    name_of_event = list(Invited_talks.objects.values_list('nameoftheevent', flat=True).distinct())
    duration = list(Invited_talks.objects.values_list('duration', flat=True).distinct())
    conducted_by = list(Invited_talks.objects.values_list('conductedBy', flat=True).distinct())
    topic_of_talk = list(Invited_talks.objects.values_list('topicOfTalk', flat=True).distinct())

    return render(request, 'it_table_sort.html', {
        'faculty_name': faculty_name,
        'event_type': event_type,
        'name_of_event': name_of_event,
        'duration': duration,
        'conducted_by': conducted_by,
        'topic_of_talk': topic_of_talk,
    })