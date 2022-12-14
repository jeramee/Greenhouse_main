from pprint import pprint


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
  
def get_all_devices():
    '''read device dictionary and return the result'''
    for device in devices:
        pprint(device)
    '''press enter to continue'''
    input("Press enter to continue...")

def get_all_herbs():
    '''read herb dictionary and return the result'''
    for herb in herbs:
        pprint(herb)
    '''press enter to continue'''
    input("Press enter to continue...")  

def get_all_vegetables():
    '''read vegetable dictionary and return the result'''
    for vegetable in vegetables:
        pprint(vegetable)
    '''press enter to continue'''
    input("Press enter to continue...")    

def get_all_fruits():
    '''read fruit dictionary and return the result'''
    for fruit in fruits:
        pprint(fruit)
    '''press enter to continue'''
    input("Press enter to continue...")   

def greenhouse():
    '''calls the get_all_herbs() function and returns the result'''
    get_all_devices()
    get_all_herbs()
    get_all_vegetables()
    get_all_fruits()

greenhouse1 = greenhouse()
greenhouse2 = greenhouse()
greenhouse3 = greenhouse()
greenhouse4 = greenhouse()
greenhouse5 = greenhouse()
greenhouse6 = greenhouse()
greenhouse7 = greenhouse()
