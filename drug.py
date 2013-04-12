import random, sys, time

def intro():
    print("D R U G  L O R D")

def startGame():
    money = 1000
    drugs = {'weed':0, 'coke':0, 'h':0, 'meth':0, 'x':0, 'mush':0, 'crk':0, 'oc':0, 'xx':0}
    drugPrices = [0, 0, 0, 0, 0, 0, 0, 0, 0]
    
def getName():
    print("What name will you go by?")
    return input()

def loadTravel():
    iNum = 0
    for i in cities:
        iNum += 1
        print('' + str(iNum) + '.', end=' ')
        print(i)

def pickCity():
    print('Choose a city.')
    choice = input()
    choice = int(choice) - 1
    city = cities[int(choice)]
    setPrices()
    return city

def quitGame():
    sys.exit()

def setPrices():
    drugPrices.clear()
    drugPrices.append(random.randint(149, 350))
    drugPrices.append(random.randint(500, 750))
    drugPrices.append(random.randint(250, 500))
    drugPrices.append(random.randint(60, 120))
    drugPrices.append(random.randint(5, 20))
    drugPrices.append(random.randint(20, 50))
    drugPrices.append(random.randint(40, 80))
    drugPrices.append(random.randint(80, 180))
    drugPrices.append(random.randint(2, 7))

def loadDeal(drug, price):
    print('''
''' + str(drug) + ''': $''' + str(price) + '''
1. Buy
2. Sell
3. Cancel
''')
    if input() == '1':
        print('buy mode')
    elif input() == '2':
        print('sell mode')
    elif input() == '3':
        doWhat()
        

def loadMarket():
    print('''
----------------------------------------
''' + str(currentCity) + '''
----------------------------------------
''')
    iNum = 0
    for i in drugPrices:
        iNum += 1
        print('' + str(iNum) + '.', end=' ')
        print(drugNames[iNum - 1], end=': $')
        print(i)
    print('10. Return Home')
    print('Enter your selection.')
    drawHud()
    choice = input()
    choice = int(choice) - 1
    if int(choice) in range(0, 9):
        currentDrug = drugNames[int(choice)]
        currentPrice = drugPrices[int(choice)]
        print('Do you want to deal '+ currentDrug + '?')
        if input().lower().startswith('y'):
            loadDeal(currentDrug, currentPrice)

    if choice == '9':
        doWhat()
    elif choice in 'quit q exit e x'.split():
        quitGame()
    else:
        print('Please enter a valid option from the list.')
    
def doWhat():
    choice=''
    while True:
        print('''
1. Buy/Sell locally
2. Travel
3. Grow/Manufacture
4. Visit Loan Shark
What would you like to do?''')
        drawHud()
        choice = input()
        if choice == '1':
            loadMarket()
        elif choice == '2':
            loadTravel()
        elif choice == '3':
            loadGrow()
        elif choice == '4':
            loadShark()
        elif choice in 'quit q exit e x'.split():
            quitGame()
        else:
            print('Please enter a valid option from the list.')

def drawHud():
    print("$" + str(money))
        
cities = ['Los Angeles', 'Detroit', 'Honolulu', 'Miami', 'Seattle', 'Portland', 'Chicago', 'New York', 'Memphis', 'Little Rock', 'San Francisco', 'Dallas']
random.shuffle(cities)                  
drugs = {}
drugPrices = []
drugNames = 'Marijuana Cocaine Heroin Methamphetamine Ecstasy Mushrooms Crack Oxycontin Xanax'.split()
pName=None
intro()
money = 1000
pName=getName()
print("Alright " + pName + ", let's sell some drugs!")
startGame()
loadTravel()
currentCity=pickCity()
while True:
    doWhat()
