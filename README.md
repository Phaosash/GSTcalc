<h1>GST Calculator – Extract GST from a Gross Amount</h1>
A simple, lightweight Python script that calculates the GST component of a GST-inclusive purchase price.
Ever received an invoice with a total amount and wanted to know how much of that total is GST versus the actual cost of the goods or services?
This little utility does exactly that!

Rather than adding GST to a net amount, this script works backwards from the gross (GST-inclusive) amount to calculate the GST component and the original net purchase price.

<h2>Features</h2>
Calculate GST: Extracts the GST component from a GST-inclusive amount.<br>
Calculate Net Amount: Determines the original purchase price before GST.<br>
Input Validation: Handles invalid user input and prompts for a valid number.<br>
Simple & Lightweight: No external dependencies or third-party packages required.<br>
Easy to Use: Just run the script, enter an amount, and get your breakdown.<br>

<h2>How It Works</h2>
In Australia, GST is generally calculated at a rate of 10%.
When an amount already includes GST, you cannot simply calculate 10% of the total to determine the GST component.
Instead, the GST component is extracted using the following formula:

<h3>GST Calculation:</h3>
python<br>
gst = gross_amount - (gross_amount / 1.10)

<h3>Net Amount Calculation:</h3>
python<br>
net = gross_amount - gst<br><br>

Where:<br>
gross_amount is the total invoice amount, including GST.
gst is the GST component of the total.
net is the original amount before GST was added.

<h2>Getting Started</h2>
<h4>Prerequisites</h4>
Python 3.x<br>
No additional libraries or dependencies required.

<h2>Example Usage</h2>
<h4>Input:</h4>
What was the purchase price of the item? 110.00

<h4>Output:</h4>
Total: $110.00<br>
GST: $10.00<br>
Net: $100.00<br>

<h2>Purpose:</h2>
This project was created as a small practical Python utility to solve a common everyday problem: identifying the GST component of an invoice when only the final GST-inclusive amount is available.
<br><br>
It's also a handy exercise in Python fundamentals, including:
Functions and code organisation<br>
Floating-point arithmetic<br>
User input handling<br>
Exception handling<br>
String formatting

<h2>Notes:</h2>
The calculator assumes a GST rate of 10%, as used in Australia.<br>
The entered amount must already include GST.<br>
Results are displayed to two decimal places.<br>

<h2>Disclaimer:</h2>
This is a basic calculator intended for straightforward GST calculations, not a substitute for formal accounting or tax advice.<br>

<h2>Future Improvements:</h2>
Some potential enhancements for future versions:
- Allow users to specify a different GST rate.<br>
- Support calculating GST on multiple invoice items.<br>
- Add command-line arguments to avoid interactive input.<br>
- Include automated unit tests.<br>
- Add support for calculating GST on GST-exclusive amounts.<br>

<h2>License</h2>
This project is open source. Feel free to use, modify, and improve it.<br>
