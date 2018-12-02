def main():


    ISBN = int(input('Please enter a 10 or 13 digit number: ')) 

    while len(str(ISBN))!=10:

        print('Error: Please make sure your number is 10 digits long')

        ISBN = int(input('Please enter a 10 digit number: '))


        

    






def compact(number, convert=False):

## Convert the ISBN to the minimal representation.

    number = clean(number, ' -').strip().upper()

    if len(number) == 9:

      number = '0' + number

    if convert:

      return to_isbn13(number)

    return number

 

 

def calc_isbn10_check_digit(number):

    ## Calculate the ISBN check digit for 10-digit numbers.

    check = sum((i + 1) * int(n)

        for i, n in enumerate(number)) % 11

    return 'X' if check == 10 else str(check)


def calc_isbn13_check_digit(number):

    check = sum((i + 1) * int(n)

        for i, n in enumerate(number)) % 14

    return 'X' if check == 13 else str(check)

 

 

def validate(number, convert=False):

## Checks to see if the number provided is a valid ISBN (either a legacy

## 10-digit number or a 13-digit number). 

    number = compact(number, convert=False)

    if not number[:-1].isdigit():

        raise InvalidFormat()

    if len(number) == 10:

        if calc_isbn10_check_digit(number[:-1]) != number[-1]:

            raise InvalidChecksum()

    elif len(number) == 13:

        ean.validate(number)

    else:

        raise InvalidLength()

    if convert:

      number = to_isbn13(number)

      return number



 

 

def isbn_type(number):

## Check the passed number and return 'ISBN13', 'ISBN10' or None (for

## invalid) for checking the type of number passed

  try:

    number = validate(number, convert=False)

  except ValidationError:

      return None

  if len(number) == 10:

      return 'ISBN10'

  else: # len(number) == 13:

    return 'ISBN13'



 

def to_isbn13(number):

## Convert the number to ISBN-13 format.

  number = number.strip()

  min_number = compact(number, convert=False)

  if len(min_number) == 13:

    return number # nothing to do, already ISBN-13

  number = number[:-1] + ean.calc_check_digit('978' + min_number[:-1])

  # add prefix

  if ' ' in number:

    return '978 ' + number

  elif '-' in number:

    return '978-' + number

  else:

    return '978' + number

 

 

def to_isbn10(number):

## Convert the number to ISBN-10 format.

  number = number.strip()

  min_number = compact(number, convert=False)

  if len(min_number) == 10:

    return number # nothing to do, already ISBN-10

  elif isbn_type(min_number) != 'ISBN13':

     raise InvalidFormat('Not a valid ISBN13.')

  elif not number.startswith('978'):

      raise InvalidFormat('Does not use 978 Bookland prefix.')

  # strip EAN prefix

  number = number[3:-1].strip().strip('-')

  digit = _calc_isbn10_check_digit(min_number[3:-1])

  # append the new check digit

  if ' ' in number:

    return number + ' ' + digit

  elif '-' in number:

    return number + '-' + digit

  else:

    return number + digit



def split(number, convert=False):

## Split the specified ISBN into an EAN.UCC prefix, a group prefix, a

## registrant, an item number and a check-digit. 

  from stdnum import numdb

  # clean up number

  number = compact(number, convert)

  # get prefix if any

  delprefix = False

  if len(number) == 10:

    number = '978' + number

    delprefix = True

  # split the number

  result = numdb.get('isbn').split(number[:-1])

  itemnr = result.pop() if result else ''

  prefix = result.pop(0) if result else ''

  group = result.pop(0) if result else ''

  publisher = result.pop(0) if result else ''

  # return results

  return ('' if delprefix else prefix, group, publisher, itemnr, number[-1])

 

def format(number, separator='-', convert=False):

  return separator.join(x for x in split(number, convert) if x)


num=True
while num:
    print ("""
    1.Verify the check digit of an ISBN-10
    2.Verify the check digit of an ISBN-13
    3.Convert an ISBN-10 to an ISBN-13
    4.Convert an ISBN-13 to an ISBN-10
    5.Exit
    """)
    num=input("What would you like to do?") 
    if num=="1": 
      print("\n ISBN-10 check") 
    elif num=="2":
      print("\n ISBN-13 check") 
    elif num=="3":
      print("\n ISBN-10 convert") 
    elif num=="4":
      print("\n ISBN-13 convert")
    elif num=="5":
      print("\n Goodbye")
      break
    elif num!="":
      print("\n Not Valid Choice Try again") 

main()
