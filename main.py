import pmut
import keyswap

'''
Keyswap examples:
------------------
swaplist.open_key_file("leet.dict")         # opens swaplist file
swaplist.write_key_file("new.dict")         # writes swaplist file
swaplist.clear_keys()                       # empties swaplist
swaplist.add_key("z","2")                   # add key to swaplist
swaplist.rem_key("z")                       # remove key from swaplist
print swaplist.swaplist_keys()              # prints keys in swaplist

Mutator examples:
------------------
print mutator.first_upper(password)         # first alpha upper
print mutator.last_upper(password)          # last alpha upper
print mutator.number_suffix(password,5,25)  # appends suffix, takes 2 params for range
print mutator.number_prefix(password,5,25)  # appends prefix, takes 2 params for range
print mutator.single_swap(password)         # 1 time iteration over password, takes password and exchange list as params
print mutator.all_swap(password,exchange)   # All combinations C(n,r), takes password and exchange list as params
print mutator.swap_list_size()              # number of mutations in array
'''

swaplist = keyswap.swaplist()
swaplist.open_key_file("leet.dict")
exchange = swaplist.swaplist_keys()
password = "password"
mutator = pmut.mutator(password)
print mutator.all_swap(password,exchange)
print mutator.swap_list_size()
