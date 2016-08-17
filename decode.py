#!/usr/bin/python
# http://www.securitynotes.ro/2014/12/decrypt-lost-password-saved-in-remmina.html

from Crypto.Cipher import DES3
import base64

secret = base64.decodestring('PASTE THE SECRET FOUND AT POINT 1')
key = secret[:24]
iv = secret[24:]

# Encoded Encrypted password
EEpwd = 'PASTE THE PASSWORD FOUND AT POINT 2'

# Decoded Encrypted password
DEpwd = base64.decodestring(EEpwd)

# Decoded Decrypted password
DDpwd = DES3.new(key, DES3.MODE_CBC, iv).decrypt(DEpwd)
print "Decoded (Decrypted ( PWD ) ) : ",DDpwd
