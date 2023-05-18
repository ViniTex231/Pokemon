from jogo import battle


def start():
    while True:
        start = input("Press '1' for start the game: ")
        if start == "1":
            battle()


if __name__ == "__main__":
    start()
