#!/usr/bin/env python3

def create_list():
    '''
    the function creating a list from all the inputs from the user
    :return: a list from the user till the input is an empty list.
    if the first input is empty string as input the functions will return an empty list
    '''
    new_list = []  # the new list that gets inputs
    adding_to_list = input()  # the input of the user
    while len(adding_to_list) != 0:  # if the input is not an empty string
        new_list.append(adding_to_list)  # add the input to the list
        adding_to_list = input()
    return new_list
    pass


def concat_list(str_list):
    '''
    the function converting the list objects into one string
    :param str_list:
    :return: a concatenation of the list objects a string
    '''
    length_of_input_string = len(str_list)
    converted_list_to_string = ''  # the new string that will contain the list values
    for i in range(0, length_of_input_string):
        converted_list_to_string += str_list[i]  # adding the objects list to the string
    return converted_list_to_string
    pass


def average(num_list):
    '''
    the function calculate the average of the numbers in the list
    :param num_list: list of numbers, may be empty. if there are values they are from type int or float
    :return: return None if the list is empty or the average of the list
    '''
    if len(num_list) == 0:  # checking if the list is empty
        return None
    else:
        count_of_numbers = len(num_list)  # how many numbers there are in the list
        sum_of_list_numbers = 0
        for counting in range(0,count_of_numbers):
            sum_of_list_numbers += num_list[counting]  # summing up all the numbers in the list
        average_list = sum_of_list_numbers/count_of_numbers  # c alculating the average
        return average_list
    pass


def cyclic(lst1,lst2):
    '''
    the function determinate if 2 lists are cyclic permutations to each other
    :param lst1: the list with objects, may be empty
    :param lst2:the list with objects, may be empty
    :return:True if the 2 lists are cyclic permutations to each other, else False
    '''
    length_of_lst1 = len(lst1)
    length_of_lst2 = len(lst2)

    if lst1 == lst2:  # checking if the 2 lists are already equal as they are
        return True

    elif length_of_lst1 == 0 and length_of_lst2 == 0:  # checking if the lists are empty
        return True

    elif length_of_lst1 != length_of_lst2:  # if the length of the 2 lists are not the same
        return False

    else:
        cyc_list_1 = []
        for time_of_cycling in range(0, length_of_lst1):
            cyc_list_1.append(lst1[time_of_cycling])

        for i in range(0, length_of_lst1):
            last_element = cyc_list_1[(length_of_lst1-1)]
            cyc_list_1.insert(0,last_element)
            cyc_list_1.pop()
            if cyc_list_1 == lst2:
                return True

        return False
    pass


def histogram(n,num_list):
    '''
    the function calculate a histogram of a given list of numbers
    :param n: positive int number
    :param num_list: list of objects from type int. may be empty
    :return: list a histogram of values in num_list
    '''
    new_list = []
    for i in range(0, n):
        new_list.append(0)

    for i in range(0, len(num_list)):
        new_list[num_list[i]] = int(new_list[num_list[i]]) + 1
    return new_list
    pass


def is_prime_number(number):
    '''
    the function checks if the number is a prime number
    :param number: int positive number, bigger than 1.
    :return: True if the number is a prime number else False, if the number is 0 is not a prime number and
    '''

    if number == 2:
        is_a_prime_number = True
    if number > 2:
        for i in range(2, number):
            if number % i == 0:  # if the number is divided with the index
                is_a_prime_number = False  # if the number is not a prime number
                break
            else:
                is_a_prime_number = True  # if the number is a prime number

    return is_a_prime_number
    pass


def prime_factors(n):
    '''
    The function calculates the decomposition into the first factors of the number we received
    :param n:a positive number equal or bigger than 1
    :return: return empty list if the number is 1,
    if the number is a prime number - the function return a list only with the prime number
    else return a list with all the prime numbers that divided by n
    '''
    list_of_prime_factors = []

    if n <= 1:  # if the input is smaller or equal to 1.
        return []

    elif is_prime_number(n) is True:
        list_of_prime_factors.append(n)
        return list_of_prime_factors

    else:
        divider = 2
        while n > 2:
            if is_prime_number(divider) is True:
                if n % divider == 0:
                    list_of_prime_factors.append(divider)
                    n = int(n/divider)
                    divider = 1
                    if is_prime_number(n) is True:  # checking if n now is a prime number
                        list_of_prime_factors.append(n)
                        break
            divider += 1
        return list_of_prime_factors
    pass


def cartesian(lst1, lst2):
    '''
    the functions makes all the cartesian product of the 2 lists together
    :param lst1: list  of objects
    :param lst2: list  of objects
    :return: if one of the lists is empty - will be return empty list, else will return list of all the cartesian\
    product where the first object is from the 1st list and the second of objects is from the 2nd list
    '''
    list1_length = len(lst1)
    list2_length = len(lst2)
    list_cartesian = []
    if list1_length == 0 or list2_length == 0:
        return []

    else:
            for place_in_lst1 in range(0, list1_length):
                for place_in_lst2 in range(0, list2_length):
                    new_list = []
                    new_list.append(lst1[place_in_lst1])
                    new_list.append(lst2[place_in_lst2])
                    list_cartesian.append(new_list)
            return list_cartesian
    pass


def pairs(n, num_list):
    '''
    the function making a list of all th couples of numbers that their sum is equal to number n
    :param n:a number
    :param num_list: list of numbers
    :return: a list of couples of numbers, from the num_list, that their sum is equal to number n
    '''
    result = []  # the final list with all the possible couples
    if len(num_list) == 0 or len(num_list) == 1:
        return []
    else:
        for i in range(0, len(num_list)):
            for j in range(i, len(num_list)):
                if n == num_list[j]+num_list[i]:
                    list_new = max(num_list[j], num_list[i]),min(num_list[j], num_list[i])  # a list of the couple of
                    # numbers that their sum equal to n
                    if list_new not in result:  # checking if the new list already exists
                        result.append(list_new)
    return result
    pass
