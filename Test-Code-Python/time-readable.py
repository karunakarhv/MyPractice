def make_readable(totalTimeInSec):
    hours = totalTimeInSec
    hours = hours // 3600
    print('hours: {}'.format(hours))
    minutes = (totalTimeInSec % 3600)//60
    seconds = (totalTimeInSec % 3600)%60
    formattedString = "{:02d}:{:02d}:{:02d}".format(hours, minutes, seconds)
    print(formattedString)
    return formattedString

make_readable(359999)