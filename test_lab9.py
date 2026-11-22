from Lab_Program9 import product_details


def test_product_details():
    result = product_details("P101", "Notebook", "10", "50")
    expected = (
        "Product ID: P101\n"
        "Name: Notebook\n"
        "Quantity: 10\n"
        "Price: 50"
    )

    assert result == expected