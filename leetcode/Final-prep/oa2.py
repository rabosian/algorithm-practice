def isValidSchedule(locations, window, hours):
  startTime = window[0][0] + hours[0]
  
#   if window != window.sort():
#     return False

  for i in range(len(locations)-1):
    distance = abs(locations[i+1] - locations[i])
    if (startTime + distance) < window[i+1][0]:
        startTime += (window[i+1][0] + hours[i+1])
    else: 
        startTime += (distance + hours[i+1])
    print("start: ", startTime)
    if startTime > window[i+1][1]:
      return False

  return True



locations = [5, 7]
window = [[10,11],[11,12]]
hours = [1, 0]
print(isValidSchedule(locations, window, hours))
