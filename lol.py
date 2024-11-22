import random
import pyttsx3
import requests
from bs4 import BeautifulSoup


class Name:
    def __init__(self, first, middle, last):
        self.first = first
        self.middle = middle
        self.last = last

    def full_Name(self):
        return "{} {} {}".format(self.first, self.middle, self.last)
    
    def name_translation(self, source_lang, target_lang):
        url = f"https://context.reverso.net/translation/{source_lang}-{target_lang}/{self.first}"
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }

        # Send the GET request
        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            # Parse the HTML
            soup = BeautifulSoup(response.content, "html.parser")

            # Extract translations
            translations = soup.find_all("a", class_="translation")
            translation_list = [t.text.strip() for t in translations if t.text.strip()]

            return translation_list[1]
        else:
            return [f"Error: {response.status_code}"]
    pass
    
    # def cool_email_name(self):
    #     pass
    
    # change this to have an interface and make a button that voices it....
    # can use gtts instead
    def funny(self):
        vowels = ["a", "e", "i", "o", "u", "y"]  
        consonants = ["m", "n", "l", "r", "t", "k", "p"]  
        
        random_pair = random.choice(vowels) + random.choice(consonants)
        random_tena = f"t{random_pair}a"  
        
        nickname = self.first[0] + random_tena + self.first[1:]
        print(nickname)
        engine = pyttsx3.init()
        engine.say(nickname)
        engine.runAndWait()
        return nickname
    
    def urban_dictionary(self):
        term = self.first  # Use the first name as the search term
        api = f"http://api.urbandictionary.com/v0/define?term={term}"  # Correct URL format
        try:
            response = requests.get(api)
            response.raise_for_status()
            data = response.json()
            if data["list"]:
                # Get the top definition
                top_definition = data["list"][0]["definition"]
                return f"{term}: {top_definition}"
            else:
                return f"No Urban Dictionary definitions found for {term}."
        except Exception as e:
            return f"Error fetching definition: {str(e)}"
    pass
    

first = Name("Arwa", "Ahmed", "Madien")

print(first.urban_dictionary())
print(first.name_translation("english", "arabic"))