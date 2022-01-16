
def create_tabular_data(scorecard_data, num_of_sets):
    table_data = []
    while len(scorecard_data) !=  num_of_sets+1:
        scorecard_data.append(('-','-'))
    rows = list(zip(*scorecard_data))
    sets_names = ["Team Name"]
    sets_names.extend([f"Set-{str(i+1)}" for i in range(num_of_sets)])
    table_data.append(sets_names)
    table_data.extend(rows)
    return table_data

def disply_table(table_data):
    for row in table_data:
        msg = "{: >6}"*len(table_data[0])
        print(f"{msg}".format(*row))

