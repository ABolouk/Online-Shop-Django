def price_discount(price, discount):
    final_price = price
    if discount:
        amount, price = int(discount.amount), int(price)
        try:
            max_value = int(discount.max_value)
        except:
            max_value = 0
        if discount.type == "PER":
            profit = int(price * amount / 100)
            final_price = str((price - profit) if not max_value else (price - min(max_value, profit)))
        else:
            final_price = str((price - amount) if (price >= amount) else 0)
    return final_price
