# Implementation of circular queue using doubly circular linkedlist 
# Develop python program for songs player application using 
# concept of circular queue and DLL
# 1. addSong - allow adding new song to the playlist. Check queue full status
# 2. playNextSong -Retrieve and play the next song in the playlist . After the last song is played, the playlist should continue from the first song
# 3. playPreviousSong - Retrieve and play the next song in the playlist
# 4. removeSong - Remove songs from the playlist. check queue empty
# 5. viewCurrentSong - View the current song details

from playsound import playsound

playsound('/path/to/sound.mp3')


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class SongPlayer:
    def __init__(self, max_size=10):
        self.head = None
        self.tail = None
        self.current = None
        self.size = 0
        self.max_size = max_size

    def is_full(self):
        return self.size >= self.max_size

    def is_empty(self):
        return self.size == 0

    def addSong(self, song_name):
        if self.is_full():
            print("Playlist is full. Cannot add more songs.")
            return

        new_node = Node(song_name)

        if self.head is None:
            self.head = self.tail = self.current = new_node
            new_node.next = new_node.prev = new_node  
        else:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.size += 1
        print(f"Song '{song_name}' added to the playlist.")

    def playNextSong(self):
        if self.is_empty():
            print("Playlist is empty. No song to play.")
            return

        self.current = self.current.next
        print(f"Now playing: {self.current.data}")

    def playPreviousSong(self):
        if self.is_empty():
            print("Playlist is empty. No song to play.")
            return

        self.current = self.current.prev
        print(f"Now playing: {self.current.data}")

    def removeSong(self, song_name):
        if self.is_empty():
            print("Playlist is empty. No song to remove.")
            return

        temp = self.head
        found = False

        for _ in range(self.size):
            if temp.data == song_name:
                found = True
                break
            temp = temp.next

        if not found:
            print(f"Song '{song_name}' not found in the playlist.")
            return

        if self.size == 1:
            self.head = self.tail = self.current = None
        else:
            temp.prev.next = temp.next
            temp.next.prev = temp.prev

            if temp == self.head:
                self.head = temp.next
            if temp == self.tail:
                self.tail = temp.prev
            if temp == self.current:
                self.current = temp.next  

        self.size -= 1
        print(f"Song '{song_name}' removed from the playlist.")

    def viewCurrentSong(self):
        if self.is_empty():
            print("No current song. Playlist is empty.")
        else:
            print(f"Currently playing: {self.current.data}")

    def showPlaylist(self):
        if self.is_empty():
            print("Playlist is empty.")
            return

        print("Playlist:")
        temp = self.head
        for _ in range(self.size):
            marker = " <-- Current Song" if temp == self.current else ""
            print(f"- {temp.data}{marker}")
            temp = temp.next


if __name__ == "__main__":
    player = SongPlayer(max_size=5)

    print("Welcome to music player")
    while(True):
        print("1.ADD SONG \n2.PLAY NEXT SONG \n3.PLAY PREVIOUS SONG \n4.REMOVE SONG \n5.VIEW CURRENT SONG \n6.EXIT")
        operation = int(input("enter the no. of operation you want to preform: "))

        if(operation == 1):
            songName = input("enter the name of the song: ")
            player.addSong(songName)
        elif(operation == 2):
            player.playNextSong()
        elif(operation == 3):
            player.playPreviousSong()
        elif(operation == 4):
            removeSongName = input("Enter the name of the song you want to remove: ")
            player.removeSong(removeSongName)
        elif(operation == 5):
            player.viewCurrentSong()
        elif(operation == 6):
            break
        else:
            print("Enter Correct Number")




