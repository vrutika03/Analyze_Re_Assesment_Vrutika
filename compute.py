# import sys

# def compute_values(threshold, limit):
#     output = []
#     cumulative_sum = 0.0

#     with open('input.txt', 'r') as file:
#         for line in file:
#             value = float(line.strip())
        
#             if value < threshold:
#                 transformed_value = 0.0
#             elif value > limit:
#                 transformed_value = limit
#             else:
#                 transformed_value = value
        
#             output.append(transformed_value)
#             cumulative_sum += transformed_value
#             sys.stdout.write(str(transformed_value) + "\n")
    
#     sys.stdout.write(str(cumulative_sum) + "\n")

# if __name__ == "__main__":
#     if len(sys.argv) != 3:
#         sys.stderr.write("Error: Two numerical arguments (threshold and limit) are required.\n")
#         sys.exit(1)
    
#     threshold = float(sys.argv[1])
#     limit = float(sys.argv[2])
    
#     compute_values(threshold, limit)


import sys

def compute_values(threshold, limit):
    output = []
    cumulative_sum = 0.0

    with open('input.txt', 'r') as file:
        for line in file:
            value = float(line.strip())

            if value < threshold:
                transformed_value = 0.0
            else:
                transformed_value = max(0.0, value - threshold)
                transformed_value = min(transformed_value, limit - cumulative_sum)

            output.append(transformed_value)
            cumulative_sum += transformed_value
            sys.stdout.write(f"{transformed_value:.1f}\n")

    sys.stdout.write(f"{cumulative_sum:.1f}\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        sys.stderr.write("Error: Two numerical arguments (threshold and limit) are required.\n")
        sys.exit(1)

    threshold = float(sys.argv[1])
    limit = float(sys.argv[2])

    compute_values(threshold, limit)
