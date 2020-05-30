def print_message_box(message):
    """Imprime a mensagem em uma caixa de mensagem"""

    lines = message.splitlines()

    longer = 0
    for line in lines:
        if(len(line) > longer):
            longer = len(line)


    count = longer + 2

    horizontal_bar = "-" * count
    print()
    print(f"+{horizontal_bar}+")
    for line in lines:
        print(f"| {line.ljust(longer)} |")
    print(f"+{horizontal_bar}+")
    print()