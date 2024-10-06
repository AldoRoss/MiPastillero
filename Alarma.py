import datetime
import time
from playsound import playsound

DAYS_MAP = {
    'lunes': 0,
    'martes': 1,
    'miércoles': 2,
    'jueves': 3,
    'viernes': 4,
    'sábado': 5,
    'domingo': 6
}

alarm_list = []

def add_alarm(alarm_time, days, concept):
    """Función para agregar o actualizar una alarma en la lista"""
    for day in days:
        # Verificar si ya existe una alarma en la misma hora y día
        existing_alarm = next((alarm for alarm in alarm_list if alarm['time'] == alarm_time and day in alarm['days']), None)

        if existing_alarm:
            # Concatenar el concepto si la alarma ya existe para ese día y hora
            existing_alarm['concept'] += f", {concept}"
            print(f"Alarma actualizada: {existing_alarm['concept']} a las {alarm_time} en el día {day}")
        else:
            # Crear una nueva alarma
            alarm = {
                'time': alarm_time,       # Hora de la alarma
                'days': [day],            # Días de la semana para la alarma
                'concept': concept        # Concepto o descripción de la alarma
            }
            alarm_list.append(alarm)
            print(f"Alarma agregada: {concept} a las {alarm_time} en el día {day}")

def check_alarms():
    """Función para verificar y activar las alarmas si coinciden con la hora y día actual"""
    while True:
        now = datetime.datetime.now()
        current_day = now.weekday()  # Día de la semana actual (0=lunes, 6=domingo)
        current_time = now.strftime("%H:%M")  # Hora actual en formato HH:MM

        # Verificar cada alarma en la lista
        for alarm in alarm_list:
            if current_day in alarm['days'] and current_time == alarm['time']:
                print(f"¡Alarma activada! Concepto: {alarm['concept']}")
                playsound('alarm.mp3')  # Reproduce el sonido de la alarma
                time.sleep(60)  # Evitar que suene repetidamente en el mismo minuto

        time.sleep(30)  # Verifica las alarmas cada 30 segundos

if __name__ == "__main__":
    while True:
        # Pedir al usuario la hora de la alarma
        alarm_time = input("Introduce la hora de la alarma (HH:MM): ")

        # Pedir los días de la semana
        days_input = input("Introduce los días (ejemplo: lunes, martes, miércoles): ").lower().split(", ")
        
        # Pedir el concepto o descripción de la alarma
        concept = input("Introduce el concepto de la alarma: ")

        # Convertir los días ingresados a números de 0 (lunes) a 6 (domingo)
        alarm_days = [DAYS_MAP[day.strip()] for day in days_input if day.strip() in DAYS_MAP]

        # Agregar la alarma a la lista (verificará si existe o no una alarma con la misma hora y día)
        add_alarm(alarm_time, alarm_days, concept)

        # Preguntar si se quiere agregar otra alarma
        more_alarms = input("¿Deseas agregar otra alarma? (sí/no): ").lower()
        if more_alarms != 'sí':
            break

    # Iniciar el proceso para revisar todas las alarmas
    print("Comenzando a verificar alarmas...")
    check_alarms()
