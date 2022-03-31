from mutagen.mp3 import MP3
import datetime

def convert_sec_hh_mm_ss(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return hour, minutes, seconds

def totalTimer(times):
    td = datetime.timedelta(0)
    print('Initial Value ', td)
    duration = sum([datetime.timedelta(minutes=m, seconds=s) for m, s in times], td)
    print('Duration ', duration)
    return duration

if __name__ == '__main__':
    listOfSongs = ['1.mp3', '2.mp3', '3.mp3', '4.mp3', '5.mp3']
    timesList = []
    for song in listOfSongs:
        audio = MP3(song)
        _, m, s = convert_sec_hh_mm_ss(audio.info.length)
        timesList.append((m, s))

    # assert totalTimer(timesList) >= datetime.timedelta(0, 1415)
    print('Total Duration {} of the playlist'.format(totalTimer(timesList)))


