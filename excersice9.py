import win32com.client

names = ["hey harsh i am made by python"]
shoutOut = win32com.client.Dispatch("SAPI.SpVoice")

for name in names:
 shoutOut.Speak(" " + name)
