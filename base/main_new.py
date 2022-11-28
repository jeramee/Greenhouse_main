from read_json import Read_JSON_Dictionary
import json
from pathlib import Path
from pprint import pprint
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

    devices = [
    {
        'id': 1,
        'name': 'Actuator',
        'description': 'Actuator is a device that is used to move or control a mechanism or system, especially by means of levers, pulleys, or gears.',
        'image': 'https://en.wikipedia.org/wiki/Actuator#/media/File:Pneumatic_Rack_and_Pinion_Actuators.JPG',
    },

    {
        'id': 2,
        'name': 'Sensor',
        'description': 'Sensor is a device, module, machine, or subsystem whose purpose is to detect events or changes in its environment and send the information to other electronics, frequently a computer processor.',
        'image': 'https://en.wikipedia.org/wiki/Sensor#/media/File:Sensor.jpg',
    },

    {
        'id': 3,
        'name': 'Controller',
        'description': 'A microcontroller is a small computer on a single integrated circuit containing a processor core, memory, and programmable input/output peripherals.',
        'image': 'https://en.wikipedia.org/wiki/Microcontroller#/media/File:Arduino_Uno_-_R3.jpg',
    },

    {
        'id': 4,
        'name': 'Pump',
        'description': 'A pump is a device that moves fluids (liquids or gases), or sometimes slurries, by mechanical action.',
        'image': 'https://en.wikipedia.org/wiki/Pump#/media/File:Water_pump.jpg',
    },

    {
        'id': 5,
        'name': 'Relay',
        'description': 'A relay is an electrically operated switch. Many relays use an electromagnet to mechanically operate a switch, but other operating principles are also used, such as solid-state relays.',
        'image': 'https://en.wikipedia.org/wiki/Relay#/media/File:Electromagnetic_relay.jpg',
    },

    {
        'id': 6,
        'name': 'Sensor',
        'description': 'Sensor is a device, module, machine, or subsystem whose purpose is to detect events or changes in its environment and send the information to other electronics, frequently a computer processor.',
        'image': 'https://en.wikipedia.org/wiki/Sensor#/media/File:Sensor.jpg',
    },

    {
        'id': 7,
        'name': 'Valve',
        'description': 'A valve is a device that regulates, directs or controls the flow of a fluid (gases, liquids, fluidized solids, or slurries) by opening, closing, or partially obstructing various passageways.',
        'image': 'https://en.wikipedia.org/wiki/Valve#/media/File:Valve.png',
    },

    {
        'id': 8,
        'name': 'Waterhose',
        'description': 'A hose is a flexible tube used to convey fluids from one location to another.',
        'image': 'https://en.wikipedia.org/wiki/Hose#/media/File:Garden_hose.jpg',
    }
    ]
        

    fruits = [
    {
        'id': 1,
        'name': 'apple',
        'description': 'Apple is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Apple is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/apple.jpg',
    },

    {
        'id': 2,
        'name': 'apricot',
        'description': 'Apricot is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Apricot is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/apricot.jpg',
    },

    {
        'id': 3,
        'name': 'cherry',
        'description': 'Cherry is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Cherry is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/cherry.jpg',
    },
    
    {
        'id': 4,
        'name': 'coconut',
        'description': 'Coconut is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Coconut is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/coconut.jpg',
    },

    {
        'id': 5,
        'name': 'fig',
        'description': 'Fig is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Fig is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/fig.jpg',
    },

    {
        'id': 6,
        'name': 'grape',
        'description': 'Grape is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Grape is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/grape.jpg',
    },

    {
        'id': 7,
        'name': 'kiwi',
        'description': 'Kiwi is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Kiwi is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/kiwi.jpg',
    },    

    {
        'id': 8,
        'name': 'lemon',
        'description': 'Lemon is a fruit that is harvested in the early spring. It is a perennial plant that grows from a bulb. Lemon is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/lemon.jpg',
    }

    ]

    herbs = [
    {
        'id': 1,
        'name': 'basil',
        'description': 'Basil is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Basil is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/basil.jpg',
    },
    
    { 
        'id': 2,
        'name': 'chives',
        'description': 'Chives is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Chives is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/chives.jpg',
    },

    {
        'id': 3,
        'name': 'cilantro',
        'description': 'Cilantro is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Cilantro is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/cilantro.jpg',
    },

    {
        'id': 4,
        'name': 'dill',
        'description': 'Dill is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Dill is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/dill.jpg',
    },

    {
        'id': 5,
        'name': 'fennel',
        'description': 'Fennel is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Fennel is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/fennel.jpg',
    },

    {
        'id': 6,
        'name': 'Oregano',
        'description': 'Oregano is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Oregano is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/oregano.jpg',
    },

    {
        'id': 7,
        'name': 'parsley',
        'description': 'Parsley is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Parsley is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/parsley.jpg',
    },

    {
        'id': 8,
        'name': 'rosemary',
        'description': 'Rosemary is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Rosemary is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/rosemary.jpg',
    },

    {
        'id': 9,
        'name': 'sage',
        'description': 'Sage is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Sage is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/sage.jpg',
    },

    {
        'id': 10,
        'name': 'thyme',
        'description': 'Thyme is a cool-season herb that is harvested in the early spring. It is a perennial plant that grows from a bulb. Thyme is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/thyme.jpg',
    }
    ]

    vegetables = [
    {
        'id': 1,    
        'name': 'asparagus',
        'description': 'Asparagus is a spring vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Asparagus is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/asparagus.jpg',
    },

    {
        'id': 2,    
        'name': 'broccoli',
        'description': 'Broccoli is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Broccoli is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/broccoli.jpg',
    },

    {
        'id': 3,    
        'name': 'cabbage',
        'description': 'Cabbage is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Cabbage is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/cabbage.jpg',
    },

    {
        'id': 4,    
        'name': 'carrot',
        'description': 'Carrot is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Carrot is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/carrot.jpg',
    },

    {
        'id': 5,    
        'name': 'cauliflower',
        'description': 'Cauliflower is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Cauliflower is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/cauliflower.jpg',
    },

    {
        'id': 6,    
        'name': 'celery',
        'description': 'Celery is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Celery is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/celery.jpg',
    },

    {
        'id': 7,    
        'name': 'chard',
        'description': 'Chard is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Chard is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/chard.jpg',
    },

    {
        'id': 8,    
        'name': 'collard',
        'description': 'Collard is a cool-season vegetable that is harvested in the early spring. It is a perennial plant that grows from a bulb. Collard is a good source of vitamin K, vitamin C, folate, and fiber. It is also a good source of vitamin A, vitamin E, vitamin B6, thiamin, riboflavin, niacin, pantothenic acid, phosphorus, magnesium, iron, zinc, copper, and manganese.',
        'image': 'https://www.gardeningknowhow.com/wp-content/uploads/2019/04/collard.jpg',
    }  
    ]


    my_devices_file = 'my_devices'
    my_fruits_file = 'my_fruits'
    my_herbs_file = 'my_herbs'
    my_vegetables_file = 'my_vegetables'
    
    '''try to write JSON to file'''
    '''from the Read_JSON_Dictionary class'''    
    my_devices_path = 'jsons\\' + str(my_devices_file) + '.json'
    my_fruits_path = 'jsons\\' + str(my_fruits_file) + '.json'
    my_herbs_path = 'jsons\\' + str(my_herbs_file) + '.json'
    my_vegetables_path = 'jsons\\' + str(my_vegetables_file) + '.json'
    

    print("This main checks for files and creates them if they don't exist.")
    print("Then it writes the JSON data to the files.")
    print()

    '''devices list of dictionaries to json'''
    file_path = Path(my_devices_path)
    if not file_path.exists():
        print(my_devices_path)
        f1 = open(my_devices_path, 'x')
        f1.close()
    if file_path.exists():
        print(my_devices_path)
        rj = Read_JSON_Dictionary(my_devices_path, devices)
        rj.write_JSON_dictionary()

    '''fruits list of dictionaries to json'''
    file_path = Path(my_fruits_path)
    if not file_path.exists():
        print(my_fruits_path)
        f1 = open(my_fruits_path, 'x')
        f1.close()
    if file_path.exists():
        print(my_fruits_path)
        rj = Read_JSON_Dictionary(my_fruits_path, fruits)
        rj.write_JSON_dictionary()

    '''herbs list of dictionaries to json'''
    file_path = Path(my_herbs_path)
    if not file_path.exists():
        print(my_herbs_path)
        f1 = open(my_herbs_path, 'x')
        f1.close()
    if file_path.exists():
        print(my_herbs_path)
        rj = Read_JSON_Dictionary(my_herbs_path, herbs)
        rj.write_JSON_dictionary()

    '''vegetables list of dictionaries to json'''
    file_path = Path(my_vegetables_path)
    if not file_path.exists():
        print(my_vegetables_path)
        f1 = open(my_vegetables_path, 'x')
        f1.close()
    if file_path.exists():
        print(my_vegetables_path)
        rj = Read_JSON_Dictionary(my_vegetables_path, herbs)
        rj.write_JSON_dictionary()

    '''Here I am going to read one of these JSON files
    back into a list of dictionaries'''
    if not file_path.exists():
        print(my_devices_path)
        f1 = open(my_devices_path, 'r')
        f1.close()
    if file_path.exists():
        print(my_devices_path)
        f1 = open(my_devices_path, 'r') 
        my_devices_list = json.loads(f1.read())    
        f1.close()

        '''print end of line character'''
        print()    
        input("Press Enter to continue...")
        print("This is my list of dictionaries from the project:")
        print()
        pprint(my_devices_list)    
        print()
        input("Press Enter to continue...")
        pprint(my_devices_list[0]['name'])
        pprint(my_devices_list[0]['description'])
        pprint(my_devices_list[0]['image'])
        pprint(my_devices_list[1]['name'])
        pprint(my_devices_list[1]['description'])
        pprint(my_devices_list[1]['image'])
        pprint(my_devices_list[2]['name'])
        pprint(my_devices_list[2]['description'])
        pprint(my_devices_list[2]['image'])
        pprint(my_devices_list[3]['name'])
        pprint(my_devices_list[3]['description'])
        pprint(my_devices_list[3]['image'])
        
        '''print end of line character'''
        print()
        input("Press Enter to continue...")
        pprint(my_devices_list[4]['name'])
        pprint(my_devices_list[4]['description'])
        pprint(my_devices_list[4]['image'])
        pprint(my_devices_list[5]['name'])
        pprint(my_devices_list[5]['description'])
        pprint(my_devices_list[5]['image'])
        pprint(my_devices_list[6]['name'])
        pprint(my_devices_list[6]['description'])
        pprint(my_devices_list[6]['image'])
        pprint(my_devices_list[7]['name'])
        pprint(my_devices_list[7]['description'])
        pprint(my_devices_list[7]['image'])
        

        
'''initialize __name__ == '__main__'''
if __name__ == '__main__':
    main()

