# Question 4 - Use the next() function to find the first element in a list of dictionaries 
# whose attribute ‘x’ = 5. Default to an empty dictionary if not found.
def get_first_element(dic_elements, criteria_key, criteria_value):
    
    dic_elements_qx = len(dic_elements)
    iter_dic_elements = iter(dic_elements)

    for i in range(dic_elements_qx):
        # next() function
        found_element = next(iter_dic_elements, None) 
        if found_element == None:
            return {}
        else:
            if criteria_key in found_element and found_element[criteria_key] == criteria_value:
                return found_element
    else:
        return {}

#Test 1 > Existing dic element
dic_elements = [{'x': 1, 'y': 5, 'z': 2}, {'x': 10, 'y': 14, 'z': 1}, {'x': 5, 'y': 1, 'z': 2}, {'x': 8, 'y': 10, 'z': 3}]
print (get_first_element(dic_elements, 'x', 5))

#Test 2 > Existing dic element (with some empty dic)
dic_elements = [{'x': 1, 'y': 5, 'z': 2}, {}, {'x': 5, 'y': 1, 'z': 2}, {'x': 8, 'y': 10, 'z': 3}]
print (get_first_element(dic_elements, 'x', 5))

#Test 3 > Not existing dic element
dic_elements = [{'x': 1, 'y': 5, 'z': 2}, {'x': 10, 'y': 14, 'z': 1}, {'x': 25, 'y': 1, 'z': 2}]
print (get_first_element(dic_elements, 'x', 5))

#Test 4 > Not dic elements
dic_elements = []
print (get_first_element(dic_elements, 'x', 5))

#Test 5 > Not dic elements with key filter criteria x
dic_elements = [{'w': 1, 'y': 5, 'z': 2}, {'w': 10, 'y': 14, 'z': 1}, {'w': 25, 'y': 1, 'z': 2}]
print (get_first_element(dic_elements, 'x', 5))
