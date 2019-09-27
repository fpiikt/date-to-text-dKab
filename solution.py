"""
  Автор: Кабардинов Дмитрий, группа №P3355
  
  Решение реализовано внутри класса DateToTextClass и содержится внутри метода convert
 
"""
class DateToTextClass():
    days = {
        1: 'первое',
        2: 'второе',
        3: 'третье',
        4: 'четвёртое',
        5: 'пятое',
        6: 'шестое',
        7: 'седьмое',
        8: 'восьмое',
        9: 'девятое',
        10: 'десятое',
        11: 'одиннадцатое',
        12: 'двенадцатое',
        13: 'тринадцатое',
        14: 'четырнадцатое',
        15: 'пятнадцатое',
        16: 'шестнадцатое',
        17: 'семнадцатое',
        18: 'восемнадцатое',
        19: 'девятнадцатое',
        20: 'двадцатое',
        21: 'двадцать первое',
        22: 'двадцать второе',
        23: 'двадцать третье',
        24: 'двадцать четвертое',
        25: 'двадцать пятое',
        26: 'двадцать шестое',
        27: 'двадцать седьмое',
        28: 'двадцать восьмое',
        29: 'двадцать девятое',
        30: 'тридцатое',
        31: 'тридцать первое'
    }

    months = {
        1: 'января',
        2: 'февраля',
        3: 'марта',
        4: 'апреля',
        5: 'мая',
        6: 'июня',
        7: 'июля',
        8: 'августа',
        9: 'сентября',
        10: 'октября',
        11: 'ноября',
        12: 'декабря',
    }

    hours = {
        'singular': 'час',
        'plural': 'часов',
        'plural_alt': 'часа'
    }

    minutes = {
        'singular': 'минута',
        'plural': 'минут',
        'plural_alt': 'минуты'
    }

    seconds = {
        'singular': 'секунда',
        'plural': 'секунд',
        'plural_alt': 'секунды'
    }
    
    thousands = {
        'singular': 'тысяча',
        'plural': 'тысяч',
        'plural_alt': 'тысячи',
    }

    numbers = {
        1: {'fem': 'одна', 'mus': 'один' },
        2: {'fem': 'две', 'mus': 'два' },
        3: 'три',
        4: 'четыре',
        5: 'пять',
        6: 'шесть',
        7: 'семь',
        8: 'восемь',
        9: 'девять',
    }

    hundreds = {
        1: 'сто',
        2: 'двести',
        3: 'триста',
        4: 'четыреста',
        5: 'пятьсот',
        6: 'шестьсот',
        7: 'семьсот',
        8: 'восемьсот',
        9: 'девятьсот',
    }

    tens = {
        1: 'десять',
        2: 'двадцать',
        3: 'тридцать',
        4: 'сорок',
        5: 'пятьдесят',
        6: 'шестьдесят',
        7: 'семьдесят',
        8: 'восемьдесят',
        9: 'девяносто',
    }

    tensRound = {
        1: 'десятого',
        2: 'двадцатого',
        3: 'тридцатого',
        4: 'сорокового',
        5: 'пятидесятого',
        6: 'шестидесятого',
        7: 'семидесятого',
        8: 'восьмидесятого',
        9: 'девяностого',
    }

    yearEndings = {
        0: 'нулевого',
        1: 'первого',
        2: 'второго',
        3: 'третьего',
        4: 'четвёртого',
        5: 'пятого',
        6: 'шестого',
        7: 'седьмого',
        8: 'восьмого',
        9: 'девятого',  
    }

    teens = {
        11: 'одиннадцать',
        12: 'двенадцать',
        13: 'тринадцать',
        14: 'четырнадцать',
        15: 'пятнадцать',
        16: 'шестнадцать',
        17: 'семнадцать',
        18: 'восемнадцать',
        19: 'девятнадцать',
    }

    yearPrefixes = {
            1: '',
            2: 'двух',
            3: 'трёх',
            4: 'четырёх',
            5: 'пяти',
            6: 'шести',
            7: 'семи',
            8: 'восьми',
            9: 'девяти',
        }

    def __init__(self, dateString):
        """"dateString is a date in DD.MM.YYYY HH:MM:SS format that needs to be converted to text"""
        self.dateString = dateString

    def convert(self):
        """parses date string and returns its text representation in russian language"""
        [date, time] = self.dateString.split(' ')
        [day, month, year] = [int(x) for x in date.split('.')]
        [hours, minutes, seconds] = [int(x) for x in time.split(':')]
        
        hoursUnits = self.getUnitsForNumber(hours, self.hours)
        minutesUnits = self.getUnitsForNumber(minutes, self.minutes)
        secondsUnits = self.getUnitsForNumber(seconds, self.seconds)
        dayWord = self.days[day]
        monthWord = self.months[month]
        yearWord = self.getYear(year)
        hoursWord = self.getTimeNumber(hours, 'mus')
        minutesWord = self.getTimeNumber(minutes, 'fem')
        secondsWord = self.getTimeNumber(seconds, 'fem')
        return f'{dayWord} {monthWord} {yearWord} года {hoursWord} {hoursUnits} {minutesWord} {minutesUnits} {secondsWord} {secondsUnits}'

    def getThousands(self, number):
        thousands = number // 1000
        if thousands == 0:
            return None
        else:
            numWord = self.numbers[thousands]
            firstWord = numWord['fem'] if isinstance(numWord, dict) else numWord
            secondWord = self.getUnitsForNumber(thousands, self.thousands)
            return f'{firstWord} {secondWord}'
    
    def getHundreds(self, number):
        hundreds = number // 100 % 10 # e.g. 2019 // 100 = 20
        if hundreds == 0: # e.g. 34 // 100 = 0
            return None
        return self.hundreds[hundreds]
    
    def getTens(self, number):
        tens = number // 10 % 10
        return None if tens == 0 else self.tens[tens]
            
    def getYear(self, number):
        """return text representation of year number"""
        orders = []

        # 1. getting millenias
        if number % 1000 == 0 and number // 1000 is not 0: # 1000, 2000, 3000, etc. (but not less than 1000)
            thousands = number // 1000
            return f'{self.yearPrefixes[thousands]}тысячного' # тысячного, двухтысячного, трёхтысячного
        else:
            orders.insert(0, self.getThousands(number))
        # 2. getting centuries
        if number % 100 == 0 and number // 100 is not 0: # 1200, 2100, 900, etc. (but not less than 100)
            hundreds = number // 100
            if hundreds >= 10:
                hundreds = hundreds % 10 # we are taking the second digit
            return f'{self.yearPrefixes[hundreds]}сотого' if orders[0] is None else f'{orders[0]} {self.yearPrefixes[hundreds]}сотого'
        else:
            orders.insert(1, self.getHundreds(number))
        # 3. getting decades
        if number % 10 == 0 and number // 10 is not 0: # 1340, 560, 30, etc. (but not less than 10)
            decades = (number // 10) % 10
            orders.insert(2, self.tensRound[decades])
            return ' '.join([x for x in orders if x is not None])
        elif 10 < (number % 100) and (number % 100) < 20: # teens
            orders.insert(2, f'{self.teens[number % 100][:-1]}ого')
            return ' '.join([x for x in orders if x is not None])
        else:
            orders.insert(2, self.getTens(number))
        # 4. getting precise year
        year = number % 10
        orders.insert(3, self.yearEndings[year])
        return ' '.join([x for x in orders if x is not None])

    def getTimeNumber(self, number, gender):
        orders = []
        """returns corresponding text for a number in time (hours/minutes/seconds)
        gender can be either 'fem' or 'mus'
        """
        if number == 0:
            return 'ноль'
        elif number < 10:
            orders.insert(0, 'ноль')
            lastDigit = number
        elif number % 10 == 0:
            return self.tens[number // 10]
        elif 10 < number and number < 20:
            return self.teens[number]
        else:
            tens = number // 10
            orders.insert(0, self.tens[tens])
            lastDigit = number % 10
        numWord = self.numbers[lastDigit]
        word = numWord[gender] if isinstance(numWord, dict) else numWord
        orders.insert(1, word)
        return ' '.join(orders)

    def getUnitsForNumber(self, number, words):
        """receives number and list of forms of a word to choose from (минута/минут/минуты)
           returns the correct form of the word
        """
        if 10 <= number and number <= 20:
            return words['plural']
        remainder = number % 10
        if remainder == 1:
            return words['singular']
        if 2 <= remainder and remainder <= 4:
            return words['plural_alt']
        return words['plural']

    def getDay(self, number):
        return self.days[number]

    def getMonth(self, number):
        return self.months[number]

if __name__ == '__main__':
    res1 = DateToTextClass('25.09.2019 08:17:59')
    assert res1.getUnitsForNumber(22, res1.minutes) == "минуты"
    assert res1.getUnitsForNumber(21, res1.seconds) == "секунда"
    assert res1.getUnitsForNumber(13, res1.hours) == "часов"
    assert res1.getUnitsForNumber(2, res1.hours) == "часа"
    assert res1.getDay(25) == 'двадцать пятое'
    assert res1.getMonth(11) == 'ноября'
    assert res1.getYear(1990) == 'одна тысяча девятьсот девяностого'
    assert res1.getYear(1991) == 'одна тысяча девятьсот девяносто первого'
    assert res1.getYear(2000) == 'двухтысячного'
    assert res1.getYear(34) == 'тридцать четвёртого'
    assert res1.getYear(600) == 'шестисотого'
    assert res1.getYear(555) == 'пятьсот пятьдесят пятого'
    assert res1.getYear(0) == 'нулевого'
    assert res1.getYear(10) == 'десятого'
    assert res1.getYear(977) == 'девятьсот семьдесят седьмого'
    assert res1.getYear(2019) == 'две тысячи девятнадцатого'
    assert res1.getYear(1918) == 'одна тысяча девятьсот восемнадцатого'
    assert res1.getTimeNumber(19, 'mus') == 'девятнадцать'
    assert res1.getTimeNumber(40, 'fem') == 'сорок'
    assert res1.getTimeNumber(21, 'fem') == 'двадцать одна'
    assert res1.getTimeNumber(21, 'mus') == 'двадцать один'
    assert res1.getTimeNumber(2, 'mus') == 'ноль два'
    assert res1.getTimeNumber(2, 'fem') == 'ноль две'
    assert res1.getTimeNumber(57, 'fem') == 'пятьдесят семь'
    assert res1.convert() == "двадцать пятое сентября две тысячи девятнадцатого года ноль восемь часов семнадцать минут пятьдесят девять секунд"
    res2 = DateToTextClass('03.11.1812 21:00:00')
    assert res2.convert() == 'третье ноября одна тысяча восемьсот двенадцатого года двадцать один час ноль минут ноль секунд'
    res3 = DateToTextClass('14.06.0000 00:00:00')
    assert res3.convert() == 'четырнадцатое июня нулевого года ноль часов ноль минут ноль секунд'
    res4 = DateToTextClass('30.01.0045 18:19:20')
    assert res4.convert() == 'тридцатое января сорок пятого года восемнадцать часов девятнадцать минут двадцать секунд'
    res5 = DateToTextClass('30.02.0001 03:02:01')
    assert res5.convert() == 'тридцатое февраля первого года ноль три часа ноль две минуты ноль одна секунда'
    res6 = DateToTextClass('30.02.0010 15:21:50')
    assert res6.convert() == 'тридцатое февраля десятого года пятнадцать часов двадцать одна минута пятьдесят секунд'
    res7 = DateToTextClass('31.02.0015 09:11:40')
    assert res7.convert() == 'тридцать первое февраля пятнадцатого года ноль девять часов одиннадцать минут сорок секунд'
    res8 = DateToTextClass('31.03.0400 23:23:23')
    assert res8.convert() == 'тридцать первое марта четырёхсотого года двадцать три часа двадцать три минуты двадцать три секунды'
    res9 = DateToTextClass('08.03.0498 12:01:38')
    assert res9.convert() == 'восьмое марта четыреста девяносто восьмого года двенадцать часов ноль одна минута тридцать восемь секунд'
    res10 = DateToTextClass('17.01.9999 11:10:36')
    assert res10.convert() == 'семнадцатое января девять тысяч девятьсот девяносто девятого года одиннадцать часов десять минут тридцать шесть секунд'
