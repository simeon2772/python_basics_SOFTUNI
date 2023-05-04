start_number = int(input())
end_number = int(input())

for i in range(start_number, end_number + 1):
    current_number_str = str(i)
    even_sum = 0
    odd_sum = 0
    for symbol_count in range(0, len(current_number_str)):
        digit = int(current_number_str[symbol_count])
        if symbol_count % 2 == 0:
            even_sum += digit
        else:
            odd_sum += digit
    if even_sum == odd_sum:
        print(current_number_str, end=" ")
