#Your optional code here
#You can import some modules or create additional functions


def checkio(data: list) -> list:
    temp_dict = {}
    for i,item in enumerate(data):
        print("iter:",i)
        if item  not in temp_dict:
            print("added number ",item,"to dict")
            temp_dict[item] = 1
        else:
            print("increased count of number ",item," in dict")
            temp_dict[item] = temp_dict[item] + 1
    for key,val in temp_dict.items():
        #check if value(count) of number is 1 then remove this unique element from our list
        if val == 1:
            data.remove(key)
    return data

#Some hints
#You can use list.count(element) method for counting.
#Create new list with non-unique elements
#Loop over original list


if __name__ == "__main__":
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert list(checkio([1, 2, 3, 1, 3])) == [1, 3, 1, 3], "1st example"
    assert list(checkio([1, 2, 3, 4, 5])) == [], "2nd example"
    assert list(checkio([5, 5, 5, 5, 5])) == [5, 5, 5, 5, 5], "3rd example"
    assert list(checkio([10, 9, 10, 10, 9, 8])) == [10, 9, 10, 10, 9], "4th example"
    print("It is all good. Let's check it now")
