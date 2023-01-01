# Function to convert a base 10 integer to any base b less than or equal to 10
# Defaults to binary if a base is not specified
def convert(n, b=2):

    if n == 0:
        return 0
    
    if b > 10:
      return 'Invalid base'

    current = n
    converted_num = []

    while current != 0:
        converted_num.append(str(current % b))
        current = current // b

    converted_num.reverse()
    return ''.join(converted_num)

  
# Function to convert a base 10 integer to hexadecimal  
def convert_to_hex(n):
    if n == 0:
        return 0
    
    hexes = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}

    current = n
    converted_num = []

    while current != 0:
        new_num = current % 16
        if new_num >= 10:
            new_num = hexes[new_num]
        converted_num.append(str(new_num))
        current = current // 16

    converted_num.reverse()
    return ''.join(converted_num)
