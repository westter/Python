class CityPopulationInsights:
    def __init__(self):
        self.cities = [
            ("Paris", "France", 2148327),
            ("Lagos", "Nigeria", 9000000),
            ("Tokyo", "Japan", 13929286),
            ("Reykjavik", "Iceland", 128793),
            ("New York", "USA", 8419000),
            ("Los Angeles", "USA", 3980400),
            ("London", "UK", 8982000),
            ("Beijing", "China", 21540000),
            ("Sydney", "Australia", 5312163),
            ("Moscow", "Russia", 11920000),
            ("Cairo", "Egypt", 10230350),
        ]

    def highestPopulation(self):
        highest = 0
        for city in self.cities:
            if city[2] > highest:
                highest = city[2]
        return highest

    def smallestPopulation(self):
        smallest = self.cities[0][2]
        for city in self.cities:
            if city[2] < smallest:
                smallest = city[2]
        return smallest

    def averagePopulation(self):
        total = 0
        for city in self.cities:
            total += city[2]

        return total/len(self.cities)

population_insights = CityPopulationInsights()

print("Highest Population:", population_insights.highestPopulation())
print("Smallest Population:", population_insights.smallestPopulation())
print("Average Population:", population_insights.averagePopulation())

#outpust
#Highest Population: 21540000
#Smallest Population: 128793
#Average Population: 8690029.0
