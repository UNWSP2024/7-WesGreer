# Population program
# Written by Wesley Greer on 3/6/2026
def main():
    print('''This program allows you to enter population data for different states for different years.
    When you are done entering population data, you can enter a year
    and it will display the total population for that year according to the data you entered.''')

# Allow the user to input population data and add it to a list
    population_data = []

    i = True
    while i == True:
        year = int(input("Enter year: "))
        state = input("Enter state name: ")
        population = int(input("Enter population: "))
        population_data.append([year, state, population])
        more_entries = input("Would you like to add another entry? (y=yes) ")
        if more_entries == 'y':
            pass
        else:
            i = False

    def sum_population_for_year():
        total_population = 0
        for entry in population_data:
            if entry[0] == y:
                total_population += entry[2]
            else: pass
        print('The total population for', y, 'is', total_population)

    # Now have the user enter a year.
    y = int(input('Enter a year to find the sum of the population for that year: '))
    sum_population_for_year()




# Call the main function.
if __name__ == '__main__':
    main()
