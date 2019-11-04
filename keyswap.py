import os

class swaplist:

    def __init__(self):
        self.exchange = {}

    def open_key_file(self, keyfile):
        try:
            f = open(os.path.join(os.getcwd())+"/"+(keyfile))
        except:
            print("Opening dictionary file %s failed" % (str(keyfile))) 
        for line in f:
            line = line.strip()
            line = line.split(":")
            self.exchange[line[0]] = line[1]
        f.close()

    def write_key_file(self, keyfile):
        try:
            f = open(keyfile,"wr")
        except:
            print("Writing to dictionary file %s failed" % (str(keyfile)))
        for key in self.exchange:
            f.write(key+":"+self.exchange[key]+'\n')
        f.close()
            
    def add_key(self, key, swap):
        self.exchange[key] = swap

    def rem_key(self, key):
        del self.exchange[key]

    def clear_keys(self):
        exchange.clear()

    def swaplist_keys(self):
        return self.exchange
