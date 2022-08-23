import main
import scrape

for i in range(200):
    dict = scrape.scrape(i+1)
    try:   
        chemical = main.Chemical(dict['name'], dict['cas_number'])
        chemical.save()
    except TypeError:
        print("Name and CAS number not specified")


