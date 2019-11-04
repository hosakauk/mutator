import re

class mutator():
  
    def __init__(self, password):
        self.password = password
        self.list = []

    def first_upper(self, password):
        password = re.sub(r'(?<![a-z])[a-z](?![0-9])', lambda x: x.group(0).upper(), password)
        return password

    def last_upper(self, password):
        password = re.sub(r'(?<![0-9])[a-z](?![a-z])', lambda x: x.group(0).upper(), password)
        return password

    def number_suffix(self, password, lower, upper):
        for i in range(lower,(upper+1)):
            self.list.append(password+str(i))
        return(self.list)

    def number_prefix(self, password, lower, upper):
        for i in range(lower,(upper+1)):
            self.list.append(str(i)+password)
        return(self.list)
            
    def single_swap(self, password, exchange):
        for i in range(len(password)):
            for char in password[i]:
                if char in exchange:
                    charswap = char.replace(char, exchange[char])
                else:
                    charswap = char
            newchar = password[i].replace(password[i], charswap)
            newpass = (password[:i]+newchar+password[i+1:])
            if newpass in self.list:
                pass
            else:
                self.list.append(newpass)
        return(self.list)
            
    def all_swap(self, password, exchange):
        self.list.append(password)
        for item in self.list:
            for i in range(len(item)):
                for char in item[i]:
                    if char in exchange:
                        charswap = char.replace(char, exchange[char])
                    else:
                        charswap = char
                newchar = item[i].replace(item[i], charswap)
                newpass = (item[:i]+newchar+item[i+1:])
                if newpass in self.list:
                    pass
                else:
                    self.list.append(newpass)
        return(self.list)

    def swap_list_size(self):
        return len(self.list)
