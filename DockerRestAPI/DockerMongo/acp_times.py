"""
Open and close time calculations
for ACP-sanctioned brevets
following rules described at https://rusa.org/octime_alg.html
and https://rusa.org/pages/rulesForRiders
"""
import arrow

def open_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
       brevet_dist_km: number, the nominal distance of the brevet
           in kilometers, which must be one of 200, 300, 400, 600,
           or 1000 (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control open time.
       This will be in the same time zone as the brevet start time.
    """

    # Sets overall time limits for races with control distance greater than
    # brevet distance. Source: rusa.org/pages/rulesForRiders
    if control_dist_km >= brevet_dist_km:
      if brevet_dist_km == 200:
        open_time = arrow.get(brevet_start_time).shift(minutes=353).isoformat()
      elif brevet_dist_km == 300:
        open_time = arrow.get(brevet_start_time).shift(minutes=540).isoformat()
      elif brevet_dist_km == 400:
        open_time = arrow.get(brevet_start_time).shift(minutes=728).isoformat()
      elif brevet_dist_km == 600:
        open_time = arrow.get(brevet_start_time).shift(minutes=1128).isoformat()
      elif brevet_dist_km == 1000:
        open_time = arrow.get(brevet_start_time).shift(minutes=1985).isoformat()
      return open_time

    speed = (34.0, 32.0, 30.0, 28.0, 26.0)
    speed_index = 0
    time = 0

    # Calculates time depending on where the control distance is in the brevet.
    while (speed_index < 3 and control_dist_km > 200):
      control_dist_km -= 200
      time += (200 / speed[speed_index])
      speed_index += 1
    # Use remaining brevet distance
    time += control_dist_km / speed[speed_index]
    # Convert time to minutes
    time = int((time * 60) + .5)
    return arrow.get(brevet_start_time).shift(minutes=time).isoformat()

def close_time(control_dist_km, brevet_dist_km, brevet_start_time):
    """
    Args:
       control_dist_km:  number, the control distance in kilometers
          brevet_dist_km: number, the nominal distance of the brevet
          in kilometers, which must be one of 200, 300, 400, 600, or 1000
          (the only official ACP brevet distances)
       brevet_start_time:  An ISO 8601 format date-time string indicating
           the official start time of the brevet
    Returns:
       An ISO 8601 format date string indicating the control close time.
       This will be in the same time zone as the brevet start time.
    """

    # Sets overall time limits for races with control distance greater than
    # brevet distance. Source: rusa.org/pages/rulesForRiders
    if control_dist_km >= brevet_dist_km:
      if brevet_dist_km == 200:
        close_time = arrow.get(brevet_start_time).shift(minutes=810).isoformat()
      elif brevet_dist_km == 300:
        close_time = arrow.get(brevet_start_time).shift(minutes=1200).isoformat()
      elif brevet_dist_km == 400:
        close_time = arrow.get(brevet_start_time).shift(minutes=1620).isoformat()
      elif brevet_dist_km == 600:
        close_time = arrow.get(brevet_start_time).shift(minutes=2400).isoformat()
      elif brevet_dist_km == 1000:
        close_time = arrow.get(brevet_start_time).shift(minutes=4500).isoformat()
      return close_time
    elif control_dist_km == 0:
      close_time = arrow.get(brevet_start_time).shift(minutes=60).isoformat()
      return close_time

    speed = (15.0, 15.0, 15.0, 11.428, 13.333)
    speed_index = 0
    time = 0

    # Calculates time depending on where the control distance is in the brevet.
    while (speed_index < 3 and control_dist_km > 200):
      control_dist_km -= 200
      time += (200 / speed[speed_index])
      speed_index += 1
    # Use remaining brevet distance
    time += control_dist_km / speed[speed_index]
    # Convert time to minutes
    time = int((time * 60) + .5)
    return arrow.get(brevet_start_time).shift(minutes=time).isoformat()
