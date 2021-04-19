car_plates = ['113', '217', '343', '434', '536']
odd_days = ["SU", "TU", "TH"]
even_days = ["SA", "MO", "WE"]
today = input("Enter day of a week SAturday to FRriday: ").upper()
pass_list = []
for plate in car_plates:
    last_digit = int(plate[-1])
    if today in odd_days and last_digit % 2 != 0:
        pass_list.append(plate)
    elif today in even_days and last_digit % 2 == 0:
        pass_list.append(plate)
    elif today == "FR":
        pass_list.append(plate)
print(*pass_list, sep='\n')