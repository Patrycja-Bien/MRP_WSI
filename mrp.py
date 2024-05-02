# Name: [0 - Gross requirements, 1 - Planned order receipts, 2 - Available, 3 - Lead Time, 4 - Safety stock, 5 - Batches]
level_0_item = {"Name": ["GR", "POR", "A", "LT", "SS", "B"]}
# Name: [0 - How much for 1 piece of level 0, 1 - Available, 2 - Lead time, 3 - Safety stock, 4 - Batches, {5 - Level 2 components}]
level_1_components = {"Name": ["N", "A", "LT", "SS", "B", {"Name": ["N", "A", "LT", "SS", "B"]}]}

interactive = input("Would you like to use iteractive input version? (Y/N): ")
if interactive.upper() == "Y":
    level_0_item.clear()
    level_1_components.clear()
# Interactive input: Level 0
    level_0_name = input("Name your level 0 item: ")
    gross_requirements_0 = []
    planned_order_receipts_0 = []
    try:
        order_count = int(input(f"How many of orders would you like to place for {level_0_name}?: "))
        for order in range(order_count):
            gross_requirements_0.append(int(input(f"State your gross requirements for order {order + 1} of {order_count} for {level_0_name}: ")))
            planned_order_receipts_0.append(int(input(f"State your planned week of receipt for order {order + 1} of {order_count} for {level_0_name}: ")))
        available_0 = int(input(f"How many of {level_0_name} is available?: "))
        lead_time_0 = int(input(f"What is the lead time for {level_0_name} in weeks?: "))
        safety_stock_0 = int(input(f"What is the safety stock for {level_0_name}?: "))
    except ValueError:
        raise ValueError("Input must be an integer.")
    batches_0 = input(f"Do you make {level_0_name} in fixed batches? (Y/N): ")
    if batches_0.upper() == "Y":
        try:
            batches_0 = int(input(f"What is the size of the batch for {level_0_name}?: "))
        except ValueError:
            raise ValueError("Input must be an integer.")
    elif batches_0.upper() == "N":
        batches_0 = 0
    else:
        raise ValueError("Wrong input. Type only 'Y' or 'N'.")
    level_0_item.update({level_0_name: [gross_requirements_0, planned_order_receipts_0, available_0, lead_time_0,safety_stock_0, batches_0]})
    # Interactive input: Level 1
    try:
        component_count_1 = int(input(f"How many level 1 components does the {level_0_name} have?: "))
    except ValueError:
        raise ValueError("Input must be an integer.")
    for component in range(component_count_1):
        level_1_name = input("Name your level 1 component: ")
        try:
            needed_1 = int(input(f"How many of {level_1_name} is needed to make 1 piece of {level_0_name}?: "))
            available_1 = int(input(f"How many of {level_1_name} is available?: "))
            lead_time_1 = int(input(f"What is the lead time for {level_1_name} in weeks?: "))
            safety_stock_1 = int(input(f"What is the safety stock for {level_1_name}?: "))
        except ValueError:
            raise ValueError("Input must be an integer.")
        batches_1 = input(f"Do you make {level_1_name} in fixed batches? (Y/N): ")
        if batches_1.upper() == "Y":
            try:
                batches_1 = int(input(f"What is the size of the batch for {level_1_name}?: "))
            except ValueError:
                raise ValueError("Input must be an integer.")
        elif batches_1.upper() == "N":
            batches_1 = 0
        else:
            raise ValueError("Wrong input. Type only 'Y' or 'N'.")
        level_1_components.update({level_1_name: [needed_1, available_1, lead_time_1, safety_stock_1, batches_1, {}]})
    # Interactive input: Level 2
        try:
            component_count_2 = int(input(f"How many level 2 components does the {level_1_name} have?: "))
        except ValueError:
            raise ValueError("Input must be an integer.")
        for component in range(component_count_2):
            level_2_name = input(f"Name your level 2 component for {level_1_name}: ")
            try:
                needed_2 = int(input(f"How many of {level_2_name} is needed to make 1 piece of {level_1_name}?: "))
                available_2 = int(input(f"How many of {level_2_name} is available?: "))
                lead_time_2 = int(input(f"What is the lead time for {level_2_name} in weeks?: "))
                safety_stock_2 = int(input(f"What is the safety stock for {level_2_name}?: "))
            except ValueError:
                raise ValueError("Input must be an integer.")
            batches_2 = input(f"Do you make {level_2_name} in fixed batches? (Y/N): ")
            if batches_2.upper() == "Y":
                try:
                    batches_2 = int(input(f"What is the size of the batch for {level_2_name}?: "))
                except ValueError:
                    raise ValueError("Input must be an integer.")
            elif batches_2.upper() == "N":
                batches_2 = 0
            else:
                raise ValueError("Wrong input. Type only 'Y' or 'N'.")
            level_1_components[level_1_name][5].update({level_2_name: [needed_2, available_2, lead_time_2, safety_stock_2, batches_2]})
elif interactive.upper() == "N":
    pass
else:
    raise ValueError("Wrong input. Type only 'Y' or 'N'.")

def min_batch(net_quantity,batch):
    batches_needed = net_quantity // batch
    if net_quantity % batch != 0:
        batches_needed += 1
    return batches_needed * batch

def mrp(l_0_item, l_1_components):
    messages = []
# Level 0
    for name_0, info_0 in l_0_item.items():
        for i in range(len(info_0[0])):
            messages.append(f"Level 0: {name_0}")    
            week_0 = info_0[1][i] - info_0[3]
            if week_0 <= 0:
                return(f"Order for item {name_0} can't be made on time with a planned order receipt on week {info_0[1][i]} and a lead time of {info_0[3]}.")
            net_0 = (info_0[0][i] - info_0[2]) + info_0[4]
            if net_0 < 0:
                net_0 = 0
            if info_0[5] != 0:
                net_with_batches_0 = min_batch(net_0, info_0[5])
            else:
                net_with_batches_0 = net_0
            messages.append(f"Planned order receipts: week {info_0[1][i]}\nGross requirements: {info_0[0][i]}\nLead Time: {info_0[3]} week(s)\nAvailable in stock: {info_0[2]}\nSafety stock: {info_0[4]}\nBatches of production: {info_0[5]}\nNet requirements: {net_0}\nPlanned order release: {net_with_batches_0} on week {week_0}\n")
            info_0[2] = (net_with_batches_0 + info_0[2]) - info_0[0][i]
    # Level 1
            for name_1,info_1 in l_1_components.items():
                messages.append(f"Level 1 component: {name_1} x {info_1[0]}")
                week_1 = week_0 - info_1[2]
                if week_1 <= 0:
                    return(f"Order for item {name_1} can't be made on time with a planned order receipt on week {week_0} and a lead time of {info_1[2]}.")
                net_1 = (net_with_batches_0 * info_1[0] - info_1[1]) + info_1[3]
                if net_1 < 0:
                    net_1 = 0
                if info_1[4] != 0:
                    net_with_batches_1 = min_batch(net_1, info_1[4])
                else:
                    net_with_batches_1 = net_1
                messages.append(f"Planned order receipts: week {week_0}\nGross requirements: {net_0 * info_1[0]}\nLead Time: {info_1[2]} week(s)\nAvailable in stock: {info_1[1]}\nSafety stock: {info_1[3]}\nBatches of production: {info_1[4]}\nNet requirements: {net_1}\nPlanned order release: {net_with_batches_1} on week {week_1}\n")
                info_1[1] = (net_with_batches_1 + info_1[1]) - (net_0 * info_1[0])
    # Level 2
                if len(info_1[5]) != 0:
                    for name_2, info_2 in l_1_components[name_1][5].items():
                        messages.append(f"Level 2 component: {name_2} x {info_2[0]}")
                        week_2 = week_1 - info_2[2]
                        if week_2 <= 0:
                            return(f"Order for item {name_2} can't be made on time with a planned order receipt on week {week_1} and a lead time of {info_2[2]}.")
                        net_2 = (net_with_batches_1 * info_2[0] - info_2[1]) + info_2[3]
                        if net_2 < 0:
                            net_2 = 0
                        if info_2[4] != 0:
                            net_with_batches_2 = min_batch(net_2, info_2[4])
                        else:
                            net_with_batches_2 = net_2
                        messages.append(f"Planned order receipts: week {week_0}\nGross requirements: {net_1 * info_2[0]}\nLead Time: {info_2[2]} week(s)\nAvailable in stock: {info_2[1]}\nSafety stock: {info_2[3]}\nBatches of production: {info_2[4]}\nNet requirements: {net_2}\nPlanned order release: {net_with_batches_2} on week {week_2}\n")
                        info_2[1] = (net_with_batches_2 + info_2[1]) - (net_1 * info_2[0])
    return "\n".join(map(str, messages))

print(mrp(level_0_item, level_1_components))



