# def convert_seconds(seconds):
#   seconds = seconds % (24 * 3600)
#   hour = seconds // 3600
#   seconds %= 3600
#   minutes = seconds // 60
#   seconds %= 60
#   return (hour, minutes, seconds)


# hour, minute, sec = convert_seconds(3999)
# print(hour, minute, sec)

# for x in range(10):
#     for y in range(x):
#         print(y)


# for x in range(5):
#     for y in range(x):
#         print("*", end=" ")
#     print(" ")
        
# winners = ["as", "dilan", "ucok"]
# for i, person in enumerate(winners):
#     print(f"{i + 1}. {person}")
    
    
def full_emails(people):
    result=[]
    for email, name in people:
        result.append(f"{name}, <{email}>")
    return result

print(full_emails([("hanif@gmail.com", "hanif"),
             ("ucok@gmail.com", "ucok")]))

def countLetter(text):
    result={}
    
    for letter in text:
        if letter in result:
            result[letter] += 1
        else:
            result[letter] = 1
    return result

print(countLetter("aaaaa"))

wardrobe = {'shirt': ['red', 'blue', 'white'], 'jeans': ['blue', 'black']}
new_items = {'jeans': ['white'], 'scarf': ['yellow'], 'socks': ['black', 'brown']}
wardrobe.update(new_items)

print(wardrobe)

genre = "transcendental"
print(genre[:-8])