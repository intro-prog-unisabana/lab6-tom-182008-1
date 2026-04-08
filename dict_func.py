# Write your code here!
def employee_print(employee_info):
    info_copy = employee_info.copy()
    
    required_keys = ["Name", "Salary", "Role"]
    
    for key in required_keys:
        value = info_copy.pop(key, "N/A")
        print(f"{key}: {value}")
    
    if not info_copy:
        print("No other info!")
    else:
        for key, value in info_copy.items():
            print(f"{key}: {value}")
