level_0_name = "Stół"
gross_requirements_0 = [20,40]
available_0 = 2
planned_order_receipts_0 = [5,7]
lead_time_0 = 1
safety_stock_0 = 0
batches_0 = 0
# Nazwa: [0 - skład, 1 - ilość na magazynie, 2 - lead_time, 3 - safety_stock, 4 - batches]
level_1_components = {
    "Blat": [1, 22, 3, 0, 0],
    "Nogi": [4, 40, 2, 0, 0]                  
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
        messages.append(f"Level 0: {level_0_name}")    
        week_0 = planned_order_receipts[i] - lead_time
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
            messages.append(f"Level 1 component: {name_1}x{info_1[0]}")
            week_1 = week_0 - info_1[2]
            net_1 = (net_with_batches_0 * info_1[0] - info_1[1]) + info_1[3]
            if net_1 < 0:
                net_1 = 0
            if info_1[4] != 0:
                net_with_batches_1 = min_batch(net_1, info_1[4])
            else:
                net_with_batches_1 = net_1
            messages.append(f"Planned order receipts: week {week_0}\nGross requirements: {net_0 * info_1[0]}\nLead Time: {info_1[2]} week(s)\nAvailable in stock: {info_1[1]}\nSafety stock: {info_1[3]}\nBatches of production: {info_1[4]}\nNet requirements: {net_1}\nPlanned order release: {net_with_batches_1} on week {week_1}\n")
            info_1[1] = (net_with_batches_1 + info_1[1]) - (net_0 * info_1[0])
    return "\n".join(map(str, messages))

print(mrp(level_0_name, gross_requirements_0, planned_order_receipts_0, lead_time_0, available_0, safety_stock_0, batches_0, level_1_components))



