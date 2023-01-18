
seated = 0
waiting_to_order = 0
waiting_for_order = 0
eating = 0
leaving_served = 0
rejected = 0


def print_state():
    print("================================")
    print("Currently there are "
          + str(seated)
          + " customers seated")
    print(str(waiting_to_order)
          + " are waiting to order, "
          + str(waiting_for_order)
          + " are waiting for their order and "
          + str(seated - waiting_for_order - waiting_to_order)
          + " are seated served")
    print(str(rejected)
          + " were rejected and "
          + str(leaving_served)
          + " were served so far")


file = open("data.dsl", "r")
for line in file:
    if line != "\n":
        data = line.split("\n")[0]
        data = data.split(" ")
        if data[0].isdigit():
            if data[1] == "enter":
                seated += int(data[0])
                waiting_to_order += int(data[0])
            elif data[1] == "order":
                waiting_to_order -= int(data[0])
                waiting_for_order += int(data[0])
            elif data[1] == "receive":
                waiting_for_order -= int(data[0])
                eating += int(data[0])
            elif data[1] == "leave_served":
                eating -= int(data[0])
                seated -= int(data[0])
                leaving_served += int(data[0])
            elif data[1] == "leave":
                seated -= int(data[0])
                rejected += int(data[0])
        elif data[0] == "state":
            print_state()
