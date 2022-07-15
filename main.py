import csv
import datetime


'''Name: Ioannis Ntoulis
   Student ID: 004124437 '''


# HashTable class using chaining
# Citation: (Dr. Tepe, C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code 2020)
class ChainingHashTable:
    # Constructor with optional initial capacity parameter.
    # Assigns all buckets with an empty list.
    # Space-time complexity -> O(1)
    def __init__(self, initial_capacity=10):
        # initialize the hash table with empty bucket list entries.
        # @param: initial_capacity , initialize the hashtable with.
        self.table = []
        for i in range(initial_capacity):
            self.table.append([])

    # Inserts a new item into the hash table.
    # Space-time complexity -> O(N)
    def insert(self, key, item):  # does both insert and update
        # get the bucket list where this item will go.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # update key if it is already in the bucket
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                kv[1] = item
                return True

        # if not, insert the item to the end of the bucket list.
        key_value = [key, item]
        bucket_list.append(key_value)
        return True

    # Searches for an item with matching key in the hash table.
    # Returns the item if found, or None if not found.
    # Space-time complexity -> O(N)
    def search(self, key):
        # get the bucket list where this key would be.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]
        # print(bucket_list)

        # search for the key in the bucket list
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                return kv[1]  # value
        return None

    # Removes an item with matching key from the hash table.
    # Space-time complexity -> O(N)
    def remove(self, key):
        # get the bucket list where this item will be removed from.
        bucket = hash(key) % len(self.table)
        bucket_list = self.table[bucket]

        # remove the item from the bucket list if it is present.
        for kv in bucket_list:
            # print (key_value)
            if kv[0] == key:
                bucket_list.remove([kv[0], kv[1]])


'''Class Package to initialize the class properties
@:param ID initialize the package id for each package in the class
@:param address initialize the package address
@:param city initialize the package city
@:param state initialize the package state
@:param zipCode initialize the package zip code
@:param delivery_time initialize the package delivery time
@:param weight initialize the package weight
@:param special_notes initialize the package special notes
'''


class Package:
    def __init__(self, ID, address, city, state, zipCode, delivery_time, weight, special_notes):
        self.ID = ID
        self.address = address
        self.city = city
        self.state = state
        self.zipCode = zipCode
        self.delivery_time = delivery_time
        self.weight = weight
        self.special_notes = special_notes
        self.status = ""
        self.time_leaves_the_hub = None

    def __str__(self):  # overwrite print(Package) otherwise it will print object reference
        return "%s, %s, %s, %s, %s, %s, %s, %s, %s" % (
            self.ID, self.address, self.city, self.state, self.zipCode, self.delivery_time, self.weight,
            self.special_notes, self.status)


'''
The function above is responsible for loading the file name when the program calls it. There were two parameters used;
first, there is the filename and the second is myHash, which is the ChainingHashTable() I created. The function assigns 
the appropriate column from the CSV file to each package in the package data. The next step is to create a 
package object, which is then inserted into the hashTable using the parameters that were provided. 
Space-time complexity -> 0(N)
 '''


def loadPackageData(fileName, myHash):
    with open(fileName) as package_file:
        packageData = csv.reader(package_file, delimiter=',')
        next(packageData)  # skip header
        for package in packageData:
            pID = int(package[0])
            pAddress = package[1]
            pCity = package[2]
            pState = package[3]
            pZip = package[4]
            pDelivery_time = package[5]
            pWeight = package[6]
            pStatus = "In Hub"

            # package object
            p = Package(pID, pAddress, pCity, pState, pZip, pDelivery_time, pWeight, pStatus)

            # insert it into the hash table
            myHash.insert(pID, p)


# Hash table instance
myHash = ChainingHashTable()

# Load packages to Hash Table
loadPackageData('/Users/admin/Desktop/Package_File.csv', myHash)


'''Class Truck to initialize the class properties
@:param capacity initialize the capacity for each truck and it sets the number of packages a truck can carry
@:param speed initialize the truck's speed and it sets the speed at 18 mph as per instructions
@:param loaded initialize a boolean, if the truck is loaded or not
@:param packages initialize a list for the packages that any truck can carry
'''


class Truck:
    def __init__(self, capacity=16, speed=18, loaded=True, packages=[]):
        self.capacity = capacity
        self.speed = speed
        self.loaded = loaded
        self.packages = packages


'''
Create three different objects for truck1, truck2, truck3
I loaded the trucks manually
There are fifteen packages on the truck1.  The majority of these packages are those that need to be delivered by
10:30 a.m, or packages that have a zip code near the packages with a delivery requirement
The second truck is loaded with fourteen packages; this truck will depart the hub at 9:10 in order to await packages
that have been delayed by the flight, and it also carries packages that have constraints, such as this package must be
transported in truck 2, etc.
The third truck carries packages that are free from constraints and contains package nine, for which a driver knows 
the wrong address at 10:20 a.m. The truck will leave the hub at 11:00 a.m.
'''
truck1 = Truck(16, 18, True, [1, 4, 6, 13, 15, 19, 20, 25, 29, 30, 37, 40, 38, 3, 8])
truck2 = Truck(16, 18, True, [2, 7, 10, 12, 14, 16, 17, 18, 21, 24, 28, 31, 32, 34])
truck3 = Truck(8, 18, True, [5, 11, 22, 23, 26, 27, 33, 35, 36, 39, 9])

# initialize a list to store the data from the appropriate CSV file for the distances between different addresses
distanceData = []

'''
using this function to load the distance file and append each row in the addressData list
Space-time complexity 0(N)
'''


def load_distance_data(filename):
    with open(filename) as csvfile_1:
        distance_csv = list(csv.reader(csvfile_1, delimiter=','))
        for distance in distance_csv:
            distanceData.append(distance)
        return distanceData


# initialize a list to store the data from the appropriate CSV file for the addresses
addressData = []

'''
using this function to load the address file and append each row in the addressData list
Space-time complexity 0(N)
'''


def load_address_data(filename):
    with open(filename) as csvfile_2:
        distance_name_csv = csv.reader(csvfile_2, delimiter=',')
        for row in distance_name_csv:
            addressData.append(row[0])
        return addressData


# Call the function and pass the path for the distance csv file as an argument
load_distance_data('/Users/admin/Desktop/Distance_InNumbers.csv')
# Call the function and pass the path for the address csv file as an argument
load_address_data('/Users/admin/Desktop/Distance_Address.csv')

'''
Using this function to calculate the distance between two specific addresses.
The function uses two arguments, address1 and address2. I named two variables h and j to store the appropriate address.
h is used for each row in the file and j is used for each column. With the if statement I checked if the position in the
 list is empty to return me the appropriate value, else it will return the value that it's not empty.
 Space-time complexity -> 0(N)
'''


def distance_in_between(address1, address2):
    vReturn = 0
    h = addressData.index(address1)
    j = addressData.index(address2)
    if distanceData[h][j] == '':
        vReturn = distanceData[j][h]
    else:
        vReturn = distanceData[h][j]
    return float(vReturn)


'''
Using this function to calculate the minimum distance for a package between two addresses. I checked for each package in
 the packages using a look up function from the hashtable that I created, and then I found the distance using the 
 previous function (distance_in_between()). I passed as arguments the address that the package leaves and the package
  address. Everytime the distance is less than the minn that I set it to 1000, then the minn will be the shortest 
  distance and the minimum distance package id will be now the package id that I need.
 Space-time complexity -> 0(N)
'''


def min_distance_from_address(address, packages):
    minn = 1000
    for pack_id in packages:
        package = myHash.search(pack_id)
        distance = distance_in_between(address, package.address)
        if distance < minn:
            minn = distance
            minPackageID = package.ID
    return minPackageID, minn


'''
Using this function to deliver the packages. The function uses two arguments, the truck that will leave the hub and the
time that the truck will leave the hub. I convert every String time to timedelta and I initialize the miles to zero, and 
the current address as 4001 South 700 East.I used two loops for this function, the first one to iterate through the
 packages and I looked up for the package id in the hashtable. Then I used a timedelta time object for the time the 
 package leaves the hub. In the second loop, I iterated in the packages and this time I computed the package id that 
 it's being delivered, and the distance that the truck has travelled. More calculations needed for the miles, the
  delivery time, and using the look up function for the delivered package. I set up again the timedelta, the delivery
   status, and for the second iteration I set up the package delivered address as current address. After this process, I
   remove the delivered package from the truck packages and the function returns the miles that the truck has travelled.
 Space-time complexity -> 0(N^2)
'''


def delivering_packages(truck, startTime):
    h, m, s = startTime.split(":")
    time_object = datetime.timedelta(hours=int(h), minutes=int(m), seconds=int(s))
    current_truck_address = '4001 South 700 East'
    miles = 0
    for pack_id in truck.packages[:]:
        package_in_hub = myHash.search(pack_id)
        package_in_hub.time_leaves_the_hub = time_object
    for pack_id in truck.packages[:]:
        id_delivered, distance_traveled = min_distance_from_address(current_truck_address, truck.packages)
        miles = miles + distance_traveled
        delivery_time = (distance_traveled / 18) * 60 * 60
        dts = datetime.timedelta(seconds=delivery_time)
        time_object = time_object + dts
        package_delivered = myHash.search(id_delivered)
        package_delivered.delivery_time = time_object
        package_delivered.status = 'Delivered'
        current_truck_address = package_delivered.address
        truck.packages.remove(id_delivered)
    return miles


# miles per truck, using the delivering packages function. I used as arguments each truck and the starttime that
# I want the trucks to leave the hub.
t1 = delivering_packages(truck1, '08:00:00')
t2 = delivering_packages(truck2, '09:10:00')
t3 = delivering_packages(truck3, '11:00:00')

# total miles for the sum of the three trucks
total_miles = t1 + t2 + t3

# Space-time complexity -> O(N^2) + 3 O(N)
# This is the display message that a user can see when runs the program.
if __name__ == '__main__':
    print('*******************************************************')
    print('WGUPS Routing Application!')
    print('*******************************************************')

    # loop until user is satisfied
    # Space-time complexity -> O(N)
    isExit = True
    while isExit:
        print("\nOptions:")
        print('1. Get the total mileage of all trucks.')
        print("2. View the status and info of any package at any time")
        print("3. Exit the Program")
        option = input("Chose an option (1,2, or 3): ")
        # Space-time complexity -> O(N)
        if option == "1":
            print(f'Route was completed in {total_miles:.2f} miles.\n')
        # Space-time complexity -> O(N)
        elif option == "2":
            checkTime = input("Please enter a time in the form '00:00:00 : ")
            hour, mint, secd = checkTime.split(':')
            rTime = datetime.timedelta(hours=int(hour), minutes=int(mint), seconds=int(secd))
            print('Package Status')
            # Space-time complexity -> O(N^2)
            for n in range(1, 41):
                p = myHash.search(n)
                dTime = p.delivery_time
                time_left_hub = p.time_leaves_the_hub
                if rTime < time_left_hub:
                    print('Package ID:', p.ID, ',', 'Address:', p.address, ',', 'City:', p.city, ',', 'State:', p.state,
                          ',', 'Zip Code:', p.zipCode, ',', 'Weight:', p.weight, ',', 'At Hub')
                elif dTime <= rTime:
                    print('Package ID:', p.ID, ',', 'Address:', p.address, ',', 'City:', p.city, ',', 'State:', p.state,
                          ',', 'Zip Code:', p.zipCode, ',', 'Weight:', p.weight, ',', 'Delivery time:', p.delivery_time,
                          ',', 'Delivered')
                else:
                    print('Package ID:', p.ID, ',', 'Address:', p.address, ',', 'City:', p.city, ',', 'State:', p.state,
                          ',', 'Zip Code:', p.zipCode, ',', 'Weight:', p.weight, ',', "En Route")
        else:
            print("Program End")
            quit()

'''Resources

Tepe, C. (2020, November 17). C950 - Webinar-1 - Let’s Go Hashing - Complete Python Code. 
 https://wgu.hosted.panopto.com/Panopto/Pages/Viewer.aspx?id=f08d7871-d57a-496e-a6a1-ac7601308c71. 
 Retrieved July 12, 2022, from https://my.wgu.edu/
'''
