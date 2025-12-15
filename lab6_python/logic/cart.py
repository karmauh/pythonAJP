from models.product import Product


class Cart:
    def __init__(self):
        self._products: list[Product] = []

    def add_product(self, product: Product) -> None:
        self._products.append(product)

    def remove_product(self, product: Product) -> bool:
        for i, p in enumerate(self._products):
            if p == product:
                self._products.pop(i)
                return True
        return False

    def total_price(self) -> float:
        return sum(p.price for p in self._products)

    def __len__(self) -> int:
        return len(self._products)

    def __contains__(self, item) -> bool:
        return any(p == item for p in self._products)

    def __str__(self) -> str:
        if not self._products:
            return "Koszyk jest pusty."

        lines = ["Koszyk:"]
        for idx, p in enumerate(self._products, start=1):
            lines.append(f"{idx}. {p}")
        lines.append(f"Suma: {self.total_price():.2f} PLN")
        return "\n".join(lines)
