level_0_name = "Stół"
gross_requirements_0 = [20,40]
available_0 = 2
planned_order_receipts_0 = [6,8]
lead_time_0 = 1
safety_stock_0 = 0
batches_0 = 0
# Nazwa: [0 - Gross requirements, 1 - Planned order receipts, 2 - Available, 3 - Lead Time, 4 - Safety stock, 5 - Batches]
level_0_item = {
    level_0_name: [gross_requirements_0, planned_order_receipts_0 ,available_0, lead_time_0, safety_stock_0, batches_0]
}
# Nazwa: [0 - skład 1 sztuki z levelu 0, 1 - ilość na magazynie, 2 - lead_time, 3 - safety_stock, 4 - batches, 5 - Level 2 components]
level_1_components = {
    "Blat": [1, 22, 3, 0, 0, {"Płyta pilśniowa": [1,5,1,0,0]}],
    "Nogi": [4, 40, 2, 0, 0,{}]                  
                      }

def min_batch(net_quantity,batch):
    batches_needed = net_quantity // batch
    if net_quantity % batch != 0:
        batches_needed += 1
    return batches_needed * batch
def mrp(l_0_name, gross_requirements, planned_order_receipts, lead_time, in_stock, safety_stock, batches, l_1_components):
    messages = []
# Level 0
    for i in range(len(gross_requirements)):
        messages.append(f"Level 0: {l_0_name}")    
        week_0 = planned_order_receipts[i] - lead_time
        if week_0 <= 0:
            return(f"Order for item {l_0_name} can't be made on time with a planned order receipt on week {planned_order_receipts[i]} and a lead time of {lead_time}.")
        net_0 = (gross_requirements[i] - in_stock) + safety_stock
        if net_0 < 0:
            net_0 = 0
        if batches != 0:
            net_with_batches_0 = min_batch(net_0, batches)
        else:
            net_with_batches_0 = net_0
        messages.append(f"Planned order receipts: week {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net_0}\nPlanned order release: {net_with_batches_0} on week {week_0}\n")
        in_stock = (net_with_batches_0 + in_stock) - gross_requirements[i]
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

print(mrp(level_0_name, gross_requirements_0, planned_order_receipts_0, lead_time_0, available_0, safety_stock_0, batches_0, level_1_components))



