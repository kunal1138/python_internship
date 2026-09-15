# Task 2: Python Voice Assistant

import datetime
import webbrowser
from urllib.parse import quote_plus

import speech_recognition as sr
import pyttsx3


def speak(text):
    print("Assistant:", text)
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def main():
    recognizer = sr.Recognizer()
    recognizer.operation_timeout = 15

    # Use the computer's default microphone.
    try:
        microphone = sr.Microphone()
        with microphone as source:
            print("Adjusting microphone... Stay quiet for a moment.")
            recognizer.adjust_for_ambient_noise(source, duration=1)
    except (OSError, AttributeError) as error:
        print("Microphone unavailable:", error)
        return

    speak("Hello! I am your Python assistant. How can I help?")

    while True:
        try:
            with microphone as source:
                print("\nListening... Speak now.")
                audio = recognizer.listen(
                    source, timeout=5, phrase_time_limit=8
                )

            # Sends recorded speech to Google's recognition service.
            print("Recognizing...")
            command = recognizer.recognize_google(
                audio, language="en-IN"
            ).lower().strip()

            print("You said:", command)

            if command in ("exit", "quit", "stop", "goodbye"):
                speak("Goodbye!")
                break

            elif "time" in command:
                current_time = datetime.datetime.now().strftime("%I:%M %p")
                speak("The time is " + current_time)

            elif "date" in command:
                today = datetime.datetime.now().strftime("%d %B %Y")
                speak("Today's date is " + today)

            elif "open youtube" in command:
                speak("Opening YouTube.")
                webbrowser.open("https://www.youtube.com")

            elif "open google" in command:
                speak("Opening Google.")
                webbrowser.open("https://www.google.com")

            elif command.startswith("search for "):
                query = command.removeprefix("search for ").strip()
                if query:
                    speak("Searching for " + query)
                    webbrowser.open(
                        "https://www.google.com/search?q=" + quote_plus(query)
                    )
                else:
                    speak("Please say search for, followed by a topic.")

            elif "hello" in command:
                speak("Hello! How can I help you?")

            else:
                speak(
                    "Try asking the time, the date, open Google, "
                    "open YouTube, or search for Python tutorials."
                )

        except sr.WaitTimeoutError:
            continue
        except sr.UnknownValueError:
            speak("I could not understand. Please try again.")
        except sr.RequestError:
            speak("Speech recognition is unavailable. Check your internet.")
            break
        except OSError as error:
            print("Microphone error:", error)
            break


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nAssistant stopped.")