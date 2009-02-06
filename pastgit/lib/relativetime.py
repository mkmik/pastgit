import datetime as dt
import time

_partialMinute = 45 * 60
_partialHour   = 90 * 60
_fullDay       = 24 * 60 * 60
_twoDays       = _fullDay * 2

def relative_time(tt):
    """
    """
    now = dt.datetime.utcnow()

    now = time.mktime(now.timetuple())
    date = time.mktime(tt)
    
    delta = now - date

    if delta < 60:
        return u"less than a minute ago"
    elif delta < 120:
        return u"about a minute ago"
    elif delta < _partialMinute:
        return u"%d minutes ago" % int(delta / 60)
    elif delta < _partialHour:
        return u"about an hour ago"
    elif delta < _fullDay:
        return u"%d hours ago" % int(delta / 3600)
    elif delta < _twoDays:
        return u"1 day ago"
    else:
        return u'%d days ago' % int(delta / 86400)
