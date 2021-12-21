import random

def main():
    list_of_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p",
                       "q","r","s","t","u","v","w","x","y","z"]
    list_of_numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
    list_of_characters = ["!", "@", "#", "$", "%", "^", "&", "*", "(",")","-","+","=","?"
                          " ","'",":",";","/","<",">","[","]","{","}",".",","]
    combined_list = list_of_characters + list_of_numbers + list_of_letters
    prompt = user_prompt()
    password = create_password(prompt, combined_list)
    print(f"Here is your password {password}")

def user_prompt():
    while True:
        prompt = input("Enter Password Length (Max 20): ")
        if prompt.isdigit():
            if 0<int(prompt)<=20:
                return int(prompt)
            else:
                print("Invalid Entry. Please try again.")
        else:
            print("Invalid Entry. Please enter a number between (1-20)")
            continue

def create_password(prompt, combined_list):
    password = random.sample(combined_list, prompt)
    string_password = "".join(password)
    return string_password

if __name__ == '__main__':
    main()