def trigger_alarm(temperatures, threshold=80):
    triggered_sensors = []
    
    for sensor, temp in temperatures.items():
        if temp > threshold:
            triggered_sensors.append(sensor)
            
    return triggered_sensors