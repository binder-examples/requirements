DATA_PATH = '/Users/cvitzthum/Github/requirements/intermediate_tutorial/poetry_package/poetrypackage/data/customers.csv'


def analyze_customer_data():
    # This function analyzes customer data
    input_file = open(DATA_PATH, 'r')
    all_customers = []
    # read header
    headers = input_file.readline().strip().split(',')
    for line in input_file.readlines():
        # read the data
        parsed_line = line.strip().split(',')
        line_dict = {}
        for x in range(len(headers)):
            for y in range(len(parsed_line)):
                line_dict[headers[x]] = parsed_line[y]
        # clean the data... some first names and last are missing
        if not line_dict['First Name'] or not line_dict['Last Name']:
            continue
        all_customers += [line_dict]

    # get statistics about Country
    countries = {}
    for customer in all_customers:
        abc = customer['Country']

        # imitate some complex processing...
        import time
        time.sleep(0.0001)

        if abc not in countries:
            countries[abc] = 0
        else:
            countries[abc] = countries[abc] + 1

    return countries
