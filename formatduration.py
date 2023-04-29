import math
def format_duration(seconds):
    if seconds == 0:
        return "now"
    years = math.floor((math.floor((math.floor(math.floor((seconds/60))/60))/24))/365)
    seconds = seconds - (years*365*24*(60**2))
    days = math.floor((math.floor(math.floor((seconds/60))/60))/24)
    seconds = seconds - (days*24*(60**2))
    hours = math.floor(math.floor((seconds/60))/60)
    seconds = seconds - (hours*(60**2))
    minutes = math.floor(seconds/60)
    seconds = seconds - (minutes*60)
    idk = [years,days,hours,minutes,seconds]
    times = ["years","days","hours", "minutes", "seconds"]
    timesingular = ['year','day','hour','minute','second']
    timeselected = []
    timetosay = []
    count = 0
    i = 0
    for time in idk:
        if time != 0:
            timeselected.append(time)
            timetosay.append(times[i])
            count += 1
        i += 1
            
    vals = []
    newtimes = []
    if count == 1 and len(timetosay) == 1:
        if timeselected[0] <= 1:
            return f'{timeselected[0]}' + " " + timesingular[times.index(timetosay[0])]
        else:
            return f'{timeselected[0]}' + " " + timetosay[0]
    else:  
        ans = ''
        for time in timetosay:
            newtime = time
            val = timeselected[timetosay.index(time)]
            if val <= 1:
                newtime = timesingular[times.index(time)]
                newtimes.append(newtime)
            else:
                newtimes.append(newtime)
            vals.append(val)
            
        if count == 2:
            return f'{vals[0]}' + ' ' + f'{newtimes[0]}' + ' and ' + f'{vals[1]}' + ' ' + f'{newtimes[1]}'
        else:
            somelist = []
            numstoinsert = []
            i = 0
            for val in vals:
                somelist.append(f'{val}' + ' ' + f'{newtimes[i]}')
                i += 1
            n = 1
            i = 0
            for element in somelist:
                numstoinsert.append(n)
                n += 2
            for num in numstoinsert:
                if i == count-2:
                    somelist.insert(num, " and ")
                    break
                else:
                    somelist.insert(num, ", ")
                i += 1
                
            returnthis = ''.join(somelist)
            returnthisnew = list(returnthis)
            
    return ''.join(returnthisnew)
seconds = 1000
print(format_duration(seconds))
