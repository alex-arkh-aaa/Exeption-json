import datetime
#from api import register_booking

print('123'.rjust(10, '0'))
def create_booking(room_name, start, end):
    print('Начинаем создание бронирования')
    booking = Booking(room_name, start, end)
    res = {
        "created": False,
        "msg": "Комната занята",
        "booking": {
            "room_name": booking.room_name,
            "start_date": booking.start_date,
            "start_time": booking.start_time,
            "end_date": booking.end_date,
            "end_time": booking.end_time,
            "duration": booking.duration}
    }
    if register_booking(booking):
        res['created'] = True
        res['msg'] = 'Бронирование создано'
    try:
        raise register_booking(booking)
    except KeyError:
        res['created'] = False
        res['msg'] = 'Комната не найдена'
        print('Заканчиваем создание бронирования')
    return res


class Booking():
    def __init__(self, room_name, start, end):
        if end < start: raise ValueError('yyy yyyy y grrrrrrraaaaaaa')
        self.room_name = room_name
        self.start = start
        self.end = end
        self.duration = (end - start).seconds // 60
        start.month = start.month.rjust(2, '0')
        start.day = start.day.rjust(2, '0')
        self.start_date = f'{start.year}-{start.month}-{start.day}'
        end.month = end.month.rjust(2, '0')
        end.day = end.day.rjust(2, '0')
        self.end_date = f'{end.year}-{end.month}-{end.day}'
        self.start_time = str(start).split()[1][:-3]
        self.end_time = str(end).split()[1][:-3]

