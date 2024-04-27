pen_gross_requirements = [450,630]
#pen_scheduled_receipts = 0 # chyba niepotrzebne
pen_available = 100
#pen_net_requirements = 0
pen_planned_order_receipts = 0
pen_planned_order_release = [5,6]
pen_lead_time = 1
pen_safety_stock = 0
pen_batches = 200

def pen_mrp(gross_requirements, planned_order_release, lead_time, in_stock, safety_stock, batches):
    messages = []
    for i in range(len(gross_requirements)):
        if safety_stock == 0 and batches == 0:
            week = planned_order_release[i] - lead_time
            net = gross_requirements[i] - in_stock
            if gross_requirements[i] > in_stock:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.,\nna magazynie jest {in_stock} gotowych długopisów,\nnie ma minimalnej ilości długopisów na magazynie,\ni nie ma określonej partii produkcji,\nto należy wytworzyć {net} długopisów w tygodniu nr {week}.\n" )
                in_stock = 0
            else:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.\nna magazynie jest {in_stock} gotowych długopisów,\nnie ma minimalnej ilości długopisów na magazynie,\ni nie ma określonej partii produkcji,\nto nie potrzeba wytwarzać więcej długopisów w tygodniu nr {week}.\n") 
                in_stock = net*(-1)
        elif safety_stock != 0 and batches == 0:
            week = planned_order_release[i] - lead_time
            net = gross_requirements[i] - in_stock
            if (gross_requirements[i] + safety_stock) > in_stock:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.,\nna magazynie jest {in_stock} gotowych długopisów,\nminimalna ilość długopisów na magazynie to {safety_stock},\ni nie określonej partii produkcji,\nto należy wytworzyć {net + safety_stock} długopisów w tygodniu nr {week}.\n" )
                in_stock = safety_stock
            else:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.,\nna magazynie jest {in_stock} gotowych długopisów,\nminimalna ilość długopisów na magazynie to {safety_stock},\ni nie określonej partii produkcji,\nto nie potrzeba wytwarzać więcej długopisów w tygodniu nr {week}.\n") 
                in_stock = in_stock - gross_requirements[i]
                if in_stock < safety_stock:
                    sub = safety_stock - in_stock
                    in_stock += sub
        elif safety_stock == 0 and batches != 0:
            week = planned_order_release[i] - lead_time
            net = gross_requirements[i] - in_stock
            # dokończyć
            if gross_requirements[i] > in_stock:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.,\nna magazynie jest {in_stock} gotowych długopisów,\nnie ma minimalnej ilości długopisów na magazynie,\na określona partia produkcji to {batches},\nto należy wytworzyć {net} długopisów w tygodniu nr {week}.\n" )
                in_stock = None
            else:
                messages.append(f"Jeśli na tydzień nr {planned_order_release[i]} jest potrzebne {gross_requirements[i]} długopisów,\nczas wytworzenia to {lead_time} tyg.\nna magazynie jest {in_stock} gotowych długopisów,\nnie ma minimalnej ilości długopisów na magazynie,\na określona partia produkcji to {batches},\nto nie potrzeba wytwarzać więcej długopisów w tygodniu nr {week}.\n") 
                in_stock = in_stock - gross_requirements[i]
        else:
            pass
    return "\n".join(map(str, messages))

print(pen_mrp(pen_gross_requirements, pen_planned_order_release, pen_lead_time, pen_available, pen_safety_stock, pen_batches))

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




