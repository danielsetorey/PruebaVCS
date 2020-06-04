from src.scrapping.printer import superprint



def test_printer_ok():
    assert superprint("aa") == "aa"
