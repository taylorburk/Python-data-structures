def weekday_name(day_of_week):
    """Return name of weekday.
    
        >>> weekday_name(1)
        'Sunday'
        
        >>> weekday_name(7)
        'Saturday'
        
    For days not between 1 and 7, return None
    
        >>> weekday_name(9)
        >>> weekday_name(0)
    """
    days = ["None", "Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","None"]
    if day_of_week in range(0,8):
        return days[day_of_week]
    else:
        return None
    