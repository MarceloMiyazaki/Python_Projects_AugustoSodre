
class Motor():
    def __init__(self) -> None:
        pass

    def status():
        return "Motor funcionando!"

class Pneu():
    def __init__(self) -> None:
        pass

    def status():
        return "Pneus cheios!"

class Veiculo(Motor, Pneu):
    def status():
        super(Motor).status()
        super(Pneu).status()