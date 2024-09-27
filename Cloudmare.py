from flask import Flask, render_template, request
import colorama, pyfiglet, socket

app = Flask(__name__)

colorama.init(autoreset=True)

# Colors
rd = colorama.Fore.RED
mag = colorama.Fore.MAGENTA
cv = colorama.Fore.WHITE
gn = colorama.Fore.GREEN
bl = colorama.Fore.LIGHTBLUE_EX
yl = colorama.Fore.LIGHTGREEN_EX

# Function to generate banner
def banner():
    fg = pyfiglet.Figlet(font="small").renderText("RemaxBox Team")
    return bl + fg + rd + "CloudFlare bypasser , Get Real IP of website\n" + mag + "Created By Maximum Radikali"

# Function to get the real IP of subdomains
def get_real_ips(site):
    results = []
    with open("dom.txt", "r") as f:
        for i in f:
            k = i.strip()
            try:
                fs = socket.gethostbyname(k + site)
                results.append(gn + fs + cv)
            except:
                pass
    return results

@app.route('/')
def index():
    return render_template('index.html', banner=banner())

@app.route('/get_ips', methods=['POST'])
def get_ips():
    site = request.form['site']
    if site:
        ip_list = get_real_ips(site)
        return render_template('index.html', banner=banner(), site=site, ip_list=ip_list)
    return render_template('index.html', banner=banner(), error="No URL provided!")

if __name__ == "__main__":
    app.run(debug=True)
