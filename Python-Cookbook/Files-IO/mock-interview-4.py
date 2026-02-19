#Scenario: You have a list of 1,000 latencies. How do you find the 99th percentile? The "Interviewer-Sought" Answer:
#Sort the list: latencies.sort()
#Calculate the index: index = int(len(latencies) * 0.99) - 1
#Return the value: return latencies[index]

def calculate_99th_percentile(latencies):
    if not latencies:
        return None  # Handle empty list case

    # Step 1: Sort the list
    latencies.sort()

    # Step 2: Calculate the index for the 99th percentile
    index = int(len(latencies) * 0.99) - 1

    # Step 3: Return the value at that index
    return latencies[index]

# Example usage
latencies = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
percentile_99 = calculate_99th_percentile(latencies)
print(f"99th Percentile Latency: {percentile_99} ms")