try:
    file = open('city.txt', 'r')
    print("all city ditels")

    for line in file:
        city, population = line.strip().split(',')
        print(f"City: {city}, Population: {population}")
        file.close()

        file = open('city.txt', 'r')
        print("City with population greater than 1 million:")
        file.close()

        file = open('city.txt', 'r')
        print("City with population less than 1 million:")

        if float(population) < 1000000:
            print(line)

        file.close()
        except FileNotFoundError:
        print("File not found. Please check the file name and try again.")