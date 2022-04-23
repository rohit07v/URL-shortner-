
class Codec:
    def __init__(self):
        self.encodeMap={}
        self.decodeMap={}
        self.base="http://tinyurl.com/"

    def encode(self,longurl):
        if longurl not in self.encodeMap:
            shorturl=self.base+str(len(longurl)+1)
            self.encodeMap[longurl]=shorturl
            self.decodeMap[shorturl]=longurl


        return self.encodeMap[longurl]

    def decode(self,shorturl):
        return self.decodeMap[shorturl]





longurl = input()
codec=Codec()
print(codec.encode(longurl))
print(codec.decode(codec.encode(longurl)))
