from radio import radio, cli


ip = "10.0.1.99"
port = 6610
radio = radio.Radio(ip, port)


if __name__ == "__main__":
    try:
        cli.main(radio)
    except KeyboardInterrupt:
        pass
