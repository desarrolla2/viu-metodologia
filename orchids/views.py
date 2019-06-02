from random import randint, choice

from django.contrib import messages
from django.shortcuts import render, redirect

from orchids.forms import OrchidForm, GreenhouseForm, NumberForm
from orchids.models import Vars, Orchid, Greenhouse, WEATHER_ANDES, WEATHER_COAST, STATE_NOT_ASSIGNED, STATE_ASSIGNED, \
    STATE_DESTROYED, STATE_SOLD, VARS_DAY


def index(request):
    return render(request, 'index.html', {
        'greenhouses': Greenhouse.objects.count(),
        'orchids': Orchid.objects.count()
    })


def simulate(request):
    form = NumberForm()
    if request.method == "POST":
        form = NumberForm(request.POST)
        if form.is_valid():
            sections = []
            for x in range(0, form.cleaned_data['number']):
                sections = __simulate_day(sections)

            return render(request, 'simulate.html', {'sections': sections})

    return render(request, "form_create.html", {'form': form})


def random(request):
    greenhouses = randint(2, 4)
    for x in range(0, greenhouses):
        model_instance = Greenhouse.create(randint(100000, 999999), choice([WEATHER_ANDES, WEATHER_COAST]),
                                           randint(10, 20), randint(100, 1000))
        model_instance.save()

    orchids = randint(6, 10)
    for x in range(0, orchids):
        model_instance = Orchid.create(randint(100000, 999999), choice([WEATHER_ANDES, WEATHER_COAST]),
                                       randint(10, 200), randint(5, 15), randint(16, 25), randint(1, 6),
                                       randint(1, 6))
        model_instance.save()

    messages.add_message(request, messages.INFO, '%d random greenhouses created successfully.' % greenhouses)
    messages.add_message(request, messages.INFO, '%d random orchids created successfully.' % orchids)

    return redirect('index')


def clear(request):
    greenhouses = Greenhouse.objects.count()
    orchids = Orchid.objects.count()

    Greenhouse.objects.all().delete()
    Orchid.objects.all().delete()

    day = __simulate_get_current_day()
    day.value = 1
    day.save()

    messages.add_message(request, messages.INFO, '%d greenhouses deleted successfully.' % greenhouses)
    messages.add_message(request, messages.INFO, '%d orchids deleted successfully.' % orchids)

    return redirect('index')


def orchid_create(request):
    form = OrchidForm()
    if request.method == "POST":
        form = OrchidForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.current_days_in_andes = model_instance.original_days_in_andes
            model_instance.current_days_in_coast = model_instance.original_days_in_coast
            model_instance.save()

            messages.add_message(request, messages.INFO, 'orchid created successfully.')
            return redirect('index')

    return render(request, "form_create.html", {'form': form})


def orchid_list(request):
    orchids = Orchid.objects.all()

    return render(request, "orchid_list.html", {'orchids': orchids})


def greenhouse_create(request):
    form = GreenhouseForm()
    if request.method == "POST":
        form = GreenhouseForm(request.POST)
        if form.is_valid():
            model_instance = form.save(commit=False)
            model_instance.available = model_instance.capacity
            model_instance.save()

            messages.add_message(request, messages.INFO, 'greenhouse created successfully.')
            return redirect('index')

    return render(request, "form_create.html", {'form': form})


def greenhouse_list(request):
    greenhouses = Greenhouse.objects.all()

    return render(request, "greenhouse_list.html", {'greenhouses': greenhouses})


def __simulate_sell(sections):
    orchids = Orchid.objects.filter(state=STATE_NOT_ASSIGNED, current_days_in_andes=0,
                                    current_days_in_coast=0).order_by('-number')
    if orchids.count() == 0:
        return sections

    logs = [{
        'message': 'Found %d orchids ready to sell.' % orchids.count(),
        'class': 'list-group-item-primary'
    }]
    message = ''
    for orchid in orchids:
        message += 'Orchid "%s" with %d plants sold, ' % (orchid.name, orchid.number)
        orchid.state = STATE_SOLD
        orchid.save()
    logs.append({
        'message': message,
        'class': 'padding-40'
    })
    day = __simulate_get_current_day()
    sections.append({'name': 'Day %d: selling ready orchids' % day.value, 'logs': logs})

    return sections


def __simulate_destroy(sections):
    orchids = Orchid.objects.filter(state=STATE_NOT_ASSIGNED).order_by('-number')
    if orchids.count() == 0:
        return sections

    logs = [{
        'message': 'Found %d orchids not assigned and it will be destroyed.' % orchids.count(),
        'class': 'list-group-item-primary'
    }]
    message = ''
    for orchid in orchids:
        message += 'Orchid "%s" with %d plants destroyed, ' % (orchid.name, orchid.number)
        orchid.state = STATE_DESTROYED
        orchid.save()
    logs.append({
        'message': message,
        'class': 'padding-40'
    })
    day = __simulate_get_current_day()
    sections.append({'name': 'Day %d: destroying unassigned orchids' % day.value, 'logs': logs})

    return sections


def __simulate_assign(sections, filter_by_preferred_weather=True, filter_by_prefered_temperature=True):
    orchids = Orchid.objects.filter(state=STATE_NOT_ASSIGNED).order_by('-number')
    if orchids.count() == 0:
        return sections
    assigned = 0
    greenhouses = Greenhouse.objects.filter().order_by('-available')
    logs = [{
        'message': 'Found %d orchids not assigned and ordered it by number descending.' % orchids.count(),
        'class': 'list-group-item-primary'
    }]
    message = ''
    for orchid in orchids:
        message += 'Orchid "%s" with %d plants, ' % (orchid.name, orchid.number)
    if len(message) > 0:
        logs.append({
            'message': message,
            'class': 'padding-40'
        })
    logs.append({
        'message': 'Found %d greenhouses and ordered it by available spaces descending.' % greenhouses.count(),
        'class': 'list-group-item-primary'
    })
    message = ''
    for greenhouse in greenhouses:
        message += 'Greenhouse "%s" with %d available spaces, ' % (greenhouse.name, greenhouse.available)
    if len(message) > 0:
        logs.append({
            'message': message,
            'class': 'padding-40'
        })
    for orchid in orchids:
        logs.append({
            'message': 'Start assignation of Orchid "%s" with preferred temperature %d-%d, preferred weather "%s", %d number of plants, available days %d in andes, %d in coast.' %
                       (orchid.name, orchid.min_temperature, orchid.max_temperature, orchid.preferred_weather,
                        orchid.number, orchid.current_days_in_andes, orchid.current_days_in_coast,),
            'class': 'list-group-item-primary'
        })
        for greenhouse in greenhouses:
            logs.append({
                'message': 'Evaluating Greenhouse "%s" with temperature %d,  climate "%s" and %d available spaces.' % (
                    greenhouse.name, greenhouse.temperature, greenhouse.weather, greenhouse.available,),
                'class': 'padding-40'
            })
            if greenhouse.available < orchid.number:
                logs.append({
                    'message': 'Not enought space available.',
                    'class': 'list-group-item-warning padding-80'
                })
                continue

            if greenhouse.weather == 'ANDES' and orchid.current_days_in_andes <= 0:
                logs.append({
                    'message': 'The lot does not have days available on the andes.',
                    'class': 'list-group-item-warning  padding-80'
                })
                continue

            if greenhouse.weather == 'COAST' and orchid.current_days_in_coast <= 0:
                logs.append({
                    'message': 'The lot does not have days available on the coast.',
                    'class': 'list-group-item-warning  padding-80'
                })
                continue

            if filter_by_preferred_weather and greenhouse.weather != orchid.preferred_weather:
                logs.append({
                    'message': 'Weather is not preferred.',
                    'class': 'list-group-item-warning  padding-80'
                })
                continue

            if filter_by_prefered_temperature and greenhouse.temperature < orchid.min_temperature:
                logs.append({
                    'message': 'Temperature is too low.',
                    'class': 'list-group-item-warning  padding-80'
                })
                continue

            if filter_by_prefered_temperature and greenhouse.temperature > orchid.max_temperature:
                logs.append({
                    'message': 'Temperature is too high.',
                    'class': 'list-group-item-warning padding-80'
                })
                continue

            orchid.greenhouse = greenhouse
            orchid.state = STATE_ASSIGNED
            greenhouse.available = greenhouse.available - orchid.number

            orchid.save()
            greenhouse.save()
            assigned += 1
            logs.append({
                'message': 'Orchid "%s" assigned to greenhouse "%s", %d spaces available.' % (
                    orchid.name, greenhouse.name, greenhouse.available),
                'class': 'list-group-item-success padding-80'
            })
            break

    if assigned > 0:
        logs.append({
            'message': 'Orchids assigned %d.' % assigned,
            'class': 'list-group-item-success'
        })

    day = __simulate_get_current_day()
    if filter_by_preferred_weather and filter_by_prefered_temperature:
        sections.append(
            {'name': 'Day %d: trying to assign by preferred weather and temperature' % day.value, 'logs': logs})
        return sections

    if filter_by_preferred_weather:
        sections.append({'name': 'Day %d: trying to assign by preferred weather' % day.value, 'logs': logs})
        return sections

    if filter_by_prefered_temperature:
        sections.append({'name': 'Day %d: trying to assign by preferred temperature' % day.value, 'logs': logs})
        return sections

    sections.append({'name': 'Day %d: trying to assign' % day.value, 'logs': logs})
    return sections


def __simulate_day(sections):
    day = __simulate_get_current_day()

    sections = __simulate_sell(sections)

    sections = __simulate_assign(sections)
    sections = __simulate_assign(sections, True, False)
    sections = __simulate_assign(sections, False, True)
    sections = __simulate_assign(sections, False, False)

    sections = __simulate_destroy(sections)

    orchids = Orchid.objects.filter(state=STATE_ASSIGNED).order_by('-number')
    if orchids.count() == 0:
        sections.append({'name': 'Day %d: updating orchids data' % day.value, 'logs': [
            {'message': 'Nothing to do.', 'class': ''}
        ]})
        __simulate_increment_day()

        return sections

    logs = [{
        'message': 'Found %d orchids ready to update.' % orchids.count(),
        'class': 'list-group-item-primary'
    }]
    for orchid in orchids:
        greenhouse = orchid.greenhouse
        if greenhouse.weather == WEATHER_ANDES:
            orchid.current_days_in_andes -= 1
            logs.append({
                'message': 'Orchid "%s" that is in ANDES,  with %d remaining days in andes and %d days in coast' %
                           (orchid.name, orchid.current_days_in_andes, orchid.current_days_in_coast),
                'class': ''
            })
            if orchid.current_days_in_andes == 0:
                orchid.greenhouse = None
                orchid.state = STATE_NOT_ASSIGNED
                logs.append({
                    'message': 'Orchid has been released',
                    'class': 'list-group-item-success padding-40'
                })

        if greenhouse.weather == WEATHER_COAST:
            orchid.current_days_in_coast -= 1
            logs.append({
                'message': 'Orchid "%s" that is in COAST,  with %d remaining days in andes and %d days in coast' %
                           (orchid.name, orchid.current_days_in_andes, orchid.current_days_in_coast),
                'class': ''
            })
            if orchid.current_days_in_coast == 0:
                orchid.greenhouse = None
                orchid.state = STATE_NOT_ASSIGNED
                logs.append({
                    'message': 'Orchid has been released',
                    'class': 'list-group-item-success padding-40'
                })
        orchid.save()
    sections.append({'name': 'Day %d: updating orchids data' % day.value, 'logs': logs})

    __simulate_increment_day()

    return sections


def __simulate_increment_day():
    day = __simulate_get_current_day()
    day.value += 1
    day.save()


def __simulate_get_current_day():
    entity = Vars.objects.filter(name=VARS_DAY).first()
    if entity is None:
        entity = Vars.create(VARS_DAY, 1)
        entity.save()

    return entity
