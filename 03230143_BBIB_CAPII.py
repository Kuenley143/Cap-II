import tkinter as tk
from tkinter import ttk, messagebox

class IncomeTaxForm(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Income Tax Form")
        self.geometry("400x600")

        self.create_widgets()

    def create_widgets(self):
        # Create a canvas to allow scrolling
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)

        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )

        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        self.add_form_fields()
        
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

    def add_form_fields(self):
        fields = [
            "Monthly Basic Salary Allowances",
            "Fees & Remuneration",
            "Bonus",
            "Commission",
            "Leave Encashment",
            "Share of Profits Received by an Employee",
            "Consultancy Income by a Non-Licensed Consultant",
            "Other Benefits Received",
            "Rental Income",
            "Maintenance Cost on Rental 30%",
            "Dividend Income",
            "Dividend Specific Deductions",
            "Other Income",
            "Other Income Specific Deduction",
            "Education Deductions",
            "Donations",
            "Life Insurance Premium"
        ]

        self.entries = {}

        for field in fields:
            label = ttk.Label(self.scrollable_frame, text=field)
            label.pack(padx=10, pady=5, anchor="w")
            entry = ttk.Entry(self.scrollable_frame)
            entry.pack(padx=10, pady=5, anchor="w", fill="x")
            self.entries[field] = entry

        submit_button = ttk.Button(self.scrollable_frame, text="Calculate Tax Payable Income", command=self.calculate_tax_payable_income)
        submit_button.pack(pady=20)

        self.result_label = ttk.Label(self.scrollable_frame, text="")
        self.result_label.pack(pady=20)

    def calculate_tax_payable_income(self):
        try:
            # Retrieve values from entries and convert to float
            values = {field: float(entry.get() or 0) for field, entry in self.entries.items()}

            # Debugging: print the retrieved values
            print("Retrieved values:", values)

            # Calculate the Tax Payable Income
            tax_payable_income = (
                values["Monthly Basic Salary Allowances"] * 12
                + values["Fees & Remuneration"]
                + values["Bonus"]
                + values["Commission"]
                + values["Leave Encashment"]
                + values["Share of Profits Received by an Employee"]
                + values["Consultancy Income by a Non-Licensed Consultant"]
                + values["Other Benefits Received"]
                + values["Rental Income"]
                - values["Maintenance Cost on Rental 30%"]
                + values["Dividend Income"]
                - values["Dividend Specific Deductions"]
                + values["Other Income"]
                - values["Other Income Specific Deduction"]
                - values["Education Deductions"]
                - values["Donations"]
                - values["Life Insurance Premium"]
            )

            # Debugging: print the calculated tax payable income
            print("Tax Payable Income:", tax_payable_income)

            self.result_label.config(text=f"Tax Payable Income: {tax_payable_income:.2f}")

            # Calculate the tax using the tax calculation function
            tax = calculate_tax(tax_payable_income)
            
            # Debugging: print the calculated tax
            print("Calculated Tax:", tax)

            self.show_tax_popup(tax)
        except ValueError as e:
            print("Error:", e)
            self.result_label.config(text="Please enter valid numbers in all fields.")

    def show_tax_popup(self, tax):
        if tax <= 0:
            messagebox.showinfo("Payable tax", "You dont have to pay tax since your yearly income does not exceed Nu.300,000")
        elif tax > 0:
            messagebox.showinfo("Payable Tax", f"Your Payable Tax is Nu. {tax:.2f}")

def calculate_tax(income):
    if income <= 300000:
        tax = 0
    elif income <= 400000:
        tax = (income - 300000) * 0.10
    elif income <= 650000:
        tax = 10000 + (income - 400000) * 0.15
    elif income <= 1000000:
        tax = 35500 + (income - 650000) * 0.20
    elif income <= 1500000:
        tax = 80500 + (income - 1000000) * 0.25
    else:
        tax = 195500 + (income - 1500000) * 0.30

    return tax

if __name__ == "__main__":
    app = IncomeTaxForm()
    app.mainloop()
