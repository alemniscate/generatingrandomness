import random

def count_quadruple(quadruple, zeroone):
    count = 0
    start = 0
    while True:
        index = zeroone.find(quadruple, start)
        if index == -1:
            break
        count += 1
        start = index + 1
        if start >= len(zeroone):
            break
    return count

def count_triad(triad, zeroone):
    return [count_quadruple(triad + "0", zeroone), count_quadruple(triad + "1", zeroone)]

def predict(testseq, triad_frequency):
    prediction = ""
    triad = ""
    for i in range(len(testseq)):
        if i < 3:
            addchar = random.choice("01")
            prediction += addchar
            triad += testseq[i]
        else:
            zero, one = triad_frequency[triad]
            addchar = "0" if zero >= one else "1"
            prediction += addchar 
            triad = triad[1:]
            triad += testseq[i] 
    return prediction

def analyze(testseq, prediction):
    correct = 0
    for i in range(3, len(testseq)):
        correct += 1 if testseq[i] == prediction[i] else 0
    size = len(testseq) - 3
    ratio = round(correct * 100 / size, 2)
    return correct, size, ratio

def check_seq(seq):
    for char in seq:
        if char not in ("0", "1"):
            return False
    return True

def get_seq():
    while True:
        print("Print a random string containing 0 or 1:")
        seq = input()
        if seq == "enough":
            return seq
        if not check_seq(seq):
            print()
            continue
        return seq


zeroone = ""
limit = 100

print("Please give AI some data to learn...")
print("The current data length is 0, 100 symbols left")

while True:
    print("Print a random string containing 0 or 1:")
    print()
    line = input()
    for char in line:
        if char == "0" or char == "1":
            zeroone += char
    if len(zeroone) >= limit:
        break
    print(f"Current data length is {len(zeroone)}, {limit - len(zeroone)} symbols left")
print()
print("Final data string:")
print(zeroone)
print()
print("You have $1000. Every time the system successfully predicts your next press, you lose $1.")
print("Otherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

triad_list = ["000", "001", "010", "011", "100", "101", "110", "111"]
triad_frequency = {}
for triad in triad_list:
    triad_frequency[triad] = count_triad(triad, zeroone)

print()
balance = 1000
while True:
    seq = get_seq()
    if seq == "enough":
        break
    print("prediction")
    prediction = predict(seq,triad_frequency)
    print(prediction)
    print()
    correct, size, ratio = analyze(seq, prediction)
    mistake = size - correct
    balance += mistake - correct
    print(f"Computer guessed right {correct} out of {size} symbols ({ratio} %)")
    print(f"Your capital is now ${balance}")
    print()

print("Game over!")


