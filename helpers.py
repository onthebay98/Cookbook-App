def timeToMinutes(timestring):
    if 'hrs' in timestring:
        times = timestring.split(' ')
        hours = times[0]
        minutes = times[2]

        return (int(60*float(hours) + float(minutes)) # total_minutes
    
    return int(timestring.split(' ')[0])