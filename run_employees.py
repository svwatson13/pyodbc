while True:
    print('\nchoose 1 for getting all employees ')
    print('choose 2 for getting 1 employee by ID')
    print('choose 3 for getting 1 product by name')
    print('choose 4 for top 10 products by unitprice')
    print('choose 5 for bottom 10 products by unitprice')
    print('choose 6 to exit ')
    user_input = input('Choose 1, 2, 3, 4, 5 or 6 ').strip()
    if user_input == '1':
        print('getting all products')
        time.sleep(2)
        products = NWProducts().print_all()
        print(products)

    elif user_input == '2':
        products = NWProducts().read_one_ID()
        print('getting 1 product')
        time.sleep(1)
        print(products.fetchone())
        time.sleep(3)
    elif user_input == '3':
        products = NWProducts().read_one_product_name()
        print('getting 1 product')
        time.sleep(1)
        print(products.fetchone())
        time.sleep(3)
    elif user_input == '4':
        print('getting top 10')
        products = NWProducts().top_10_price()
        print(products)
    elif user_input == '5':
        print('getting bottom 10')
        products = NWProducts().bottom_10_price()
        print(products)
    elif user_input == '6':
        print('goodbye')
        break
    else:
        print('Not a valid response')
        continue