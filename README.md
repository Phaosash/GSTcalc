GST Calculator – Extract GST from a Gross Amount

A simple, lightweight Python script that calculates the GST component of a GST-inclusive purchase price.
Ever received an invoice with a total amount and wanted to know how much of that total is GST versus the actual cost of the goods or services?
This little utility does exactly that!

Rather than adding GST to a net amount, this script works backwards from the gross (GST-inclusive) amount to calculate the GST component and the original net purchase price.

Features
Calculate GST: Extracts the GST component from a GST-inclusive amount.
Calculate Net Amount: Determines the original purchase price before GST.
Input Validation: Handles invalid user input and prompts for a valid number.
Simple & Lightweight: No external dependencies or third-party packages required.
Easy to Use: Just run the script, enter an amount, and get your breakdown.

How It Works

In Australia, GST is generally calculated at a rate of 10%.
When an amount already includes GST, you cannot simply calculate 10% of the total to determine the GST component.
Instead, the GST component is extracted using the following formula:

GST Calculation:

python
gst = gross_amount - (gross_amount / 1.10)

Net Amount Calculation:
python
net = gross_amount - gst


Where:
gross_amount is the total invoice amount, including GST.
gst is the GST component of the total.
net is the original amount before GST was added.


Getting Started
Prerequisites
Python 3.x
No additional libraries or dependencies required.

Example Usage


Input:

text
What was the purchase price of the item? 110.00


Output:

text
Total: $110.00
GST: $10.00
Net: $100.00


Another example using a less straightforward amount:

Input:

text
What was the purchase price of the item? 275.00


Output:

text
Total: $275.00
GST: $25.00
Net: $250.00


Purpose:
This project was created as a small practical Python utility to solve a common everyday problem: identifying the GST component of an invoice when only the final GST-inclusive amount is available.

It's also a handy exercise in Python fundamentals, including:

Functions and code organisation
Floating-point arithmetic
User input handling
Exception handling
String formatting

Notes:
The calculator assumes a GST rate of 10%, as used in Australia.
The entered amount must already include GST.
Results are displayed to two decimal places.
This is a basic calculator intended for straightforward GST calculations, not a substitute for formal accounting or tax advice.

Future Improvements:

Some potential enhancements for future versions:
- Allow users to specify a different GST rate.
- Support calculating GST on multiple invoice items.
- Add command-line arguments to avoid interactive input.
- Include automated unit tests.
- Add support for calculating GST on GST-exclusive amounts.

License
This project is open source. Feel free to use, modify, and improve it.
If you find this little utility useful, feel free to ⭐ the repository!
