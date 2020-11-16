from django.shortcuts import render


def home_view(request):
    days = [
        {
            'id': 'day 1',
            'abbvTitle': 'Mon',
            'fullTitle': 'Monday',
            'events': [
                {
                    'details': 'Get rid of pointless stuff.',
                    'edit': False
                },
                {
                    'details': 'Try to buy PlayStation 5.',
                    'edit': False
                }
            ],
            'active': True
        },
        {
            'id': 'day 2',
            'abbvTitle': 'Tue',
            'fullTitle': 'Tuesday',
            'events': [],
            'active': True
        },
        {
            'id': 'day 3',
            'abbvTitle': 'Wen',
            'fullTitle': 'Wednesday',
            'events': [],
            'active': True
        },
        {
            'id': 'day 4',
            'abbvTitle': 'Thu',
            'fullTitle': 'Thursday',
            'events': [],
            'active': True
        },
        {
            'id': 'day 5',
            'abbvTitle': 'Fri',
            'fullTitle': 'Friday',
            'events': [],
            'active': True
        },
        {
            'id': 'day 6',
            'abbvTitle': 'Sat',
            'fullTitle': 'Saturday',
            'events': [],
            'active': True
        },
        {
            'id': 'day 7',
            'abbvTitle': 'Sun',
            'fullTitle': 'Sunday',
            'events': [],
            'active': True
        }
    ]
    return render(request, 'main/calendarComponents.html', {'days': days})
