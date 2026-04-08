import re
import math

from Bank import members
class Bank(members):
    def __init__(self, country, currency):
        self.country = country
        self.currency = currency
        self.member = members
        
        
    
    def convert_currency(amount, from_country, to_currency):
    # Map countries to their currency codes
        country_to_currency = {
            "USA": "USD",
            "United States": "USD",
            "UK": "GBP",
            "United Kingdom": "GBP",
            "Japan": "JPY",
            "India": "INR",
            "Canada": "CAD",
            "Australia": "AUD",
            "Eurozone": "EUR"
        }
        
        from_currency = country_to_currency.get(from_country)

    