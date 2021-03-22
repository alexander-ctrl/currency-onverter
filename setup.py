
if __name__ == "__main__":
    try:
        import PyQt5
        import currency_converter
        import urllib
        from conversormoneda.main import run

        run()

    except Exception as e:
        print(e)