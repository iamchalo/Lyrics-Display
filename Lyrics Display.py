import time

def display_lyrics(lyrics, delay=1.2):
    for line in lyrics:
        print(line)
        time.sleep(delay)

if __name__ == "__main__":
        song_lyrics = [
            "I know we can't keep it together forever",
            "Cause you're crazy sometimes",
            "And I only see you sometimes",
            "Move from me when you're extra",
            "Move from me with the passa",
            "I'm buildin' up a house where they raised me",
            "You move with me, I'll go—, look just",
            "",
            "Don't switch on me, I got big plans",
            "We need to forward to the islands",
            "And get you gold, no spray tans",
            "I need you to stop runnin' back to your ex, he's a wasteman",
            "I wanna know, how come we can never slash and stay friends?",
            "I'm blem for real, I might just say how I feel",
            "I'm blem for real, I might just say how I feel"
        ]

print("===Lyrics Start===")
display_lyrics(song_lyrics)