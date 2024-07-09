import turtle

def draw_star(num_points):
    screen = turtle.Screen()
    board = turtle.Turtle()

    screen.bgcolor("LightSalmon")
    screen.setup(400, 300)
    screen.title("Kachua screen")

    # Angle calculation for drawing a star
    angle = 180 - (180 / num_points)

    board.penup()
    board.goto(-50, 0)  # Move to a starting position
    board.pendown()

    for _ in range(num_points):
        board.forward(400)
        board.right(angle)

    screen.mainloop()

def main():
    num_points = int(input("Enter the number of points for the star: "))
    if num_points < 5:
        print("A star needs at least 5 points.")
        return
    draw_star(num_points)

if __name__ == "__main__":
    main()
