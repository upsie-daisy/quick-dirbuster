<h1><i><code>Quick-Dirbuster</code></i>  <img width="60px" src="https://media.giphy.com/media/WUlplcMpOCEmTGBtBW/giphy.gif">
</h1>

<p>A Handy Script for Finding Website Directories using Wordlists</p>
<p>Usage of this script for attacking targets without prior mutual consent is illegal. Developers assume no liability and are not responsible for any misuse or damage caused by this program</p>
<p>quick-dirbuster will first look for a robots.txt file, then try all the paths stored in your wordlist file.</p>

<h2><i>Installation :</i></h2>

```bash
git clone https://github.com/upsie-daisy/quick-dirbuster
```

<h2><i>Arguments :</i></h2>

|     | Option          | Description               | Default |
| --- | --------------- | ------------------------- | ------- |
| -u  | --url           | Choose Target URL         |         |
| -w  | --wordlist      | WordList path             |         |
| -o  | --output        | Write in output path      | False   |
| -v  | --verbose       | Verbose mode              | False   |
| -f  | --full-url      | Print the entire URL      | False   |
| -t  | --target        | Choose Target Status Code | 200     |
| -s  | --suffix        | Suffix (.html/.php...)    | None    |
| -sl | --show-length   | Print content length      | False   |
| -fl | --filter-length | Filter by content length  | False   |
| -ro | --robots-txt    | Search for robots.txt     | True    |

<h2><i>Example :</i></h2>

```bash
./quick-dirbuster.py -u github.com -w wordlist.txt
```

<p>Result :</p>

<img src="https://media.giphy.com/media/CAIdJxPG98N4iILXYh/giphy.gif">

<h2><i>WordLists :</i></h2>

1. [Node-Dirbuster WordLists](https://github.com/daviddias/node-dirbuster/tree/master/lists)
2. [Dirbuster-ng](https://github.com/digination/dirbuster-ng/tree/master/wordlists)
3. [KaliLists](https://github.com/3ndG4me/KaliLists/blob/master/wfuzz/webservices/ws-dirs.txt)
4. [Web wordlists in 2021](https://blog.sec-it.fr/en/2021/03/02/web-wordlists/)

<hr>

![Follow me](https://img.shields.io/badge/-Follow%20Me-222222?logo=twitter&logoColor=black&color=272838&labelColor=C09891&style=for-the-badge&logoWidth=30&link=https://twitter.com/IlIIlIIllIlI)

