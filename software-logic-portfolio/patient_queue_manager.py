# -*- coding: utf-8 -*-
"""
Created on Thu Sep  5 17:24:06 2024

@author: José Alberto Rocha Munguía
"""

"""
Hospital patient queue console demo (DSA coursework).

Interactive menu. Quick automated test:
  printf '1\\nAna\\n10:00am\\n3\\n2\\n4\\n' | python3 patient_queue_manager.py
  Expect add Ana, peek Ana, attend Ana, then exit.
"""


class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("The queue is empty, cannot dequeue.")
        return self.items.pop(0)

    def size(self):
        return len(self.items)

    def peek(self):
        if self.is_empty():
            return None
        return self.items[0]


class Patient:
    def __init__(self, name, arrival_time):
        self.name = name
        self.arrival_time = arrival_time


def main():
    queue = Queue()

    while True:
        print("1. Add patient")
        print("2. Attend next patient")
        print("3. View next patient")
        print("4. Exit")
        selection = input("Choose an option: ")

        if selection == "1":
            name = input("Enter patient name: ")
            arrival_time = input("Enter arrival time (e.g., 10:00am): ")
            patient = Patient(name, arrival_time)
            queue.enqueue(patient)
            print(f"Patient {name} added to the queue\n")

        elif selection == "2":
            if not queue.is_empty():
                patient = queue.dequeue()
                print(f"Patient {patient.name} attended\n")
            else:
                print("The queue is empty\n")

        elif selection == "3":
            patient = queue.peek()
            if patient:
                print(
                    f"Next patient to attend: {patient.name}, "
                    f"Arrival Time: {patient.arrival_time}\n"
                )
            else:
                print("No more patients in line\n")

        elif selection == "4":
            break

        else:
            print("Invalid option\n")


if __name__ == "__main__":
    main()
