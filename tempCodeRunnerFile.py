
# write "with".... and close automatically........
str = "ababababababab \npopopo p op "
with open("demo.txt", "w") as file1:
    file1.write(str)
    file1.write("Pawan pawan \n bisht")
print("written"