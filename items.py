TOKEN = "" # Токен твоего бота

PROTOCOLS = {
    "1.18.2": 758, "1.18.1, 1.18.2": 757, "1.17.1": 756, "1.17": 755, "1.16.5": 754,
    "1.16.3": 753, "1.16.2": 751, "1.16.1": 736, "1.16": 735, "1.15.2": 578,
    "1.15.1, 1.15": 573, "1.14.4": 498, "1.14.3": 490, "1.14.2": 485, "1.14.1": 480,
    "1.14": 477, "1.13.2": 404, "1.13.1": 401, "1.13": 393, "1.12.2": 340,
    "1.12.1": 338, "1.12": 335, "1.11.2, 1.11.1": 316, "1.11": 315,
    "1.10.2 - 1.10": 210, "1.9.4, 1.9.3": 110, "1.9.2": 109, "1.9.1": 108,
    "1.9": 107, "1.8 - 1.8.9": 47, "1.7.6 - 1.7.10": 5, "1.7.2 - 1.7.5": 4
}

MENU = {
    "☠ Attack": "$attack <ip:port> <version> <method>",
    "💫 Spam": "$spam <ip:port> <time> <text> **(только на 1.12.2)**",
    "💦 Methods": "$methods",
    "🕳 Protocols": "$protocols",
    "💥‍♀️ Resolve" : "$resolve <domain.ru>"
}

OWNERS = [823635176575467550]
METHOD_LIST = ["join", "legitjoin", "localhost", "invalidnames", "longnames", "botjoiner", "power", "spood", "ping", "spam", "killer", "nullping", "charonbot", "multikiller", "packet", "handshake", "bighandshake", "query", "bigpacket", "network", "randombytes", "extremejoin", "spamjoin", "nettydowner", "ram", "yoonikscry", "colorcrasher", "tcphit", "queue", "botnet", "tcpbypass", "ultimatesmasher", "sf", "nabcry"]
BLACK_LIST = []

ERROR = "❌ ERROR!"
BLACKLIST_ERROR = "**🚫 Этот айпи нельзя заддосить!**"
NOT_FOUND = "**🚫 Вы не указали аргументы! $help для помощи.**"
METHOD_ERROR = "**🚫 Метода нету в списке! $methods чтобы узнать методы.**"
INTEGER_ERROR = "**🚫 Аргумент <ВРЕМЯ> должен быть числом!**"
IP_ERROR = "**🚫 Аргумент <IP> должен быть цифренным с портом! Пример: 127.0.0.1:25565**"

METHODS = "join, legitjoin, localhost, invalidnames, longnames, botjoiner, power, spoof, ping, spam, killer, nullping, charonbot, multikiller, packet, handshake, bighandshake, query, bigpacket, network, randombytes, extremejoin, spamjoin, nettydowner, ram, yoonikscry, colorcrasher, tcphit, queue, botnet, tcpbypass, ultimatesmasher, sf, nabcry"



URL_LIST_PROXY = '''
https://raw.githubusercontent.com/clarketm/proxy-list/master/proxy-list-raw.txt
https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/socks4.txt
https://raw.githubusercontent.com/jetkai/proxy-list/main/online-proxies/txt/proxies.txt
https://raw.githubusercontent.com/sunny9577/proxy-scraper/master/proxies.txt
https://api.proxyscrape.com/?request=getproxies&proxytype=socks4&timeout=10000&country=all
https://api.proxyscrape.com/v2/?request=getproxies&protocol=socks4&timeout=10000&country=all
https://raw.githubusercontent.com/ShiftyTR/Proxy-List/master/socks4.txt
https://raw.githubusercontent.com/monosans/proxy-list/main/proxies/socks4.txt
'''