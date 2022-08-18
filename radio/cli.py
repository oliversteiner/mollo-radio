def commandline_header():
    print('-----------------------')
    print('Stations:        1 to 4')
    print('Play / Pause:    p')
    print('Stop:            s')
    print('Volume:          + and -')
    print('------------------------')
    print('choose:')


def main(radio):
    commandline_header()
    cli_active = True

    while cli_active:
        user_command = input()

        # Quit
        if user_command == "q":
            cli_active = False

        # Play Station Nr
        elif user_command == "1" or user_command == "2" or user_command == "3" or user_command == "4":
            radio.play_song(user_command)

        # Play or Pause
        elif user_command == "p":
            radio.play_pause()

        # Stop
        elif user_command == "s":
            radio.stop()

        # Volume Up
        elif user_command == "+":
            radio.volume_up()

        # Volume Down
        elif user_command == "-":
            radio.volume_down()

        # Show Client Info
        elif user_command == "i":
            radio.show_info()

        # undefined input
        else:
            print("command not defined")