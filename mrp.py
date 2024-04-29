pen_gross_requirements = [450,630,100]
pen_available = 700
pen_planned_order_receipts = [5,6,7]
pen_lead_time = 1
pen_safety_stock = 200
pen_batches = 100

def pen_mrp(gross_requirements, planned_order_receipts, lead_time, in_stock, safety_stock, batches):
    messages = []
    for i in range(len(gross_requirements)):
        if safety_stock == 0 and batches == 0:
            week = planned_order_receipts[i] - lead_time
            net = gross_requirements[i] - in_stock
            if gross_requirements[i] > in_stock:
                messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net}\nPlanned order release: {week}\n")
                in_stock = 0
            else:
                if net <= 0:
                    net = 0
                messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net}\nPlanned order release: {week}\n") 
                in_stock = in_stock - gross_requirements[i]
        elif safety_stock != 0 and batches == 0:
            week = planned_order_receipts[i] - lead_time
            net = gross_requirements[i] - in_stock
            if (gross_requirements[i] + safety_stock) > in_stock:
                messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net}\nPlanned order release: {week}\n")
                in_stock = safety_stock
            else:
                messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net}\nPlanned order release: {week}\n") 
                in_stock = in_stock - gross_requirements[i]
        elif safety_stock == 0 and batches != 0:
        #     week = planned_order_receipts[i] - lead_time
        #     net = gross_requirements[i] - in_stock
        #     n = 1
        #     net_with_batches = 0
        #     while batches%net != 0 and net_with_batches < net:
        #         net_with_batches = batches * n 
        #         n += 1
        #     if gross_requirements[i] > in_stock:
        #         messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net_with_batches}\nPlanned order release: {week}\n")
        #         in_stock = (net_with_batches + in_stock) - gross_requirements[i]
        #     else:
        #         messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net_with_batches}\nPlanned order release: {week}\n") 
        #         in_stock = in_stock - gross_requirements[i]
        # else:
        #     week = planned_order_receipts[i] - lead_time
        #     net = gross_requirements[i] - in_stock
        #     n = 1
        #     net_with_batches = 0
        #     while batches%net != 0 and net_with_batches < net:
        #         net_with_batches = batches * n 
        #         n += 1
        #     if (gross_requirements[i] + safety_stock) > in_stock:
        #         messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net_with_batches}\nPlanned order release: {week}\n")
        #         in_stock = (net_with_batches + in_stock + safety_stock) - gross_requirements[i]
        #         if in_stock < safety_stock:
        #             raise ValueError
        #     else:
        #         messages.append(f"Planned order receipts: {planned_order_receipts[i]}\nGross requirements: {gross_requirements[i]}\nLead Time: {lead_time} week(s)\nAvailable in stock: {in_stock}\nSafety stock: {safety_stock}\nBatches of production: {batches}\nNet requirements: {net_with_batches}\nPlanned order release: {week}\n") 
        #         if in_stock < safety_stock:
        #             raise ValueError
        #         in_stock = in_stock - gross_requirements[i]
    return "\n".join(map(str, messages))

print(pen_mrp(pen_gross_requirements, pen_planned_order_receipts, pen_lead_time, pen_available, pen_safety_stock, pen_batches))

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

# Dodatkowo 
time_of_delivery = ""
safety_stock = ""
batches = ""

# Dane o produkcie
pen = ""
body = ""
cap = ""
ink = ""




