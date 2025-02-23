# MRP - Material Requirements Planning
MRP (Material Requirements Planning) is a Python program that generates an order schedule based on demand for components and available stock levels. The user can interactively input data about products at different levels of the BOM (Bill of Materials) and receive a detailed plan for orders and inventory management.

## 🛠️ Features
Interactive input for finished products and their components
Multi-level BOM structure support
Automatic calculation of net requirements and order schedules
Batch production and stock management support
Generation of a detailed MRP report saved as a text file

## 📊 Program Structure

## 📌 MRP System Levels
1️⃣ Level 0 (Finished Product)
- Gross Requirements (GR)
- Planned Order Receipts (POR)
- Available Stock (A)
- Lead Time (LT)
- Safety Stock (SS)
- Batch Size (B)

2️⃣ Level 1 (Components)
- Quantity needed per finished product
- Available stock
- Lead time
- Safety stock
- Batch size
- Nested Level 2 components if applicable

3️⃣ Level 2 (Subcomponents)
- Components required to produce Level 1 items
- Similar attributes as Level 1

## 🖥️ How It Works
- The user provides data for Level 0 (finished product).
- The program calculates the net requirements based on available stock and gross demand.
- If necessary, orders are scheduled considering lead time and batch size.
- The program moves down the BOM hierarchy, determining required quantities for Level 1 and Level 2 components.
- A detailed MRP report is generated, outlining planned orders and stock levels per week.

## 📄 Output
The program generates a text file report summarizing:
✔️ Planned Order Receipts
✔️ Gross Requirements
✔️ Available Inventory
✔️ Net Requirements
✔️ Order Release Dates

This MRP system helps with production planning and inventory control, ensuring efficient material flow.
