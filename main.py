def time_to_travel_light_year(speed_km_h):
    # Constants
    speed_of_light_km_s = 299792  # Speed of light in km/s
    seconds_per_hour = 3600  # Number of seconds in an hour
    hours_per_day = 24  # Number of hours in a day
    days_per_year = 365.25  # Average number of days in a year (accounting for leap years)

    # Calculate speed of light in km/h
    speed_of_light_km_h = speed_of_light_km_s * seconds_per_hour

    # Calculate distance of one light year in km
    distance_light_year_km = speed_of_light_km_h * hours_per_day * days_per_year

    # Calculate the time it takes to travel one light year at the given speed
    time_years = distance_light_year_km / speed_km_h
    
    return time_years

# Example usage
speed = 50  # Speed in km/h
time_required = time_to_travel_light_year(speed)
print(f"Time to travel one light year at {speed} km/h: {time_required} years")
