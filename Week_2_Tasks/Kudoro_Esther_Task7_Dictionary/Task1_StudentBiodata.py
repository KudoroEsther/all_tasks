#Task 1 Student biodata storage
info = {
    "Name": input("Input your name: "),
    "age": int(input("Enter your age: ")),
    "gender": input("Input your gender: "),
    "course": input("Enter your course: ").split()
}
# print(*info.items(), sep="\n")
for key, val in info.items():
    print(f"{key}:\t{val}") #prints the content of the dictionary on a new line with tab in between

