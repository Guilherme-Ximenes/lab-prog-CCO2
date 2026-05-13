BrunoMars_songs = {
    "Just the Way You Are",
    "Grenade",
    "Runaway Baby",
    "Marry You",
    "Talking to the Moon",
    "It Will Rain",
    "Somewhere in Brooklyn",
    "Young Girls",
    "Locked Out of Heaven",
    "Treasure",
    "Moonshine",
    "When I Was Your Man",
    "Natalie",
    "24K Magic",
    "Thats What I Like",
    "Versace on the Floor",
    "Finesse",
    "Leave the Door Open",
    "Die With a Smile",
    "APT"
}

votes = {}

while True:
    student = input()
    if student.upper() == "FIM DA VOTAÇÃO":
        break
    music_vote = input()
    musics = [song.strip() for song in music_vote.split(", ")]
    for song in musics:
        if song in BrunoMars_songs:
            if song in votes:
                votes[song] += 1
            else:
                votes[song] = 1

sorted_musics = sorted(votes.items())
sorted_votes = sorted(votes.items(), key=lambda x: x[1], reverse=True)

print("As músicas escolhidas para a setlist do Bruninho foram:")
for i, (song, count) in enumerate(sorted_votes, 1):
    print(f"{i}. {song}: {count} voto(s)")
print()
