'''
Write a python program to generate the ticket numbers for specified number of passengers traveling in a flight as per the details mentioned below:
The ticket number should be generated as airline:src:dest:number
where

    Consider AI as the value for airline
    src and dest should be the first three characters of the source and destination cities.
    number should be auto-generated starting from 101

The program should return the list of ticket numbers of last five passengers.
Note: If passenger count is less than 5, return the list of all generated ticket numbers.

'''


def generate_ticket(airline, source, destination, no_of_passangers):
    ticket_number_list = []

    i = 0
    if no_of_passangers < 5:
        while no_of_passangers != 0:
            ticket_number_list.append(
                f"{airline}:{source[:3]}:{destination[:3]}:{101 + i}")
            i = i + 1
            no_of_passangers = no_of_passangers - 1
    else:
        for i in range(5):
            ticket_number_list.append(
                f"{airline}:{source[:3]}:{destination[:3]}:{100 + no_of_passangers}")
            i = i + 1
            no_of_passangers = no_of_passangers - 1

        ticket_number_list = ticket_number_list[::-1]

    return ticket_number_list


print(generate_ticket("AI", "Bangalore", "London", 7))
