# from os import get_terminal_size

# from time import sleep
# from tqdm import tqdm

# def ft_tqdm(lst: range)-> list:

#     total = len(lst)
    
#     progress_bar_width = get_terminal_size().columns - 40

#     for i in range(0, total + 1):
#         progress = int(i / total * progress_bar_width)

#         progress_bar = f"|{'█' * progress:<{progress_bar_width}}|"
#         progress_percentage = progress * 100 // progress_bar_width
#         progress_info = f"{progress_percentage}%{progress_bar} {i}/{total}"

#         print(f"\r{progress_info}", end="", flush=True)
#         yield i


# def main():
# 	for elem in ft_tqdm(range(333)):
# 		sleep(0.005)
# 	print()
# 	for elem in tqdm(range(333)):
# 		sleep(0.005)
# 	print()

# if __name__ == "__main__":
#     main()

my_num_list = [3, 6, 9, 12]

def sum(*nums):
  res = 0
  for num in nums:
    res += num
  print(res)

sum(*my_num_list)