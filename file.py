file = open("data.txt", "w", encoding="utf8")
file.write("1. 스타트코딩과 함께 파이썬 공부")
file.close()

file = open("data.txt", "a", encoding="utf8")
file.write("\n2. 비전공자도 정말 쉽게 배울 수 있습니다")

file = open("data.txt", "r", encoding="utf8")
# data = file.read()
# print(data)
# file.close()

while True:
    data = file.readline()
    print(data, end="")
    if data == "":
        break

file.close()
