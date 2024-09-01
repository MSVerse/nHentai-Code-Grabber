import requests
import re

# jangan terlalu sering ya bre
# engga baik buat tubuhmu bre
# tools ini recode dari tools SinonX
# kalau ada bug benerin sendiri jangan manja jadi orang bre
# Homepage: https://msversee.blogspot.com

def check_code_range():
    start_code = input("Input your start code: ")
    end_code = input("Input your end code: ")

    for code in range(int(start_code), int(end_code) + 1):
        code_str = str(code)
        print("=================================================")
        print('Checking...', code_str)
        
        response = requests.get(f'https://nhentai.net/g/{code_str}')
        title = re.findall('<meta itemprop="name" content="(.*?)"', response.text)
        tags = re.findall('<meta name="twitter:description" content="(.*?)"', response.text)
        languages = re.findall('<a href="/language/(.*?)/"', response.text)

        if response.status_code == 200:
            print(code_str, ' >> Found Doujin')
            for title_name, tag_list in zip(title, tags):
                print('Title : ', title_name)
                print('Tags : ', tag_list)
            try:
                languages.remove('translated')
                for lang in languages:
                    print('Language : ', lang)
                with open('ValidCodes.txt', 'a', encoding='utf-8') as valid_file:
                    valid_file.write(f'{code_str}\n{title_name}\n{tag_list}\n{lang}\n\n')
            except:
                for lang in languages:
                    print('Language : ', lang)
                with open('ValidCodes.txt', 'a', encoding='utf-8') as valid_file:
                    valid_file.write(f'{code_str}\n{title_name}\n{tag_list}\n{lang}\n\n')
        else:
            print('Not Found')


if __name__ == "__main__":
    print("""
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡤⠒⠋⠉⠉⠛⠿⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠃⠀⠀⠀⠀⠀⠀⢃⠈⢿⣆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⡇⠀⢸⡀⠀⢸⣦⢰⡈⡆⠈⡟⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣇⣀⢰⣿⣿⣄⢸⣿⣿⣟⣷⠀⣷⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⢁⠃⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣿⡸⣾⣿⣿⣿⣿⡿⠿⣿⡿⡏⢻⠁⢱⠀⠀⠀⠀⠀⠀⠀⠀⠀⠅⠌⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⠻⣿⠛⠿⠈⠀⠀⠈⠀⣇⠈⣷⣾⠀⠀⠀⠀⠀⠀⠀⠀⠐⠐⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣆⠀⣹⣦⠘⣧⠀⠀⠀⠀⠀⢀⣿⣀⣿⠀⣧⠀⠀⠀⠀⠀⠀⠀⠀⡨⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⣿⣀⣿⣿⣆⠘⡷⠢⢤⡴⠖⢉⡏⢹⢹⡗⠻⢤⡀⠀⠀⠀⠀⠈⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⢹⡿⣦⡼⡔⠊⠀⢠⣾⠀⡧⠘⡇⠀⠀⠘⡄⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡟⣿⠟⢻⣾⠓⠛⡇⢳⠄⢠⠟⡇⢠⡁⢠⠃⢀⠀⠀⣽⠀⠀⠀⠀⠀⠂⠀⣀⡤⠖⠒⠛⢦⡄⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡀⠁⢴⢻⠈⣆⡀⣣⣸⡆⠀⠀⢹⣌⣷⡧⢼⣿⡀⠀⡇⠀⠀⠠⠀⠀⢠⡾⠋⠀⠀⠀⠀⠀⢱⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢧⠀⠘⡀⡆⢉⣿⣿⡏⠁⠀⠀⠀⠈⠙⠁⠀⠚⠛⡄⢸⠀⠀⢠⣠⠔⠉⠀⠀⠀⠀⠀⠀⠀⢸⠃
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠀⢹⡃⡾⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡇⣸⠷⢒⠿⠁⠀⠀⣰⠆⠀⠀⠀⠀⠀⡎⠀
    ⠀⢀⡴⠒⠒⠲⠤⣀⣀⠀⠀⠀⠀⣇⠀⠀⠳⣇⠀⠀⠀⣀⠈⠀⠀⠀⠈⠉⠒⠚⢿⠏⢠⠔⠁⠐⠀⠀⢠⠏⠀⠀⠀⠀⠀⢸⠁⠀
    ⢠⠋⠀⠀⠀⠀⠀⠀⠈⠉⠒⠦⢄⣸⡀⠀⠀⠈⣖⢲⡚⠁⠀⠀⠒⠊⠁⠀⠀⠀⢸⡗⠁⠀⠀⠠⠀⡰⠃⠀⠄⠀⠀⠀⠀⢸⠀⠀
    ⢸⡄⠀⠀⠀⠀⠀⠰⡀⠀⠀⠀⠀⠈⠙⠒⢤⣀⣸⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⡴⠁⠀⠀⠀⠀⠀⣰⠁⠀⠀⠀⠀⠀⠀⢀⡏⠀⠀
    ⠀⠱⣄⠀⠀⠀⠀⠀⠈⠑⠦⡀⠀⠀⠀⠀⠀⠈⠙⠢⣀⠀⠀⢀⣤⡀⠀⢀⡞⠀⠀⠀⠀⠀⠀⠀⡗⠀⠀⠀⠀⠀⠀⠀⡾⠀⠀⠀
    ⠀⠀⠈⠣⡀⠀⠀⠀⠀⠀⠀⠈⠢⡀⠀⠀⠀⠀⠀⠀⠈⠓⠤⠼⡟⡅⠀⠙⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⢀⡜⠀⠀⠀⠀
    ⠀⠀⠀⠀⠱⡄⠀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⢀⣄⣸⣧⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⣧⠀⠀⠀⠀⢠⠎⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠈⢦⡀⠀⠀⠀⠀⠀⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠁⠘⢿⣠⠃⠀⠀⠀⠀⠀⠀⠀⣸⠉⢦⣀⣀⣰⠏⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠐⢦⡀⠀⠀⠀⠀⠀⠙⢄⠀⠀⠀⠀⠀⠀⠀⠀⠈⢃⡀⠀⠀⠀⠀⠀⠀⢠⠇⠀⠈⠛⢠⠃⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠢⣀⠀⠀⢀⠆⠀⠑⢤⡀⠀⠀⠀⠀⠀⠀⢈⣧⣀⠀⠀⠀⢀⣴⣿⠀⠀⠀⣀⠏⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠧⡀⠀⠀⠀⠀⠈⢳⣄⣀⣀⡠⠔⠋⠀⠀⠉⠉⠋⢉⡏⠙⣄⠀⣰⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠳⣄⠀⠀⠀⠸⣧⠙⡄⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⡀⠹⣿⠉⣯⣿⣦⡀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢳⣾⡟⢳⡿⠀⣵⠀⠀⠀⠀⠀⠀⠀⠀⠀⠘⢷⣄⢙⣿⣏⣩⠍⠿⣦⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣿⡿⠿⢿⠧⣠⠟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢹⣿⡀⠀⠀⠀⢀⣸⡆⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡼⠥⠤⠐⠚⠀⣸⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠯⠵⢶⠭⠽⠚⠁⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣧⣀⢀⣀⡠⢔⡯⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠓⠒⠒⠒⠛⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                       ===== NHentai Code Grabber =====
    """)
    print("Input the starting and ending codes to grab information in NHentai.")    
    print("Please use VPN")
    check_code_range()
