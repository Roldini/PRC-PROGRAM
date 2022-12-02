import math
import arcade
import random


BREDDE = 1500
HOEJDE = 600
SPORLAENGDE = 500
FARVE = arcade.csscolor.YELLOW
maal_x = 200 + random.randint(1, BREDDE - 200)
maal_y = 25


def projektilbane(tid, stationaert_punkt, retningsvektor):
    x_0, y_0 = stationaert_punkt
    r_x, r_y = retningsvektor
    x = x_0 + r_x * tid
    y = y_0 + r_y * tid

    return x, y



def konsol():
    while not False:
        print("angiv løbsrettelse, fra 0 og op efter")
        vaerdi = input("= ")

        tegn.tid = tegn.tid

        if vaerdi.count(vaerdi, 0, None):
            break

        elif vaerdi.title(None):
            tegn.tid = tegn.tid
            break

def tegn(deltatid):

    arcade.start_render()
    vaerdi = input("= ")
    x, y = projektilbane(tegn.tid, (0, 21), (vaerdi, 9.82 - math.sqrt(tegn.tid)))
    arcade.draw_circle_filled(x, y, 3, FARVE)
    for punkt in tegn.spor:
                arcade.draw_circle_filled(*punkt, 2, FARVE)
            # projektilet vil kun bevæge sig når det er indenfor vinduet og når det ikke rammer jorden
    if (x >= 0 and x < BREDDE) and (y >= 21 and y <= HOEJDE):
        tegn.tid += deltatid * 60  # 5
        tegn.spor.append((x, y))
            # tiden sættes lig sig selv, bliver konstant og stopper derfor
    else:
        tegn.tid = tegn.tid

            # hvis projektilet rammer maalet stopper det, og der vises en animation
        if (x >= maal_x - 75 and x < maal_x + 75) and (y >= 0 and y <= maal_y):
                arcade.draw_circle_filled(maal_x, maal_y, 75, arcade.csscolor.ORANGE)
                arcade.draw_circle_filled(maal_x, maal_y, 57, arcade.csscolor.ORANGE_RED)
                tegn.tid = tegn.tid

            # målet tegnes
        arcade.draw_rectangle_filled(maal_x, maal_y, 75, 10, arcade.csscolor.RED)
            # jorden tegnes
        arcade.draw_lrtb_rectangle_filled(0, BREDDE, 20, 0, arcade.csscolor.GREEN)




def main():
        arcade.open_window(BREDDE, HOEJDE)

        arcade.set_background_color(arcade.csscolor.SKY_BLUE)

        tegn.tid = 0
        tegn.spor = list()
        arcade.schedule(tegn, 1 / 60)

        arcade.run()


if __name__ == "__main__":
    main()
