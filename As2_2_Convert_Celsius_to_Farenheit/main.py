def main():
    """
    This program converts Celsius temperatures to Fahrenheit temperatures. 
    """

    celsius = float(input("Enter the temperature in Celsius: "))
    fahrenheit = 9/5 * celsius + 32

    print(f'The temperature in Fahrenheit is {fahrenheit:.2f} degrees.')
    return celsius, fahrenheit

if __name__ == '__main__':
    main()
