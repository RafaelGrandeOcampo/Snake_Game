from turtle import Turtle


class Score(Turtle):

    def __init__(self):
        super().__init__()
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.marcador = 0
        self.color("white")
        self.penup()
        self.setposition(0, 270)
        self.actualizar_marcador()
        self.hideturtle()

    def actualizar_marcador(self):
        self.clear()
        self.write(f"Puntuación = {self.marcador}    Puntuación mas alta = {self.high_score}", align="center", font=("Arial", 20, "normal"))

    def reset(self):
        if self.marcador > self.high_score:
            self.high_score = self.marcador
            with open("data.txt", "w") as data:
                data.write(f"{self.high_score}")
        self.marcador = 0
        self.actualizar_marcador()

   # def game_over(self):
   #     self.setposition(0, 0)
   #     self.write("Game Over", align="center", font=("Arial", 20, "normal"))


    def puntuacion(self):
        self.marcador += 1

        self.actualizar_marcador()










