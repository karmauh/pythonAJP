from models.product import Product
from logic.cart import Cart


def main():
    # produkty
    p1 = Product("Laptop", 3500, "electronics")
    p2 = Product("Laptop", 5000, "electronics")
    p3 = Product("Jabłko", 2.5, "food")
    p4 = Product("Mleko", 4.2, "food")

    print("Porównania:")
    print("p1 == p2:", p1 == p2)
    print("p3 < p4 :", p3 < p4)
    print("len(p1):", len(p1))

    products = [p1, p2, p3, p4]
    products_sorted = sorted(products)
    print("\nProdukty posortowane po cenie:")
    for p in products_sorted:
        print("-", p)

    # koszyk
    cart = Cart()
    cart.add_product(p1)
    cart.add_product(p3)
    cart.add_product(p4)

    print("\nKoszyk po dodaniu produktów:")
    print(cart)

    print("\nTesty koszyka:")
    print("len(cart):", len(cart))
    print("p1 in cart:", p1 in cart)
    print("total_price:", cart.total_price())

    removed = cart.remove_product(Product("Jabłko", 999, "food"))  # cena nie ma znaczenia w __eq__
    print("\nUsunięto jabłko?:", removed)
    print(cart)


if __name__ == "__main__":
    main()
