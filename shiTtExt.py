from random import randint

def main():
	print("all credits belong to Lukas Chronc")
	print("he's indeed better than me")
	print("enjoy it")
	text = list(input("Let me FUCK your text: "))
	start = 0
	end = 3
	while end < len(text) - 1:
		pos = randint(start, end)
		text[pos] = text[pos].upper()
		start += 1
		end += 1
	print("\n \t")
	for ch in text: print(ch, end="")
	
if __name__ == "__main__": main()	
