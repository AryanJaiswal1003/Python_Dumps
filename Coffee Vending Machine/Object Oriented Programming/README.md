## Coffee Machine Project

This is a simple **Python console-based Coffee Machine simulation** built using **Object-Oriented Programming (OOP)**.
It allows a user to order drinks, processes payment, checks resources, and provides reports — just like a real coffee machine!

---

## Features

* Order drinks: **Espresso, Latte, Cappuccino**
* Resource management: tracks **water, milk, coffee**
* Payment system: simulates money insertion and validates transactions
* Machine reports: check available resources
* Shutdown option: turn the coffee machine off

---

## OOP Concepts Used

This project demonstrates **fundamental OOP principles**:

* **Encapsulation** → Each class (`Menu`, `CoffeeMaker`, `MoneyMachine`) encapsulates its own data and methods.
* **Abstraction** → Users only interact with simple methods like `.make_coffee()` or `.make_payment()` without knowing internal details.
* **Modularity** → Different classes handle different responsibilities, making the project clean and organized.
* **Reusability** → Classes can be reused or extended to add more drinks, payment options, or machine features.

---

## Usage Commands

* Enter `espresso`, `latte`, or `cappuccino` → to order a drink
* Enter `report` → to check the current resources
* Enter `off` → to turn off the machine