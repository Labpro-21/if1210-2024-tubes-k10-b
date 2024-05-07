def encrypt(s: str, key: int) -> str:
    text: str = ""
    for i in range(len(s)):
        if ord('A') <= ord(s[i]) <= ord('Z'):
            text += chr(((ord(s[i]) - ord('A') + key) % 26) + ord('A'))
        elif ord('a') <= ord(s[i]) <= ord('z'):
            text += chr(((ord(s[i]) - ord('a') + key) % 26) + ord('a'))
        else:
            text += s[i]
    return text


def decrypt(s: str, key: int) -> str:
    text: str = ""
    for i in range(len(s)):
        if ord('A') <= ord(s[i]) <= ord('Z'):
            text += chr(((ord(s[i]) - ord('A') - key) % 26) + ord('A'))
        elif ord('a') <= ord(s[i]) <= ord('z'):
            text += chr(((ord(s[i]) - ord('a') - key) % 26) + ord('a'))
        else:
            text += s[i]
    return text
