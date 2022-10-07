try {
    include [pyfiglet, os, time]
}
catch Exception {
    out < "Please install pyfiglet" | red
    exit(1)
}


public main() {
    out < "[bold]Nuclear Reactor Controler" | red | center | newl
    in name < "Please enter your name : " | endl | green
    out < "Welcome" | name | newl | green
    time.sleep(1)
    out < "Loading..." | endl | green
    time.sleep(2)
    os.system("cls" if os.name == "nt" else "clear")
    reactor()
}


func reactor() {
    powerLevel   = 0
    temperature  = 0
    Heat         = 0
    Power        = 0
    Rods         = 0
    Fuel         = 0
    Water        = 0
    Coolant      = 0
    TotalFuel    = 0
    TotalWater   = 0
    TotalCoolant = 0
    TotalRods    = 0
    Meltdown     = 0
    levelfailed  = False
    while levelfailed != True {
        out < f"Maintain a Power Level of {powerLevel} or above and a Temperature of {temperature} or below" | white | newl
        out < "                                ++++++++           " | newl | white
        out < "                                +++++++            " | newl | white
        out < "     ++++                      ++++++              " | newl | white
        out < "    +++                       +++++                " | newl | white
        out < "   ++                       \ +++ /                " | newl | black
        out < " -|+|-----------            |     |                " | newl | yellow
        out < "/ Reactor Power \           |     |                " | newl | yellow
        out < f"|   {Power}W    |           |     |                " | newl | yellow
        out < "| Control Rods  |          /       \               " | newl | yellow
        out < f"|    {Rods}     |         /---------\              " | newl | yellow
        out < "|               |        /           \             " | newl | yellow
        out < "===================================================" | newl | green
        print(f"""
        Your reactor is currently at {Power}W
        You have {Rods} control rods inserted in the reactor
        You have {Fuel} fuel in the reactor
        The water in the reactor is {Water}g
        The coolant in the reactor is {Coolant}g
        The heat in the reactor is {Heat}C

        Total Supply of Fuel: {TotalFuel}g
        Total Supply of Water: {TotalWater}g
        Total Supply of Coolant: {TotalCoolant}g
        Total Supply of Control Rods: {TotalRods}
        Chances of a meltdown: {Meltdown}%

        1. Insert Control Rod (lowers chance of meltdown by 20%)
        2. Remove Control Rod (Chances of meltdown up by 20%)
        3. Insert Fuel Rod (increases power and chance of meltdown) 
        4. Remove Fuel (lowers chance of meltdown by 10% and lowers power)
        5. Add Water (10g) (This will increase the heat)
        6. Remove Water (10g)
        7. Add Coolant (Water)
        8. Remove Coolant (10g)
        9. Do Nothing
        10. Exit
        """)

        in choice < "Please enter your choice: " | endl | green
    }
}