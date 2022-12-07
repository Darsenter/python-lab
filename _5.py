class Rocket():
    def q(objectr, sum_weight, fuel, engine):
        objectr.sum_weight = sum_weight
        objectr.fuel = fuel
        objectr.engine = engine
    def fuel_spend(objectr, count):
        objectr.fuel -= count
        objectr.sum_weight -= count
        if objectr.fuel <= 0:
            objectr.fuel = 0
            objectr.engine = False
            return False
        elif objectr.fuel > 0:
            objectr.engine = True
            return True
    def fuel_status(objectr):
        return f'количество топлива: {objectr.fuel}'
    def engine_status(objectr):
        return f'состояние двигателя: {objectr.engine}'
    def weight_status(objectr):
        return f'текущая масса: {objectr.sum_weight}'
    
def main():
    Rocket_test = Rocket(5000, 2000, True)
    while Rocket_test.fuel > 0:
        Rocket_test.fuel_spend(100)
        print(Rocket_test.fuel_status())
        print(Rocket_test.weight_status())
        print(Rocket_test.engine_status())
        
