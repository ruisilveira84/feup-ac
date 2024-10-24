import read_data as rd

def prepare_data():
    tables = rd.read_data()

    tables = rd.remove_null_entries(tables)
    rd.print_null_fields(tables)

if __name__ == "__main__":
    prepare_data()
