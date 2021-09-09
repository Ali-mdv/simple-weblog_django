from . import jalali
from django.utils import timezone


def convert_number_to_persian(str_num):
    persian_number = {'1':'۱','2':'۲','3':'۳','4':'۴','5':'۵','6':'۶','7':'۷','8':'۸','9':'۹','0':'۰'}

    for e,p in persian_number.items():
        str_num = str_num.replace(e,p)
    return(str_num)

def convert_to_jalali(time):
    jalali_month = {1:'فروردین',2:'اردیبهشت',3:'خرداد',4:'تير',5:'مرداد',6:'شهريور',7:'مهر',8:'آبان',9:'آذر',10:'دي',11:'بهمن',12:'اسفند'}
    time = timezone.localtime(time)
    time_str = '{},{},{}'.format(time.year,time.month,time.day)
    time_tuple = jalali.Gregorian(time_str).persian_tuple()

    output = f'{time_tuple[2]} {jalali_month[time_tuple[1]]} {time_tuple[0]} ساعت {time.hour}:{time.minute}'
    return convert_number_to_persian(output)
