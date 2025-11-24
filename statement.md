# **Problem Statement:** 

# **Automated Pizza Billing System**



## **Problem Statement**

A fast-food pizza outlet requires a digital solution to streamline their billing process. Currently, manual calculations for custom orders (varying sizes and multiple toppings) are prone to human error and slow down customer service. The goal is to build a robust Command Line Interface (CLI) tool to automate this workflow.



---



## **Objective**

Develop a Python program that functions as a "Self-Service Kiosk" or a "Cashier Terminal." The system must allow users to select a base pizza size, add multiple toppings, and generate a final itemized bill in Indian Rupees (INR).



---



## **Target User**

fast-food pizza outlet owners

small restaurants owners



**---**



## **Features**



#### **1. Data Structures**

The system utilizes Python dictionaries to store inventory and pricing:

* **Pizza Sizes**: Small (₹99), Medium (₹199), Large (₹299), Family (₹499).
* **Toppings**: Capsicum, Mushrooms, Onions, Olives, Corn, Extra Cheese, Jalapeno (Prices range from ₹20 to ₹40).



#### **2. User Interaction**

Size Selection: The user is prompted to select a pizza size. The system then validates this input; if the size is invalid, its prompted again.

**Topping Selection**: The user should be able to add toppings one by one. The system must continue asking for toppings until the user types a termination command (e.g., "done").

**Case Insensitivity**: The system handles the inputs gracefully regardless of case (e.g., "Small", "small", "SMALL" all work).



#### **3. Calculation Logic**

* &nbsp;The base price is determined by the pizza size.
* &nbsp;Every added topping increases the total cost.
* &nbsp;The final total is calculated dynamically as items are added.



#### **4. Output Generation**

Upon completion of the order, the system displays an Itemized Receipt containing:

* Selected Pizza Size and Base Price.
* List of all added toppings with individual prices.
* A "Total Price" summary formatted to two decimal places (e.g., ₹269.00).



---

## 

## **Constraints \& Edge Cases**

* **Invalid Inputs**: The program must not crash if the user enters a size or topping that does not exist. It should display an error message and allow the user to try again.
* **Currency Formatting**: All monetary values must be displayed with the Rupee symbol (₹).



---



# **Sample Use Case**



#### **Scenario:**

A customer orders a "Medium" pizza and adds "Corn" and "Extra Cheese".

##### 

##### **Expected Logic Flow:**

1\. Base Cost = 199.00

2\. Add Corn (+30.00) -> Subtotal = 229.00

3\. Add Extra Cheese (+40.00) -> Subtotal = 269.00

4\. User types "done".

5\. Print Receipt showing ₹269.00 total.

