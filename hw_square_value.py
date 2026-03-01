def square_it_out(start, end):
    numbers = list(range(start, end + 1))
    squares = [n**2 for n in numbers]
    even_squares = [sq for sq in squares if sq % 2 == 0]
    odd_squares = [sq for sq in squares if sq % 2 != 0]
    print("Original numbers:", numbers)
    print("Squares:", squares)
    print("Even squares:", even_squares)
    print("Odd squares:", odd_squares)
square_it_out(1, 10)