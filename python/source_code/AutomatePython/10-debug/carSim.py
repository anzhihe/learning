market_2nd = {'ns':'green', 'ew':'red'}
mission_16th = {'ns':'yellow', 'ew':'green'}

def switchLights(stoplight):
    assert 'red' in stoplight.values(), 'Neither light is red! ' + str(stoplight)
    for key in stoplight.keys():
        if stoplight[key] == 'green':
            stoplight[key] = 'yellow'
        elif stoplight[key] == 'yellow':
            stoplight[key] = 'red'
        elif stoplight[key] == 'red':
            stoplight[key] = 'green'

switchLights(market_2nd)
switchLights(mission_16th)