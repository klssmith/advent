#! /usr/bin/env python

with open('./data.txt') as f:
    passport_data = f.read().split('\n\n')


required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
formatted_passports = []

for pd in passport_data:
    formatted_passports.append(
        dict([x.split(':') for x in pd.split()])
    )

valid_passports = sum(
    1 for passport in formatted_passports
    if len(passport.keys() & required_fields) == 7
)

print(valid_passports)
