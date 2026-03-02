def manage_playlist(current_playlist, add_songs, import_playlist, banned_songs):
    """
    Manages a music playlist with adds, imports, and removals.
    
    Args:
        current_playlist: Set of currently in playlist
        add_songs: List of songs to add individually
        import_playlist: Set of songs to import from Spotify
        banned_songs: Set of songs to remove
    
    Returns:
        int: Count of final songs in playlist
    """

    MAX_SIZE = 6

    # Step 1: Add songs individually
    for song in add_songs:
        current_playlist.add(song)

    # Step 2: Import entire playlist at once
    current_playlist.update(import_playlist)

    # Step 3: Remove all banned songs at once
    current_playlist.difference_update(banned_songs)

    # Step 4: If playlist too long, randomly remove until size == 6
    while len(current_playlist) > MAX_SIZE:
        current_playlist.pop()  # removes arbitrary (random) item from set

    return len(current_playlist)
    pass
