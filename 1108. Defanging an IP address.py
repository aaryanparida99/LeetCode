class Solution:
    def defangIPaddr(self, address: str) -> str:
        temp = address.split(".")
        address ="[.]".join(temp)
        return address
    