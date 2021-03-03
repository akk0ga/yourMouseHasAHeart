import os.path

num_files = len([f for f in os.listdir(os.chdir(f'voice/fast/en'))])
print(type(num_files))
