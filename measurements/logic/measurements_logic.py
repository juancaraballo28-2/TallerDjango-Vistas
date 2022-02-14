from ..models import Measurement

def get_measurements():
    measurements = Measurement.objects.all()
    return measurements


def get_measurement(var_pk):
    measurement = Measurement.objects.get(pk=var_pk)    
    return measurement

def create_measurement(measurement):
    measurement2 = Measurement(variable=measurement["variable"], value=measurement["value"], unit=measurement["unit"], place=measurement["place"], dateTime=measurement["dateTime"])
    measurement2.save()
    return measurement2


def update_measurement(var_pk, newvar):
    measurement = get_measurement(var_pk)
    measurement.variable = newvar["variable"]
    measurement.value = newvar["value"]
    measurement.unit = newvar["unit"]
    measurement.place = newvar["place"]
    measurement.dateTime = newvar["dateTime"]
    measurement.save()
    return measurement
