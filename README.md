# factorial-digits
Corigine Assignment - Recruitment

Write a program to calculate the sum of any parsed factorial’s digits

For factorial, 𝑛! means 𝑛 × (𝑛 − 1) × (𝑛 − 2) ⋯ 3 × 2 × 1
For example, 10! = 10 × 9 × 8 ⋯ 3 × 2 × 1 = 3628800
Finding the sum of all the digitals for 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

- Used NumPy to calculate factorial of number
- Factorial result (n) stored into array x with last digit as first element (x[0]) of array x and first digit as last element of array x
- E.g. for Factorial 8! = 40320, array x would be as follows x = [0,2,3,0,4]
- Used .append python function to add elements to array

Task completed by using while loop which quits when whole factorial result been considered and captured into array
- appends n % 10 to first element of array (Least significant digit in factorial result n)
- n//=10 is computed which floors n by 10 to create new number with the 2nd least significant digit being the new least significant digit in the new loop (iteration)
- error checking: while n>10 (whole factorial result n hasn't been considered)
- process repeats until while loop case not satisfied

Sum of array elements computed using NumPy to get result

The sum of any parsed factorial’s digits successfully calculated

Sample Output:

>> $ docker run --rm -i factorial digits
10 [ENTER]
27
>> $ docker run --rm -i factorial digits
100 [ENTER]
648

INSTALL Dockerfile dockerfile1 which contains commands to create dockerfile image factorial-digits
PYTHON File: factorial-digits.py




