def save_applicant_data(source, output):
    with open(output, 'w') as opened_file:
        for item in source:
            opened_file.write(f"{item['name']},{item['specialty']},{item['math']},{item['lang']},{item['eng']}\n")     
        
