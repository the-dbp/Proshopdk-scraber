class Hdd:
    def __init__(self, name, price, gb, url):
        self.name = name
        self.price = price
        self.gb = gb
        self.url = url

    def __str__(self):
        return f"pris: {self.price} GB: {self.gb} pris pr GB: {str((self.price / self.gb))[:6]}".ljust(50)+f"url: https://www.proshop.dk{self.url}"
