# Dictionary to store challans
challan_records = []

# Rules and fines
traffic_rules = {
    "No Helmet": 500,
    "Signal Jump": 1000,
    "Over Speeding": 1500,
    "Drunk Driving": 5000,
    "No Seatbelt": 1000,
    "Using Mobile While Driving": 2000
}

# Function to file challan
def file_challan(name, vehicle_number, violation):
    if violation not in traffic_rules:
        print(f"Violation '{violation}' not recognized. Cannot file challan.")
        return

    challan = {
        "Name": name,
        "Vehicle Number": vehicle_number,
        "Violation": violation,
        "Fine": traffic_rules[violation]
    }
    
    challan_records.append(challan)
    print(f"Challan filed successfully for {name} - ₹{traffic_rules[violation]} fine for '{violation}'.")

# Function to show all challans
def show_all_challans():
    if not challan_records:
        print("No challans filed yet.")
        return

    print("\n--- All Challans Filed ---")
    for idx, challan in enumerate(challan_records, 1):
        print(f"{idx}. Name: {challan['Name']}, Vehicle: {challan['Vehicle Number']}, "
              f"Violation: {challan['Violation']}, Fine: ₹{challan['Fine']}")

# Example Usage
file_challan("Sameer Ahmed", "TS09AB1234", "No Helmet")
file_challan("Rahul Verma", "AP11CD5678", "Over Speeding")
file_challan("Ayesha Khan", "MH20EF2468", "Using Mobile While Driving")

show_all_challans()
