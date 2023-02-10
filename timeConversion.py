def timeConversion(s):
    # Write your code here
    noon = s[8:]
    formatHour = s[:8]
    splitHour = formatHour.split(':')
    
    if noon == 'PM' and int(splitHour[0]) < 12:
        splitHour[0] = str(int(splitHour[0]) + 12)
    elif noon == 'AM' : 
        if splitHour[0] == '12' : splitHour[0] = '00'
        
    return(':'.join(splitHour))

print(timeConversion('07:05:45PM'))