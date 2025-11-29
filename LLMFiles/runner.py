
cutoff = 46059

with open("demo-audio-data.csv", "r") as f:
    content = f.read()

numbers = [int(line.strip()) for line in content.splitlines() if line.strip()]

filtered_numbers = [num for num in numbers if num > cutoff]

answer = sum(filtered_numbers)

print(answer)
