# ===============================================================
# SDEV 120: Final Payroll Project - Milestone 3
# Developed by: Hanen Sassi
# Objective : implement File Read and Write with Parallel Arrays 
# ==============================================================

# ==============================================================
#  BLOCK 1: Initialize parallel lists and read input file
# ==============================================================

employee_names = []
employee_ids = []
dependents_list = []
hours_worked_list = []
hourly_wages = []

gross_pay_list = []
state_tax_list = []
federal_tax_list = []
dep_deduction_list = []
net_pay_list = []

print("=== BLOCK 1: Reading Input File ===")
fileName = "data.txt" 
   
with open("data.txt", 'r') as file:
               
    for line in file:
        data = line.strip().split(",")
        if len(data) >= 5:
                employee_names.append(data[0].strip())
                employee_ids.append(data[1].strip())
                dependents_list.append(int(data[2].strip()))
                hours_worked_list.append(float(data[3].strip()))
                hourly_wages.append(float(data[4].strip()))
    
total_employees = len(employee_names)
print("total employees read successfully:", total_employees)

#=========================================================================
#  BLOCK 2: Arrays Processing, Security Validation, and calculation
#=========================================================================
print("\n=== BLOCK 2: Processing calculations and security validation ===")
total_employees = len(employee_names)
for i in range(total_employees):
    # pull data out of parallel arrays  automatically
    employee_name = employee_names[i]
    employee_id = employee_ids[i]
    dependents = dependents_list[i]
    hours_worked = hours_worked_list[i]
    hourly_wage = hourly_wages[i]

    # INPUT VALIDATION / SECURITY CHEKS ( your custom guard rails)
    if hourly_wage < 0:
        hourly_wage = 0.0
    if hours_worked < 0 or hours_worked > 80:
        print("[SECURITY ERROR ] Invalid hours or negative value detected!")
        hours_worked = 0.0
    if dependents < 0:
        print("Security Alert: Invalid hours or negative value detected!")
        dependents = 0    
 
    # Initialize calculation variables for each worker
    regular_pay = 0.0
    overtime_pay = 0.0
   

    # Overtime Calculation structure (1.5x for hours over 40) 
    if hours_worked > 40:
        regular_pay = 40 * hourly_wage
        overtime_hours = hours_worked - 40
        overtime_pay = overtime_hours * (hourly_wage * 1.5)
    else:
        regular_pay =  hours_worked * hourly_wage
        overtime_pay = 0.0

    # correct Sequence Sequence
    total_gross_pay = regular_pay + overtime_pay 

    # Calculate Dependent Allowance reduction ($25 per dependent)
    dep_deduction = dependents * 25

    # Calculate pre-tax amount
    pre_tax_amount = total_gross_pay - dep_deduction
    if pre_tax_amount < 0:
        pre_tax_amount = 0.0

    # Calculate Taxes on pre-tax amounts (state 5.6%, Federal 7.9%)  
    state_tax = pre_tax_amount * 0.056
    federal_tax = pre_tax_amount * 0.079

    # Calculate Final Net Take-home Pay
    net_pay = pre_tax_amount - state_tax - federal_tax 
    if net_pay < 0:
        net_pay = 0.0

    # Save calculate data into list for our  Block 3 report writing
    gross_pay_list.append(total_gross_pay)
    state_tax_list.append(state_tax)
    federal_tax_list.append(federal_tax)
    dep_deduction_list.append(dep_deduction)
    net_pay_list.append(net_pay)
    print(f"employee: {employee_name}| Gross Pay: ${total_gross_pay:.2f} | Net Pay: ${net_pay:.2f}")

# =================================================================
#   BLOCK 3: WRITING DATA TO FILE 
# =================================================================
print("\n---BLOCK 3: Writing payroll report to file ---")
total_gross_pay_sum = sum(gross_pay_list)
total_state_tax_sum = sum(state_tax_list)
total_fed_tax_sum = sum(federal_tax_list)
total_net_sum = sum(net_pay_list)

output_file = open("payroll_report.txt", "w")
output_file.write("Name, ID, Gross Pay, Dep Deduction, State Tax, Fed Tax, Net Pay\n")
for i in range(total_employees):
    output_file.write(f"{employee_names[i]}, {employee_ids[i]},{gross_pay_list[i]:.2f},{dep_deduction_list[i]:.2f},{state_tax_list[i]:.2f},{federal_tax_list[i]:.2f},{net_pay_list[i]:.2f}\n")

output_file.write("--------------------------------------------------\n")
output_file.write(f"TOTALS,,{total_gross_pay_sum:.2f},,{total_state_tax_sum:.2f},{total_net_sum:.2f},{total_fed_tax_sum:.2f}\n")

output_file.close()
print("\nsuccess! your project ran perfectly.All 10 employees processed.")

