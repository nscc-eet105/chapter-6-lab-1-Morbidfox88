#Chad Collard
#Chapter 6 Lab 1
#6/30/25

def calculate_weekly_sales():
    days_of_week = ("Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday")
    daily_sales = []

    print("Weekly Sales Calculator")

    for day in days_of_week:
        sale_amount = float(input(f"Enter sales for {day}: "))
        daily_sales.append(sale_amount)

    total_weekly_sales = sum(daily_sales)
    average_weekly_sales = total_weekly_sales / len(daily_sales) if daily_sales else 0

    print("\nWeekly Sales Summary:")
    print(f"Total Weekly Sales: ${total_weekly_sales:.2f}")
    print(f"Average Weekly Sales (Average Daily): ${average_weekly_sales:.2f}")

    # Find the day with the most sales
    max_sales = max(daily_sales)
    max_sales_index = daily_sales.index(max_sales)
    day_with_most_sales = days_of_week[max_sales_index]

    # Find the day with the least sales
    min_sales = min(daily_sales)
    min_sales_index = daily_sales.index(min_sales)
    day_with_least_sales = days_of_week[min_sales_index]

    print(f"Day with the Most Sales: {day_with_most_sales} (${max_sales:.2f})")
    print(f"Day with the Least Sales: {day_with_least_sales} (${min_sales:.2f})")

calculate_weekly_sales()
