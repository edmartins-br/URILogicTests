# In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1, the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

# Input
# The input file contains two lines of data. In each line there will be 3 values: two integers and a floating value with 2 digits after the decimal point.

# Output
# The output file must be a message like the following example where "Val12or a pagar" means Value to Pay. Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

p1_Code, p1_Units, p1_Price = input().split(' ')

p1_Code = int(p1_Code)
p1_Units = int(p1_Units)
p1_Price = float(p1_Price)

p2_Code, p2_Units, p2_Price = input().split(' ')

p2_Code = int(p2_Code)
p2_Units = int(p2_Units)
p2_Price = float(p2_Price)

finalPrice = ((p1_Units * p1_Price) + (p2_Units * p2_Price))

print("VALOR A PAGAR: R$ {:.2f}".format(finalPrice))
