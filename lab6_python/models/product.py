class Product:
    def __init__(self, name: str, price: float, category: str):
        self.name = name
        self.price = float(price)
        self.category = category

    def __str__(self) -> str:
        return f"{self.name} ({self.category}) - {self.price:.2f} PLN"

    def __repr__(self) -> str:
        return f"Product(name={self.name!r}, price={self.price!r}, category={self.category!r})"

    def __eq__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        return self.name == other.name and self.category == other.category

    def __lt__(self, other) -> bool:
        if not isinstance(other, Product):
            return NotImplemented
        # sortowanie po cenie
        return self.price < other.price

    def __len__(self) -> int:
        return len(self.name)
