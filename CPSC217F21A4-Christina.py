# Christina He
# UCID: 30168171
# Program description:
# This program will analyze fictional contact tracing data by taking in records of contact from individuals
# who tested positive.
# Bonus part is included


import sys
from formatList import *
import os


# Check if the file exist
def isValidFile(file):
    return os.path.exists(file)


# open, read and close file
# returns content in a long list
def processFile():
    # check if there are correct number of arguments and check if the file is a valid one
    if len(sys.argv) > 2:
        exit("Please enter one file only!")
    elif len(sys.argv) < 2:
        file = input("Please enter a file name: ")
    else:
        file = sys.argv[1]

    if not isValidFile(file):
        print(f"{file} does not exist!")
        exit()

    # open, read and close file
    # returns the content inside file
    try:
        inputFile = open(file, "r")
        content = inputFile.readlines()
        return content
    except Exception as error:
        exit(error)
    finally:
        inputFile.close()



# Takes the content of the file in the long list and turn it into a dictionary
# returns the content in form of dictionary
def storeInDic(content):
    dictionary = {}
    positive = []
    sortedDictionary = {}

    # reformat the long list and store people tested positive as keys and contacts as values in dictionary
    for elements in content:
        reformat = elements.rstrip("\n")
        reformat = reformat.split(",")[::]
        key = reformat[0]
        reformat = reformat[1:]
        positive.append(key)
        reformat.sort()
        dictionary[key] = reformat

    positive.sort()
    for names in positive:
        sortedDictionary[names] = dictionary[names]

    return sortedDictionary


# Takes content in a long list and group each line in the content into smaller lists
# returns the reformatted list
def storeInList(content):
    list = []
    for elements in content:
        reformat = elements.rstrip("\n")
        reformat = reformat.split(",")[::]
        subList = []
        for items in reformat:
            subList.append(items)
        list.append(subList)
    return list


# Check who did not have contact with other people tested positive and returns their names
# parameter list is a list containing smaller list of people tested positive and their contacts
def patientZero(list):
    all = []
    positive = []
    patientZero = []

    for elements in list:
        all.extend(elements)
        positive.append(elements[0])

    for items in positive:
        if all.count(items) == 1:
            patientZero.append(items)

    patientZero.sort()
    return patientZero


# List and returns people might be infected but haven't appear sick
# parameter list is a list containing smaller list of people tested positive and their contacts
def potentialZombie(list):
    all = []
    positive = []
    potentialZombie = []
    for elements in list:
        all.extend(elements)
        positive.append(elements[0])

    for people in all:
        if people not in positive:
            if people not in potentialZombie:
                potentialZombie.append(people)

    potentialZombie.sort()
    return potentialZombie


# Return a list of people that are not the source of zombie virus but appeared sick
# first parameter list is a list containing smaller list of people tested positive and their contacts
# second parameter patientZero is a list of people who are the source of zombie virus
# third parameter potentialZombie is a list of people who had contact with sick people and does not appear sick
def others(list, patientZero, potentialZombie):
    all = []
    others = []

    for elements in list:
        all.extend(elements)

    for people in all:
        if people not in patientZero:
            if people not in potentialZombie:
                if people not in others:
                    others.append(people)

    others.sort()
    return others

# returns the list of people who had infected most people
# parameter list is a list containing smaller list of people tested positive and their contacts
def mostViral(list):
    # initialization
    viralIndex = [0]
    mostViral = []

    # loop through each one to see which sick people had the most contacts, add them to the list
    for index in range(len(list)):
        if len(list[index]) > len(list[viralIndex[0]]):
            viralIndex = [index]
        elif len(list[index]) == len(list[viralIndex[0]]):
            if index not in viralIndex:
                viralIndex.append(index)

    for indexes in viralIndex:
        mostViral.append(list[indexes][0])

    mostViral.sort()
    return mostViral


# returns a list of people who has possible been
# infected by the most different members of the data set
# parameter list is a list containing smaller list of people tested positive and their contacts
def tastiest(list):
    # initialization
    all = []
    tastiest = []
    remove = []
    temp = {}
    track = 0

    for elements in list:
        all.extend(elements)

    # count and store how many times the person appeared in the list
    for people in all:
        if people not in temp:
            count = all.count(people)
            temp[people] = count
        if people in potentialZombie(list):
            temp[people]+=1

    # Add people who contacted with most people to a list
    for keys in temp:
        if temp[keys] >= track:
            track = temp[keys]
            tastiest.append(keys)

    for name in tastiest:
        if temp[name] < track:
            remove.append(name)

    for items in remove:
        tastiest.remove(items)

    tastiest.sort()
    return tastiest



# I tried to do this part with recursion, it works fine with DataSet1.txt but not the others
# I might come back and see if I can fix this
# def findHeight(list,dictionary, name, res={},state={},count = 0):
#     # Creating a list containing all numbers
#     all = []
#     all.extend(patientZero(list))
#     all.extend(others(list,patientZero(list),potentialZombie(list)))
#     all.extend(potentialZombie(list))
#
#     # initial setup
#     # v = visited, n = not visited, e = exploring now
#     if res == state == {}:
#         state = {}
#         res = {}
#         for names in all:
#             state[names] = 'n'
#             res[names] = -1
#
#         # for people in potentialZombie(list):
#         #     dictionary[people] = []
#
#     state[name] = 'e'
#     for people in all:
#         if state[people] == 'n':
#             count = 0
#             name = people
#
#         if name not in dictionary:
#             res[name] = 0
#             return 0
#
#         for contacts in dictionary[name]:
#             if state[contacts] == 'n':
#                 state[contacts] = 'v'
#                 if res[contacts] < count:
#                     res[contacts] = count
#                 findHeight(list,dictionary,contacts,res,state,count=count+1)
#
#             if res[name] <= res[contacts]:
#                 res[name] = res[contacts] + 1
#
#     return res

# Find and returns distance from people who have not infected in a dictionary
# parameter list is a list containing smaller list of people tested positive and their contacts

def findHeights(list):
    # creating a list containing all people
    all = []
    all.extend(patientZero(list))
    all.extend(others(list,patientZero(list),potentialZombie(list)))
    all.extend(potentialZombie(list))

    # initial setups
    height = {}
    dictionary = {}
    highest = 0
    for items in list:
        dictionary[items[0]] = items[1:]

    for peopleNotInDictionary in potentialZombie(list):
        dictionary[peopleNotInDictionary] = []

    for people in all:
        height[people] = 0

    # change heights until everybody has one more distance from their contacts
    changed = True
    while changed:
        changed = False
        for p1 in all:
            for p2 in dictionary[p1]:
                if height[p1] <= height[p2]:
                    height[p1] = height[p2] +1
                    if highest < height[p1]:
                        highest = height[p1]
                    changed = True

    final = []
    for x in range(highest+1):
        name = [key for key in height if height[key] is highest]
        name.sort()
        final.append(name)
        highest -= 1

    return final

# List and return sick people who only contacted with people who has no symptoms
# parameter list is a list containing smaller list of people tested positive and their contacts
# parameter dictionary is a dictionary containing sick people and their contacts
def spreaderZombie(list,dictionary):
    sickperson = []
    potentialZ = potentialZombie(list)

# create a shallow list of sick people, remove any people who showed contacts besides the ones not showing symptoms
    for keys in dictionary:
        sickperson.append(keys)
        for contacts in dictionary[keys]:
            if keys in sickperson:
                if contacts not in potentialZ:
                    sickperson.remove(keys)

    return sickperson


# List and return people who had contacted with sick people and people with no symptoms
# parameter list is a list containing smaller list of people tested positive and their contacts
# parameter dictionary is a dictionary containing sick people and their contacts
def regularZombies(list,dictionary):
    sickperson = []
    potentialZ = potentialZombie(list)
    regularZombies = []

    for keys in dictionary:
        sickperson.append(keys)

    for keys in dictionary:
        cond1 = False
        cond2 = False
        for contacts in dictionary[keys]:
            if contacts in sickperson:
                cond1 = True
            if contacts in potentialZ:
                cond2 = True

        if cond1 and cond2:
            regularZombies.append(keys)

    return regularZombies


# list and returns sick people who only contacted with sick people
# parameter list is a list containing smaller list of people tested positive and their contacts
# parameter dictionary is a dictionary containing sick people and their contacts
def zombiePredators(list,dictionary):
    sickperson = []
    zombiePredators = []
    zombiePredators.extend(patientZero(list))
    zombiePredators.extend(others(list,patientZero(list),potentialZombie(list)))
    # zombiePredators.extend(potentialZombie(list))

    for keys in dictionary:
        sickperson.append(keys)

    for keys in dictionary:
        for contacts in dictionary[keys]:
            if contacts not in sickperson:
                zombiePredators.remove(keys)
    zombiePredators.sort()
    return zombiePredators


# Executing function calls and print out the final result
def main():
    # open and process file
    content = processFile()

    # create list and dictionary
    list = storeInList(content)
    dictionary = storeInDic(content)

    # List contact in an organized format
    print('Contact records:')
    for keys in dictionary:
        lineContact = formatList(dictionary[keys])
        print(f"  {keys} had contact with {lineContact}")

    print('\n',end = '')

    # List possible sources of zombie virus
    print("Patient Zero(s): " + formatList(patientZero(list)))

    # List people who might have been infected
    print("Potential Zombies: " + formatList(potentialZombie(list)))

    # list people who are not possible sources of zombie virus and had got sick
    print("Neither Patient Zero or Potential Zombie: " + formatList(others(list,patientZero(list),potentialZombie(list))))

    # list most powerful source of zombie virus
    print("Most viral people: " + formatList(mostViral(list)))

    # list people have been infected by most people
    print("Tastiest: " + formatList(tastiest(list)))

    print('\n',end = '')

    # list each person's distance from people showing no symptoms
    print("Heights:")
    height = findHeights(list)
    highest = len(height) - 1
    for items in height:
        for elements in items:
            print(f'  {elements}: {highest}')
        highest -= 1

    print('\n',end = '')
    print('For an A+ : ')
    # list people who only contacted with people not showing symptoms
    print('  Spreader zombies:',formatList(spreaderZombie(list,dictionary)))

    # list people who contacted with people got sick and people not showing symptoms
    print('  Regular zombies:', formatList(regularZombies(list,dictionary)))

    # list people who only contacted with sick people
    print('  Zombie predators:',formatList(zombiePredators(list,dictionary)))


# call main function
main()
