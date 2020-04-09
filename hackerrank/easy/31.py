"""
Task

Raghu is a shoe shop owner. His shop has X number of shoes.
He has a list containing the size of each shoe he has in his shop.
There are N number of customers who are willing to pay Xi amount of money only if they get the shoe of their desired size.

Your task is to compute how much money Raghu earned.

Input Format

The first line contains X, the number of shoes.
The second line contains the space separated list of all the shoe sizes in the shop.
The third line contains N, the number of customers.
The next N lines contain the space separated values of the shoe size desired by the customer and Xi, the price of the shoe.
"""


from collections import Counter

shoes = int(input())
list_sizes = Counter(map(int, input().split()))
customers = int(input())

money = 0
for i in range(customers):
    size, price = map(int, input().split())
    if list_sizes[size]:
        money += price
        list_sizes[size] -= 1
print(money)