from django.shortcuts import render
from base.models import Vegetable, Fruit, Herb
from django.views.generic import ListView

# Create your views here.
greenhouses = [
    {'id': 1, 'name': 'Greenhouse 1'},
    {'id': 2, 'name': 'Greenhouse 2'},   
    {'id': 3, 'name': 'Greenhouse 3'},
    {'id': 4, 'name': 'Greenhouse 4'},
    {'id': 5, 'name': 'Greenhouse 5'},   
    {'id': 6, 'name': 'Greenhouse 6'},
    {'id': 7, 'name': 'Greenhouse 7'}
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
    

def home(request):
    context = {'greenhouses': greenhouses}
    return render(request, 'base/home.html', context)

def greenhouse(request, pk):
    greenhouse = None
    for i in greenhouses:
        if i['id'] == int(pk):
            greenhouse = i
    context = {'greenhouse': greenhouse}
    return render(request, 'base/greenhouse.html', context)

def device(request, pk):
    device = None
    for i in device:
        if i['id'] == int(pk):
            device = i
    context = {'device': device}
    return render(request, 'base/device.html', context)

def fruit(request, pk):
    fruit = None
    for i in fruit:
        if i['id'] == int(pk):
            fruit = i
    context = {'fruit': fruit}
    return render(request, 'base/fruit.html', context)    

def herb(request, pk):
    herb = None
    for i in herb:
        if i['id'] == int(pk):
            herb = i
    context = {'herb': herb}
    return render(request, 'base/herb.html', context)

def vegetable(request, pk):
    vegetable = None
    for i in vegetable:
        if i['id'] == int(pk):
            vegetable = i
    context = {'vegetable': vegetable}
    return render(request, 'base/vegetable.html', context)

# Various Greenhouse Objects
def gh1(request):
    context = {'gh1': gh1}
    return render(request, 'base/gh1.html', context)

def gh2(request):
    context = {'gh2': gh2}
    return render(request, 'base/gh2.html', context)

def gh3(request):
    context = {'gh3': gh3}
    return render(request, 'base/gh3.html', context)

def gh4(request):
    context = {'gh4': gh4}
    return render(request, 'base/gh4.html', context)

def gh5(request):
    context = {'gh5': gh5}
    return render(request, 'base/gh5.html', context)

def gh6(request):
    context = {'gh6': gh6}
    return render(request, 'base/gh6.html', context)

def gh7(request):
    context = {'gh7': gh7}
    return render(request, 'base/gh7.html', context)

def add_plant(request):
    context = {'add_plant': add_plant}
    return render(request, 'base/add_plant.html', context)

def add_device(request):
    context = {'add_device': add_device}
    return render(request, 'base/add_device.html', context)


# Devices for various greenhouses
def gh1_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh1_add_device.html', context)

def gh2_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh2_add_device.html', context)

def gh3_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh3_add_device.html', context)

def gh4_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh4_add_device.html', context)

def gh5_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh5_add_device.html', context)

def gh6_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh6_add_device.html', context)

def gh7_add_device(request):
    context = {'devices': devices}
    return render(request, 'base/devices/gh7_add_device.html', context)


# Fruits for various greenhouses
def gh1_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh1_add_fruit.html', context)

def gh2_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh2_add_fruit.html', context)

def gh3_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh3_add_fruit.html', context)

def gh4_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh4_add_fruit.html', context)

def gh5_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh5_add_fruit.html', context)

def gh6_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh6_add_fruit.html', context)

def gh7_add_fruit(request):
    context = {'fruits': fruits}
    return render(request, 'base/fruits/gh7_add_fruit.html', context)


# Herbs for various greenhouses
def gh1_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh1_add_herb.html', context)

def gh2_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh2_add_herb.html', context)

def gh3_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh3_add_herb.html', context)

def gh4_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh4_add_herb.html', context)

def gh5_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh5_add_herb.html', context)

def gh6_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh6_add_herb.html', context)

def gh7_add_herb(request):
    context = {'herbs': herbs}
    return render(request, 'base/herbs/gh7_add_herb.html', context)


# Vegetables for various greenhouses
def gh1_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh1_add_vegetable.html', context)

def gh2_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh2_add_vegetable.html', context)

def gh3_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh3_add_vegetable.html', context)

def gh4_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh4_add_vegetable.html', context)

def gh5_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh5_add_vegetable.html', context)

def gh6_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh6_add_vegetable.html', context)

def gh7_add_vegetable(request):
    context = {'vegetables': vegetables}
    return render(request, 'base/vegetables/gh7_add_vegetable.html', context)

# Dictionary to store inventory while the user is logged in
def gh1_dictionary(request):
    context = {'gh1_dictionary': gh1_dictionary}
    return render(request, 'base/gh1_dictionary.html', context)

def gh2_dictionary(request):
    context = {'gh2_dictionary': gh2_dictionary}
    return render(request, 'base/gh2_dictionary.html', context)

def gh3_dictionary(request):
    context = {'gh3_dictionary': gh3_dictionary}
    return render(request, 'base/gh3_dictionary.html', context)

def gh4_dictionary(request):
    context = {'gh4_dictionary': gh4_dictionary}
    return render(request, 'base/gh4_dictionary.html', context)

def gh5_dictionary(request):
    context = {'gh5_dictionary': gh5_dictionary}
    return render(request, 'base/gh5_dictionary.html', context)

def gh6_dictionary(request):
    context = {'gh6_dictionary': gh6_dictionary}
    return render(request, 'base/gh6_dictionary.html', context)

def gh7_dictionary(request):
    context = {'gh7_dictionary': gh7_dictionary}
    return render(request, 'base/gh7_dictionary.html', context)
