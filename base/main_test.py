from read_json import Read_JSON_Dictionary
from pathlib import Path
from pprint import pprint
import json
import os

'''create main function'''
def main():
            
    # Create directory
    dirName = 'jsons'
    try:
        # Create target Directory
        os.mkdir(dirName)
        print("Directory " , dirName ,  " Created ") 
    except FileExistsError:
        print("Directory " , dirName ,  " already exists")


    gh1_file = 'gh1'
    gh2_file = 'gh2'
    gh3_file = 'gh3'
    gh4_file = 'gh4'
    gh5_file = 'gh5'
    gh6_file = 'gh6'
    gh7_file = 'gh7'

    '''write JSON from a dictionary'''
    gh1_dict = {'gh1_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh1_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh1_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh1_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh2_dict = {'gh2_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh2_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh2_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh2_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh3_dict = {'gh3_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh3_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh3_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh3_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh4_dict = {'gh4_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh4_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh4_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh4_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh5_dict = {'gh5_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh5_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh5_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh5_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh6_dict = {'gh6_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh6_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh6_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh6_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    gh7_dict = {'gh7_devices': [('actuator',3),('Controller', 4),('Pump',5),('Sensor',3),('Relay',2),('Value',2),('Waterhose',2)],
    'gh7_vegetables': [('aspargus', 12), ('broccoli', 5), ('carrots', 15), ('celery', 9), ('leeks', 8), ('onions', 6), ('potatoes', 11)],
    'gh7_fruits': [('apples', 12), ('cherries', 5), ('pears', 15), ('plums', 9), ('raspberries', 8), ('strawberries', 6), ('tomatoes', 11)],
    'gh7_herbs': [('basil', 12), ('chives', 5), ('coriander', 15), ('dill', 9), ('mint', 8), ('oregano', 6), ('parsley', 11)]}

    vegetable_list = ['asparagus', 'broccoli', 'carrots', 'celery', 'lettuce', 'leeks', 'onions', 'potatoes']
    fruit_list = ['apples', 'cherries', 'grapes', 'oranges', 'pears', 'peaches', 'plums', 'tomatoes']
    herb_list = ['basil', 'chives', 'cilantro', 'dill', 'mint', 'oregano', 'parsley', 'rosemary', 'sage', 'thyme']
    
    '''try to write JSON to file'''
    '''from the Read_JSON_Dictionary class'''    
    gh1_path = 'jsons\\' + str(gh1_file) + '.json'
    gh2_path = 'jsons\\' + str(gh2_file) + '.json'   
    gh3_path = 'jsons\\' + str(gh3_file) + '.json'
    gh4_path = 'jsons\\' + str(gh4_file) + '.json'
    gh5_path = 'jsons\\' + str(gh5_file) + '.json'
    gh6_path = 'jsons\\' + str(gh6_file) + '.json'
    gh7_path = 'jsons\\' + str(gh7_file) + '.json'

    '''rj1 = Read_JSON_Dictionary(temp_string, temp_dictionary)'''
    gh1 = Path(gh1_path)  
    if not gh1.exists():
        print(gh1_path)
        f1 = open(gh1_path, 'x')
        f1.close()
    if gh1.exists():
        print(gh1_path)
        rj = Read_JSON_Dictionary(gh1_path, gh1_dict)
        rj.write_JSON_dictionary()
    print(gh1_dict)

    gh2 = Path(gh1_path)  
    if not gh2.exists():
        print(gh2_path)
        f1 = open(gh2_path, 'x')
        f1.close()
    if gh1.exists():
        print(gh2_path)
        rj = Read_JSON_Dictionary(gh2_path, gh2_dict)
        rj.write_JSON_dictionary()


    gh3 = Path(gh3_path)
    if not gh3.exists():
        print(gh3_path)
        f1 = open(gh3_path, 'x')
        f1.close()
    if gh3.exists():
        print(gh3_path)
        rj = Read_JSON_Dictionary(gh3_path, gh3_dict)
        rj.write_JSON_dictionary()

    gh4 = Path(gh4_path)
    if not gh4.exists():
        print(gh4_path)
        f1 = open(gh4_path, 'x')
        f1.close()
    if gh4.exists():
        print(gh4_path)
        rj = Read_JSON_Dictionary(gh4_path, gh4_dict)
        rj.write_JSON_dictionary()

    gh5 = Path(gh5_path)
    if not gh5.exists():
        print(gh5_path)
        f1 = open(gh5_path, 'x')
        f1.close()
    if gh5.exists():
        print(gh5_path)
        rj = Read_JSON_Dictionary(gh5_path, gh5_dict)
        rj.write_JSON_dictionary()

    gh6 = Path(gh6_path)
    if not gh6.exists():
        print(gh6_path)
        f1 = open(gh6_path, 'x')
        f1.close()
    if gh6.exists():
        print(gh6_path)
        rj = Read_JSON_Dictionary(gh6_path, gh6_dict)
        rj.write_JSON_dictionary()

    gh7 = Path(gh7_path)
    if not gh7.exists():
        print(gh7_path)
        f1 = open(gh7_path, 'x')
        f1.close()
    if gh7.exists():
        print(gh7_path)
        rj = Read_JSON_Dictionary(gh7_path, gh7_dict)
        rj.write_JSON_dictionary()

    my_dict = {}
    if not gh7.exists():
        print(gh7_path)
        f1 = open(gh7_path, 'r')
        f1.close()
    if gh7.exists():
        print(gh7_path)
        f1 = open(gh7_path, 'r') 
        my_dict = json.loads(f1.read())    
        f1.close()  

    print()
    input("Press Enter to continue...")   

    print()
    print("This is my dictionary:")
    pprint(my_dict)
        
'''initialize __name__ == '__main__'''
if __name__ == '__main__':
    main()



