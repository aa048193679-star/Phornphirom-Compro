keep_going = 'y'
while keep_going == 'y':
  item_wholesale = float(input("Enter the item's wholesale cost: "))
  retail_price = item_wholesale * 2.5
  print(f'The commission is ${retail_price:.2f}')
  keep_going = input('Do you have another item?' + \
                                ' commission (Enter y for yes): ')