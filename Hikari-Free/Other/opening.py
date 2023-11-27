# Заходи в наш тгк за обновлениями! t.me/projecthikari
from colorama import Fore, Style, init
init()
# Цвета
dcyan = Style.NORMAL + Fore.CYAN
cyan = Style.BRIGHT + Fore.CYAN
blueb = Style.BRIGHT + Fore.BLUE
white = Style.BRIGHT + Fore.WHITE
baza = Style.NORMAL
# Баннер и меню
def Banner():
    print(f'''
{blueb}╔───────────────────────────────────────────────────────────────────────╗
{blueb}│                                                                       │
│   {white}{white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█  {blueb}│
│  {white}{blueb}░{blueb}░{white}█{white}█{white}█   {blueb}░{blueb}░{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█   {white}█{white}█{white}█{blueb}░   {white}█{white}█{white}█{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█   {blueb}│
│   {white}{blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█  {white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█   {blueb}│
│   {white}{blueb}░{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█{white}█{white}█{white}█{white}█     {blueb}░{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█{white}█   {blueb}░{white}█{white}█{white}█   {blueb}│
│   {white}{blueb}░{white}█{white}█{white}█{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█{blueb}░{blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█   {blueb}│
│   {white}{blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█   {blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█    {blueb}░{white}█{white}█{white}█  {blueb}░{white}█{white}█{white}█   {blueb}│
│   {white}{white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█ {blueb}░{blueb}░{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█   {white}█{white}█{white}█{white}█{white}█ {white}█{white}█{white}█{white}█{white}█  {blueb}│
│  {white}{blueb}░{blueb}░{blueb}░{blueb}░{blueb}░   {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░ {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░ {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░   {blueb}░{blueb}░{blueb}░{blueb}░ {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░   {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░ {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░   {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░ {blueb}░{blueb}░{blueb}░{blueb}░{blueb}░   {blueb}│
╠───────────────────────────────────────────────────────────────────────╣
│                    {white}Переходник{dcyan}:{cyan} t.me/projecthikari                     {blueb}│
│              {white}Разработчики{dcyan}:{cyan} @JIABANDA, @Honshitsu, @GD23C              {blueb}│
│           {dcyan}[{white}!{dcyan}]{cyan}Пропишите /info для более подробной информации           {blueb}│
╚───────────────────────────────────────────────────────────────────────╝
{dcyan}[{white}ВНИМАНИЕ{dcyan}]{cyan} Софт является абсолютно бесплатным, следить за новостями и обновлениями касательно софта можно в нашем телеграм-канале!''')
def Menu():
    print(f'''{blueb}╔─────────────────────╦─────────────────────────────────────────────────╗
│       {dcyan}[{white}OSINT{dcyan}]{blueb}       │           {dcyan}[{white}Разнообразные инструменты{dcyan}]{blueb}           │
╠─────────────────────╬─────────────────────────────────────────────────╣
├ {white}1{dcyan}. {white}Поиск по номеру{blueb}  ├ {white}5{dcyan}. {white}Добавить бд{blueb}                                  │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}2{dcyan}. {white}Поиск по IP{blueb}      ├ {white}6{dcyan}. {white}WormGPT{blueb}                                      │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}3{dcyan}. {white}Поиск по VK{blueb}      ├ {white}7{dcyan}. {white}Dos{blueb}                                          │
╠─────────────────────┼─────────────────────────────────────────────────╣
├ {white}4{dcyan}. {white}SHODAN{blueb}           ├ {white}8{dcyan}. {white}Web-crawler{blueb}                                  │
╚─────────────────────┴─────────────────────────────────────────────────╝''')
