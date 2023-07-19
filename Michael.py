# This is Michael's code 

def encode(string):
	new_string = ''
	for i in string:
		new_string += str(int(i)+3)
	return new_string


def menu():
	print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit')


def main():
	while True:
		menu()
		option = int(input('Please enter an option: '))
		if option == 1:
			password = input('Please enter your password to encode: ')
			encoded_password = encode(password)
			print('Your password has been encoded and stored!')
		elif option == 2:
			debugged_password = decode(encoded_password)
			print(f'The encoded password is {encoded_password}, and '
				  f'the original password is {debugged_password}')
		elif option == 3:
			break


if __name__ == '__main__':
	main()
