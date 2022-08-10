# Business Open Hours Ratio - Yelp

class TimeRange(object):
    """Represents a time range (the time between a start time and an end time)
    Example usage:
        >>> time_range = TimeRange('3-5')
        >>> print(time_range.start)
        3.0
        >>> print(time_range.end)
        5.0
    """

    def __init__(self, range_string):
        # for example, convert "3-5" into start=3.0 and end=5.0
        self.start, self.end = [
            float(time)
            for time in range_string.split('-')
        ]


def open_hours_ratio(query_time_range, open_hours):
    if not open_hours:
        return 0.0

    time_range = query_time_range.end-query_time_range.start
    total_open_hours = 0

    if type(open_hours) == list:
        for open_hour in open_hours:
            if open_hour.end < query_time_range.start or query_time_range.end < open_hour.start:
                continue
            if query_time_range.start < open_hour.start:
                if query_time_range.end > open_hour.end:
                    total_open_hours += open_hour.end - open_hour.start #
                else:
                    total_open_hours += query_time_range.end - open_hour.start #
            else:
                if query_time_range.end > open_hour.end:
                    total_open_hours += open_hour.end - query_time_range.start #
                else:
                    total_open_hours += query_time_range.end - query_time_range.start
    else:
        if open_hours.end < query_time_range.start:
            return 0.0

        if query_time_range.start < open_hours.start:
            if query_time_range.end > open_hours.end:
                total_open_hours += open_hours.end - open_hours.start
            else:
                total_open_hours += query_time_range.end - open_hours.start
        else:
            if query_time_range.end > open_hours.end:
                total_open_hours += open_hours.end - query_time_range.start
            else:
                total_open_hours += time_range

    return total_open_hours/time_range


time1 = TimeRange('5-22')
open1 = [TimeRange('0-2'), TimeRange('20-24')]


ratio = open_hours_ratio(time1, open1)
print('{:.2f}'.format(ratio))
