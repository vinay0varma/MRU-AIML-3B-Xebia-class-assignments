#Count Vowels and Consonants
#Write a function that takes a string and returns the count of vowels and consonants. For example, for the input "hello world", the output should be {'vowels': 3, 'consonants': 7}
t = input("enter the WORD or sentence : ")
vowels_count = 0
consonants_count = 0
for i in t:
    if i != " ":
        if i.lower() in "aeiou":
            vowels_count += 1 
        else:
            consonants_count += 1 
print(f"vowels : {vowels_count} and consonants : {consonants_count}")
