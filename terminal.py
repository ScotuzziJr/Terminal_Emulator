import os
import shutil

os.system('cls' if os.name == 'nt' else 'clear')

while True:
	command = input('$ ')
	if command == '\q':
		break	

	elif command == '--help':	
		list_commands = """
| `\q`						--quit terminal						|
| `pwd`						--show current directory				|
| `ls`						--list files and folders within current directory	|
| `cd ..`					--go one directory up					|
| `cd {dir_name}`				--change directory					|
| `mkdir {dir_name}`				--create a new directory				|
| `rmdir {dir_name}`				--delete a directory					|
| `touch {file_name}.{extension}`		--create a file						|
| `rm {file_name}`				--delete a file						|
| `mv {file_name} {destination_directory}`	--move a file to a directory				|
| `clear`					--clear console						|
"""
		print(list_commands)

	elif command == 'pwd':
		print(os.getcwd())

	elif command == 'ls':
		content_dir = os.listdir()
		for content in content_dir:
			print(content)

	elif command == 'cd ..':
		"""
		current_dir = os.getcwd()
		current_dir = current_dir.split('/')
		del current_dir[len(current_dir) - 1]
		new_dir = '/'.join(current_dir)
		os.chdir(f'{new_dir}')
		"""
		os.chdir("..")

	elif 'cd' in command:
		try:
			command = command.split('cd ')
			command = '/'.join(command)
			current_dir = os.getcwd()
			new_dir = current_dir + command
			os.chdir(f'{new_dir}')
		except:
			print('The directory doesn\'t exist.')

	elif 'mkdir' in command:
		try:
			command = command.split('mkdir ')
			dir_name = command[1]
			os.mkdir(f'{dir_name}')				
		except:
			print('Directory already exists.')

	elif 'rmdir' in command:
		try:
			command = command.split('rmdir ')	
			dir_name = command[1]
			os.rmdir(f'{dir_name}')
		except:
			print('There\'s no such directory.')

	elif 'mv' in command:
		try:
			command = command.split(' ')
			source = os.path.join(os.getcwd(), command[1])
			destination = os.path.join(os.getcwd(), command[2], command[1])		
			shutil.move(source, destination)
		except:
			print('There\'s no such file or directory.')	

	elif 'rm' in command:
		try:
			command = command.split('rm ')
			os.remove(command[1])
		except:
			print('There\'s no such file.')

	elif 'touch' in command:
		try:
			command = command.split('touch ')
			with open (command[1], 'w') as f:
				f.close()	
		except:
			print('File already exists.')

	elif command == 'clear':
		os.system('cls' if os.name == 'nt' else 'clear')

	else:
		print("Invalid command. To check the list of commands type `--help`")

