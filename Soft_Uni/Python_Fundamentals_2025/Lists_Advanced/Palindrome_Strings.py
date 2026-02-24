# my_list = [::-1]

words = input().split()
palindrome = input()

palindrome_list = [word for word in words if word == word[::-1]]
print(palindrome_list)
print(f"Found palindrome {palindrome_list.count(palindrome)} times")