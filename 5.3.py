import keyboard

first_name = keyboard.input_string('Podaj imię: ')
last_name = keyboard.input_string('Podaj nazwisko: ')
age = keyboard.input_integer('Podaj wiek: ')
salary = keyboard.input_real('Podaj pensję: ')
is_salary_hidden = keyboard.input_boolean('Ukryć pensję? (y/n): ')

print('DANE PRACOWNIKA')
print('===============')
print(f'Imię: {first_name} {last_name}')
print(f'Wiek: {age}')

if not is_salary_hidden:
    print(f'Pensja: {salary}')
else:
    print('Pensja: Ukryta')
