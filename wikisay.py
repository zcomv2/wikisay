import socket
import re
import wikipediaapi

# Configuración del bot
SERVER = "irc.libera.chat"
PORT = 6667
NICK = "Wikisay"
CHANNEL = "#parati"

# Especificar un User-Agent válido
USER_AGENT = "WikisayBot/1.0 (https://your_domain.org/)"

# Inicializar Wikipedia en varios idiomas con el User-Agent correcto
wiki_langs = {
    "es": wikipediaapi.Wikipedia(user_agent=USER_AGENT, language="es"),
    "en": wikipediaapi.Wikipedia(user_agent=USER_AGENT, language="en"),
    "ja": wikipediaapi.Wikipedia(user_agent=USER_AGENT, language="ja")
}

# Conectar al servidor IRC
irc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
irc.connect((SERVER, PORT))
irc.sendall(f"NICK {NICK}\r\n".encode("utf-8"))
irc.sendall(f"USER {NICK} 0 * :{NICK}\r\n".encode("utf-8"))
irc.sendall(f"JOIN {CHANNEL}\r\n".encode("utf-8"))

# Expresiones regulares para detectar comandos solo al **inicio** del mensaje
wiki_patterns = {
    "es": re.compile(r"^!wiki-es (.+)"),
    "en": re.compile(r"^!wiki-en (.+)"),
    "ja": re.compile(r"^!wiki-ja (.+)")
}

# Expresión regular para términos seguros (letras, números y espacios)
safe_input_pattern = re.compile(r'^[\w\s\-\.\(\)]+$', re.UNICODE)

def es_entrada_segura(termino):
    """Verifica que la entrada no contenga caracteres peligrosos."""
    if len(termino) > 100:  # Limitar la longitud a 100 caracteres
        return False
    if not safe_input_pattern.match(termino):  # Solo letras, números y espacios
        return False
    return True

def buscar_wikipedia(termino, idioma):
    """Busca un término en Wikipedia en el idioma seleccionado y devuelve un resumen corto."""
    if not es_entrada_segura(termino):
        return "⚠️ Entrada no válida. Solo letras, números y espacios permitidos."

    page = wiki_langs[idioma].page(termino)
    if not page.exists():
        return f"No encontré información en Wikipedia ({idioma})."

    texto = page.summary[:400]  # Limitar a 400 caracteres
    if len(page.summary) > 400:
        texto += f"... Leer más: {page.fullurl}"
    return texto

try:
    while True:
        # Leer mensajes del servidor
        response = irc.recv(2048).decode("utf-8", errors="ignore")
        print(response)

        # Mantener vivo el bot respondiendo a PING
        if response.startswith("PING"):
            irc.sendall(f"PONG {response.split()[1]}\r\n".encode("utf-8"))

        # Detectar mensajes en el canal
        elif f"PRIVMSG {CHANNEL}" in response:
            message = response.split(f"PRIVMSG {CHANNEL} :", 1)[-1].strip()

            # Buscar en cada idioma (solo si el comando está al inicio)
            for idioma, pattern in wiki_patterns.items():
                match = pattern.match(message)  # SOLO busca si está al inicio
                if match:
                    termino = match.group(1).strip()
                    respuesta = buscar_wikipedia(termino, idioma)
                    irc.sendall(f"PRIVMSG {CHANNEL} : {respuesta} \r\n".encode("utf-8"))
                    break  # Solo procesamos el primer comando encontrado

except KeyboardInterrupt:
    print("Desconectando...")
    irc.close()
