def main():
    """
    Calculate and display the sales price.
    Input is the regular price and discount rate of the item.
    """
    
    original_price = int(input('Enter the regular price: '))
    rate = int(input('Enter the discount rate: '))

    discount_amount = original_price*rate/100
    final_price = original_price - discount_amount

    print(f'Regular Price: {original_price}')
    print(f'Discount Amount: {discount_amount}')
    print(f'Final Price: {final_price}')

    return original_price, discount_amount, final_price


if __name__ == '__main__':
    main()
