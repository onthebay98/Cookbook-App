def stringToMinutes(timestring):
    '''
        converts string of the form '_ hrs _ mins' to minutes as int
    '''
    if (timestring != None) and ('hrs' in timestring):
        times = timestring.split(' ')
        hours = times[0]
        minutes = times[2]

        return (int(60*float(hours) + float(minutes))) # total_minutes
    
    return int(timestring.split(' ')[0])
                
def minutesToString(minutes):
    '''
        converts minutes as int to string of the form '_ hrs _ mins'
    '''
    if minutes == None:
        return 'Unspecified number of mins'
    elif minutes >= 60:
        hours = minutes//60
        leftover_minutes = minutes%60
        return str(f'{hours} hrs {leftover_minutes} mins')
    
    return str(f'{minutes} mins')