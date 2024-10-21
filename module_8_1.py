# модуль 8_1 Try и Except
# ==========================================
def add_everything_up(a, b):
    isinstance(a, (int, float, str))
    isinstance(b, (int, float, str))
    try:
        summ_ = a + b
        summ_ = round(summ_, 3)
        return summ_
    except TypeError:
        return f'{a}{b}'

print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
