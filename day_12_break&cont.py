def process_until_duplicate(fruits):
    fruit_set=set()
    for fruit in fruits:
        if fruit in fruit_set:
            print(f"Duplicate found,Processing Stopped")
            break
            
        fruit_set.add(fruit)
        print(f"Processed {fruit}")
    print(f"operation done")
            
 
if __name__ == "__main__":
    # print_nums()
    # skip_even()
    # Test case
    # print(first_negative([3, 5, 7, -1, 9, -3]))  # -1
    process_until_duplicate(["apple", "banana", "carrot", "apple", "date", "banana"])

# Task 3:
 
def censorship_bot(messages, banned_words):
    for i in messages:
        if i.find('bad') or i.find('oops'):
            continue
 
messages = [
    "Hello everyone!",
    "This is a bad word example!",
    "Let's keep our chat clean!",
    "Oops another bad content!",
    "Have a nice day!"
]
 
banned_words = ["bad", "oops"]
 
 
 
# Expected output
# Approved message: Hello everyone!
# Approved message: Let's keep our chat clean!
# Approved message: Have a nice day!
