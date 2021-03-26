big_data = open('intro_python\\life-expectancy\\life-expectancy.csv', 'r')

year = str(input('Write an year between 1751 to 2019: '))

#variables
overall_highest = "0"
overall_lowest = "100"
highest_life_expectancy = "0"
lowest_life_expectancy = "100"
i = 0
country_overall_highest = ""
country_overall_lowest = ""
year_overall_highest = ""
year_overall_lowest = ""
country_lowest = ""
country_highest = ""
data_list = []
average = 0
sum = 0

with big_data as data:
    for line in data:
        i += 1
        if i == 1:
            continue
        item = line.strip()
        item = item.split(',')  
        if float(item[-1]) > float(overall_highest):
            overall_highest = item[-1]
            country_overall_highest = item[0]  
            year_overall_highest = item[-2]
        if float(item[3]) < float(overall_lowest):
            overall_lowest = item[-1]
            country_overall_lowest = item[0]
            year_overall_lowest = item[-2]
        if item[2] == year:
            data_list.append(line)
            sum += float(item[-1]) 
            if float(item[-1]) > float(highest_life_expectancy):
                highest_life_expectancy = item[-1]
                country_highest = item[0]
            if float(item[-1]) < float(lowest_life_expectancy):
                lowest_life_expectancy = item[-1]
                country_lowest = item[0]
if len(data_list) < 1:
    print()
    print("We don't have data about that year")   
    print()
else:
    average = sum/len(data_list)
    print()
    print(f"The overall max life expectancy is: {float(overall_highest):.2f} from {country_overall_highest} in {year_overall_highest} ")
    print(f"The overall min life expectancy is: {float(overall_lowest):.2f} from {country_overall_lowest} in {year_overall_lowest}")

    print()
    print(f"For the year {year}:")
    print(f" The average of all countries is: {average:.2f}")
    print(f' The max life expectancy is: {float(highest_life_expectancy):.2f} from {country_highest}')
    print(f' The min life expectancy is: {float(lowest_life_expectancy):.2f} from {country_lowest}')

    print()

country = str(input('Write a country: '))
data_list2 = []
i = 0
j = 0
sum = 0
average = 0
highest_life_expectancy = "0"
lowest_life_expectancy = "100"
last_year_expectancy = 0
last_year = ""
year = ""
higher_percentage = 0
highest_year = ""
lowest_year = ""
big_data = open('intro_python\\life-expectancy\\life-expectancy.csv', 'r')
with big_data as data:
    for line in data:
        i += 1
        if i == 1:
            continue
        item = line.strip()
        line = line.strip()
        item = item.split(',') 
        if item[0].lower() == country.lower():
            j += 1
            data_list2.append(item[-2])
            sum += float(item[-1]) 
            if float(item[3]) > float(highest_life_expectancy):
                highest_life_expectancy = item[-1]
                highest_year = item[-2]
            if float(item[3]) < float(lowest_life_expectancy):
                lowest_life_expectancy = item[-1]
                lowest_year = item[-2]
            if j < 2:
                last_year_expectancy = float(item[-1])
            percentage = float(item[-1])/last_year_expectancy 
            percentage = (abs(1-percentage))*100
            if percentage > higher_percentage:
                higher_percentage = percentage
                year = item[-2]
                if j >= 2:
                    last_year = data_list2[-2]
            last_year_expectancy = float(item[-1])
if len(data_list2) < 1:  
    print()
    print("That country doesn't exist in the data")   
    print()
else:
    average = sum/len(data_list2)
    print()
    print(f"For the country {country.capitalize()}:")
    print(f" The average of all years is: {average:.2f}")
    print(f' The max life expectancy is: {float(highest_life_expectancy):.2f} from {highest_year}')
    print(f' The min life expectancy is: {float(lowest_life_expectancy):.2f} from {lowest_year}')
    print(f" The higher percentage difference between two consecutives years is: {higher_percentage:.2f}% between the years {year} and {last_year}")
    print()