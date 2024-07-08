#!/usr/bin/python3

#prompt user to enter products bought by the customer
def store_product_details(product_details, product, price,quantity):
	product_details[product] = [price, quantity]

def totals_for_all_products(product_details):
	# cost of each product (price*quantity)
	total_for_each_product = [
		int(value[0]) * int(value[1]) for value in product_details.values()
		]
	return sum(total_for_each_product)

def generate_shopping_summary(product_details):
    for product, cost in product_details.items():
        total_cost_each_product = int(cost[0]) * int(cost[1])
        print(product, total_cost_each_product)

def main():
	# stores product details
	product_details = {}
	# Prompt User for input
	print(
	    "+--------------------------------------+\n"
	    "| Enter product details                |\n"
	    "|     Enter 'q' to quit()              |\n"
	    "+--------------------------------------+"
	)
	while True:
		product = input("Product name: ")
		if product.lower() == 'q':
			break
		price = input("Price: ")
		if price.lower() == 'q':
			break
		quantity = input("quantity(kg): ")
		if quantity.lower() == 'q':
			break
		store_product_details(product_details, product, price,quantity)

	generate_shopping_summary(product_details)

	#print("\n----------------------------------------")
	#print(f"TOTALS: {totals_for_all_products(product_details)}")
    

if __name__ == '__main__':
    main()


