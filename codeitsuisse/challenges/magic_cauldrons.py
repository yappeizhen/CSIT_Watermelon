input = [
  {
    "part1": {
      "flow_rate": 20,
      "time": 1,
      "row_number": 0,
      "col_number": 0
    },
    "part2": {
      "flow_rate": 10,
      "amount_of_soup": 10.00,
      "row_number": 0,
      "col_number": 0
    },
    "part3": {
      "flow_rate": 30,
      "time": 2,
      "row_number": 0,
      "col_number": 0
    },
    "part4": {
      "flow_rate": 50,
      "amount_of_soup": 100.00,
      "row_number": 0,
      "col_number": 0
    }
  },
  {
    "part1": {
      "flow_rate": 23,
      "time": 1,
      "row_number": 0,
      "col_number": 0
    },
    "part2": {
      "flow_rate": 17,
      "amount_of_soup": 34.00,
      "row_number": 0,
      "col_number": 0
    },
    "part3": {
      "flow_rate": 36,
      "time": 1,
      "row_number": 0,
      "col_number": 0
    },
    "part4": {
      "flow_rate": 5,
      "amount_of_soup": 20.00,
      "row_number": 0,
      "col_number": 0
    }
  }
]

def part_1(input: list):
    flow_rate = input['flow_rate']
    time = input['time']
    row_number = input['row_number']
    col_number = input['col_number']
    
    # total number of cauldrons poured (each cauldron contains max 100g)
    poured = flow_rate * time

    # Initialize cauldron tower array
    tower = [[0] * k for k in range(1, 102)]
    
    # Initialize first glass total flow = total number of cauldrons poured.
    tower[0][0] = poured
    if poured <= 100:
        return round(tower[row_number][col_number],2)
    for r in range(row_number + 1):
        for c in range(r+1):
            # equal overflow amount to left and right of cauldron (r,c)
            overflow = (tower[r][c] - 100) / 2.0
            # this overflow goes into cauldron (r+1,c) and (r+1,c+1)
            if overflow > 0:
                    tower[r+1][c] += overflow
                    tower[r+1][c+1] += overflow

    return min(100, round(tower[row_number][col_number],2))
    

print(part_1(input[0]['part1']))
print(part_1(input[1]['part1']))


def part_2(input: list):
    flow_rate = input['flow_rate']
    amount_of_soup = input['amount_of_soup']
    row_number = input['row_number']
    col_number = input['col_number']

    #           1
    #         1   1
    #       1   2   1
    #     1   3   3   1
    #
    # amount of overflow from sum of glass (r-1,c) and (r-1,c+1) = r(r,c)
    # find total poured volume, obtain time = poured/flow_rate
    # Initialize cauldron tower array
    tower = [[0] * k for k in range(1, 102)]
    
    # Initialize first glass total flow = total number of cauldrons poured.
    #tower[0][0] = 



    #time = amount_of_soup / (flow_rate/100)
    #for r in range(row_number,0,-1):
        #print(r)
        # amount of 
        #for c in range(r+1):


    #return time
    return poured/flow_rate

#print(part_2(input[0]['part2']))

#print(part_2(input[1]['part2']))





def part_3(input: list):
    flow_rate = input['flow_rate']
    time = input['time']
    row_number = input['row_number']
    col_number = input['col_number']
    
    # total number of cauldrons poured (each cauldron contains max 100g)
    poured = flow_rate * time

    # Initialize cauldron tower array
    tower = [[0] * k for k in range(1, 102)]
    
    # Initialize first glass total flow = total number of cauldrons poured.
    tower[0][0] = poured
    if poured <= 150:
        return round(tower[row_number][col_number],2)
    for r in range(row_number + 1):
        for c in range(r+1):
            if c % 2 == 0:
                capacity = 150
            else:
                capacity = 100
            # equal overflow amount to left and right of cauldron (r,c)
            overflow = (tower[r][c] - capacity) / 2.0
            # this overflow goes into cauldron (r+1,c) and (r+1,c+1)
            if overflow > 0:
                    tower[r+1][c] += overflow
                    tower[r+1][c+1] += overflow

    if col_number % 2  == 0:
        capacity = 150
    else:
        capacity = 100

    return min(capacity, round(tower[row_number][col_number],2))
    
print(part_3(input[0]['part3']))
print(part_3(input[1]['part3']))


def part_4(input: list):
    flow_rate = input['flow_rate']
    amount_of_soup = input['amount_of_soup']
    row_number = input['row_number']
    col_number = input['col_number']

    return 0


def magic_cauldrons(input_dict: dict):
    result = {}
    result["part1"] = part_1(input_dict["part1"])
    result["part2"] = part_2(input_dict["part2"])
    result["part3"] = part_3(input_dict["part3"])
    result["part4"] = part_4(input_dict["part4"])
    return result


print(magic_cauldrons(input[0]))