##################
#
# A Handy Script for Finding Website Directories using Wordlists
#
# github.com/upsie-daisy/quick-dirbuster
# Made by @Upsie-Daisy
#
#################

import requests, sys, os, time
from src.flags import Flag
from src.ansi import a

flag = Flag(description="A Handy Script for Finding Website Directories using Wordlists, made by @Upsie-Daisy")

flag.new(short="-u", full="--url", required=True, help="Choose Target URL")
flag.new(short="-w", full="--wordlist", required=True, help="WordList path")
flag.new(short="-o", full="--output", default=False, type="string", help="Write in output path")
flag.new(short="-v", full="--verbose", default=False, type="bool", help="Verbose mode")
flag.new(short="-f", full="--full-url", default=False, type="bool", help="Print the entire URL")
flag.new(short="-t", full="--target", default="200", help="Choose Target Status Code")
flag.new(short="-s", full="--suffix", default=None, help="Suffix (.html/.php...)")
flag.new(short="-sl", full="--show-length", default=False, type="bool", help="Print content length")
flag.new(short="-fl", full="--filter-length", type="int", default=False, help="Filter by content length")

flag.parse()

def format_url(url):
    print(f"{a.bl}[{a.g}?{a.bl}] {a.rst}Formating url \"{a.c}{url}{a.rst}\"")
    if not url.startswith("https://") and not url.startswith("http://"):
        url = "https://" + url
    if not url.endswith("/"):
        url = url + "/"
    print(f"{a.bl}> {a.rst}{url}")
    return url

def parse_wordlist(path):
    print(f"{a.bl}[{a.g}?{a.bl}] {a.rst}Parsing WordList \"{a.c}{path}{a.rst}\"")
    try:
        with open(flag.wordlist) as file:
            wordlist = file.read().strip().split('\n')
        print(f"{a.bl}> {a.rst}Done {a.bl}({len(wordlist)} results){a.rst}")
        return wordlist
    except IOError:
        print(f"{a.bl}[{a.r}!{a.bl}] {a.rst}Error while parsing WordList \"{a.c}{path}{a.rst}\"")
        sys.exit(1)

def status_url(url):
    try:
        response = requests.get(url)
    except Exception:
        print(f"{a.bl}[{a.r}!{a.bl}] {a.rst}Error unexpected while reaching \"{a.c}{url}{a.rst}\"")
        sys.exit(1)
    return response

def progress_bar(i, length):
    print(a.sc, end="")
    print(f"{a.mt(2,0)}{a.bl}", end="")
    percent = int(i / length * os.get_terminal_size().columns)
    for hashtag in range(percent):
        print("#", end="")
    print(f"{a.rst}{a.rc}", end="")
    
def start_scan(url, wordlist, target, suffix):
    try:
        print(f"{a.clr}{a.top}", end="")
        print(f"{a.bl}", end="")
        for col in range(int((os.get_terminal_size().columns - 10) / 2)):
            print("-", end="")
        print(f"[{a.c}{a.bld}PROGRESS{a.rst}{a.bl}]", end="")
        for col in range(int((os.get_terminal_size().columns - 10) / 2)):
            print("-", end="")   
        print(f"{a.rst}\n\n")
        if flag.output != False:
            try:
                file = open(flag.output, 'w')
            except:
                print(f"{a.bl}[{a.r}!{a.bl}] {a.rst}Error unexpected while opening \"{a.c}{flag.output}{a.rst}\"")
                sys.exit(1)
            
            file.write(f"[-] Dirbuster [By @Upsie-Daisy]\n")
            file.write("\n")
            file.write(f"- Target : {url}\n")
            file.write(f"- Wordlist : {flag.wordlist} ({length})\n")
            file.write(f"- Targeted status code : {flag.target}\n")
            file.write(f"- Verbose mode : {flag.verbose}\n")
            file.write(f"- Filter length : {flag.filterlength}\n")
            file.write(f"- Show length : {flag.showlength}\n")
            file.write(f"- Print full url : {flag.fullurl}\n")
            file.write(f"- Suffix : {flag.suffix}\n")
            file.write(f"- Output report : {flag.output}\n\n")
        print(f"{a.bl}[{a.c}-{a.bl}] {a.rst}Dirbuster {a.bl}[By @Upsie-Daisy]{a.rst}")
        print()
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Target : {a.c}{url}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Wordlist : {a.c}{flag.wordlist}{a.rst} {a.bl}({length}){a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Targeted status code : {a.c}{flag.target}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Verbose mode : {a.c}{flag.verbose}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Filter length : {a.c}{flag.filterlength}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Show length : {a.c}{flag.showlength}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Print full url : {a.c}{flag.fullurl}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Suffix : {a.c}{flag.suffix}{a.rst}")
        print(f"{a.bl}[{a.bl}-{a.bl}] {a.rst}Output report : {a.c}{flag.output}{a.rst}")
        print(f"{a.bl}[{a.c}...{a.bl}] {a.rst}Start scanning in 3 seconds", end="")
        sys.stdout.flush()
        time.sleep(3)
        print(a.cll)

        result = 0
        if suffix == None:
            suffix = ""
        for i in range(length):
            progress_bar(i, length)
            sys.stdout.flush()
            response = status_url(f"{url}{wordlist[i]}{suffix}")
            if response.status_code == int(target) or target == "*" or flag.verbose:
                if flag.filterlength != False or flag.showlength == True:
                    l = len(response.text)
                    if flag.filterlength == l:
                        continue
                result += 1
                if flag.fullurl == True:
                    print(f"{a.bl}[{a.m}{response.status_code}{a.bl}] {a.rst}{url}{wordlist[i]}{suffix}", end="")
                    if flag.output != False:
                        file.write(f"[{response.status_code}] {url}{wordlist[i]}{suffix}")
                else:
                    print(f"{a.bl}[{a.m}{response.status_code}{a.bl}] {a.rst}/{wordlist[i]}{suffix}", end="")
                    if flag.output != False:
                        file.write(f"[{response.status_code}] /{wordlist[i]}{suffix}")
                if flag.showlength == True:
                    print(f" {a.bl}len:{l}{a.rst}", end="")
                    if flag.output != False:
                        file.write(f"len:{l}")
                
                if flag.output != False:
                    file.write("\n")        
                print()
        if flag.output != False:
            file.close()    
        print(f"\n{a.bl}[{a.g}v{a.bl}] {a.rst}Scan done, found {result} results !{a.rst}")
    except KeyboardInterrupt:
        print(f"\n{a.bl}[{a.r}!{a.bl}] {a.rst}Error, Keyboard Interrupt")
        sys.exit(1)

url = format_url(flag.url)
wordlist = parse_wordlist(flag.wordlist)
length = len(wordlist)

start_scan(url, wordlist, flag.target, flag.suffix)

    