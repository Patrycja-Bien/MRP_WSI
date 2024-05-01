pen_gross_requirements = [20,40]
pen_available = 18
pen_planned_order_receipts = [5,7]
pen_lead_time = 1
pen_safety_stock = 0
pen_batches = 0
def min_batch(net_quantity,batch):
    batches_needed = net_quantity // batch
    if net_quantity % batch != 0:
        batches_needed += 1
    return batches_needed * batch
def mrp_level_0(gross_requirements, planned_order_receipts, lead_time, in_stock, safety_stock, batches):
    messages = []
    for i in range(len(gross_requirements)):
        week = planned_order_receipts[i] - lead_time
        net = (gross_requirements[i] - in_stock) + safety_stock
        if net <= 0:
            net = 0
        if batches != 0:
            net_with_batches = min_batch(net, batches)
        else:
            net_with_batches = net
        messages.append(f"Planned order receipts: week {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net}\nPlanned order release: {net_with_batches} on week {week}\n")
        in_stock = (net_with_batches + in_stock) - gross_requirements[i]
    return "\n".join(map(str, messages))

print(mrp_level_0(pen_gross_requirements, pen_planned_order_receipts, pen_lead_time, pen_available, pen_safety_stock, pen_batches))

body_gross_requirements = ""
body_scheduled_requests = ""
body_available = ""
body_net_requirements = ""
body_planned_order_release = ""
body_lt = 2

cap_gross_requirements = ""
cap_scheduled_requests = ""
cap_available = ""
cap_net_requirements = ""
cap_planned_order_release = ""
cap_lt = 1

ink_gross_requirements = ""
ink_scheduled_requests = ""
ink_available = ""
ink_net_requirements = ""
ink_planned_order_release = ""
ink_lt = 1




