def hospital_years(initial_pop, growth_rate, years):
    # Check if growth rate leads to population decline
    valid = True
    message = ""

    if growth_rate < 1:
        message = "Growth rate cannot be less than 1 (negative population growth)"
        valid = False
    
    max_allowed_year = 100
    if years > max_allowed_year:
        message = f"Simulation years cannot exceed {max_allowed_year}"
        valid = False

    if not valid:
        print(message)
        return []
    # All checks passed, start simulation
    current_pop = initial_pop
    hospital_count = 1
    build_years = []

    for year in range(1, years + 1):
        current_pop = current_pop * growth_rate
        target_pop = hospital_count * 0.5
        if current_pop >= target_pop:
            build_years.append(year)
            hospital_count += 1
    return build_years

# Example function call
if __name__ == "__main__":
    result = hospital_years(2.5, 1.1, 25)
    print("Years to build new hospitals:", result)