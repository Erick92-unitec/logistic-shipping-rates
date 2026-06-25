def calculate_shipping_rate(weight_kg, distance_km):
    base_rate = 5.00
    weight_rate = weight_kg * 1.25
    distance_rate = distance_km * 0.05

    total_rate = base_rate + weight_rate + distance_rate
    return round(total_rate, 2)


if __name__ == "__main__":
    weight = float(input("Enter package weight in kg: "))
    distance = float(input("Enter shipping distance in km: "))

    rate = calculate_shipping_rate(weight, distance)
    print(f"Estimated shipping rate: ${rate}")
