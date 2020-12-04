#! /usr/bin/env python

import re

with open('./data.txt') as f:
    passport_data = f.read().split('\n\n')


required_fields = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
formatted_passports = []

for pd in passport_data:
    formatted_passports.append(
        dict([x.split(':') for x in pd.split()])
    )


def is_passport_valid(passport):
    if not len(passport.keys() & required_fields) == 7:
        return False

    if not (1920 <= int(passport['byr']) <= 2002):
        return False
    if not (2010 <= int(passport['iyr']) <= 2020):
        return False
    if not (2020 <= int(passport['eyr']) <= 2030):
        return False
    if passport['hgt'].endswith('cm'):
        if not (150 <= int(passport['hgt'][:-2]) <= 193):
            return False
    else:
        if not (59 <= int(passport['hgt'][:-2]) <= 76):
            return False
    if not re.compile('^#[a-f0-9]{6}$').match(passport['hcl']):
        return False
    if not passport['ecl'] in ('amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth'):
        return False
    if not re.compile('^[0-9]{9}$').match(passport['pid']):
        return False

    return True


valid_passports = sum(
    1 for passport in formatted_passports
    if is_passport_valid(passport)
)


print(valid_passports)
