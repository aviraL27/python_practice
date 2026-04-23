import json
from pathlib import Path

DATA_FILE = Path(__file__).resolve().parent.parent / 'youtube.txt'

def load_data():
    try:
        with open(DATA_FILE, 'r', encoding='utf-8') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_data_helper(videos):
    with open(DATA_FILE, 'w', encoding='utf-8') as file:
        json.dump(videos, file, indent=2)

def list_all_videos(videos):
    if not videos:
        print('No videos found.')
        return

    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']} ({video['time']})")

def add_video(videos):
    name = input("Enter video name: ")
    time = input("Enter video time: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)
    print('Video added successfully.')

def update_video(videos):
    if not videos:
        print('No videos available to update.')
        return

    list_all_videos(videos)
    try:
        index = int(input('Enter video number to update: '))
        if index < 1 or index > len(videos):
            print('Invalid video number.')
            return
    except ValueError:
        print('Please enter a valid number.')
        return

    name = input('Enter new video name: ')
    time = input('Enter new video time: ')
    videos[index - 1] = {'name': name, 'time': time}
    save_data_helper(videos)
    print('Video updated successfully.')

def delete_video(videos):
    if not videos:
        print('No videos available to delete.')
        return

    list_all_videos(videos)
    try:
        index = int(input('Enter video number to delete: '))
        if index < 1 or index > len(videos):
            print('Invalid video number.')
            return
    except ValueError:
        print('Please enter a valid number.')
        return

    deleted_video = videos.pop(index - 1)
    save_data_helper(videos)
    print(f"Deleted: {deleted_video['name']}")

def main():
    videos = load_data()
    while True:
        print('\n Youtube Manager | choose an option')
        print('1. List all youtube videos ')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input('Enter your choice: ')

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_video(videos)
            case '3':
                update_video(videos)
            case '4':
                delete_video(videos)
            case '5':
                print('Goodbye!')
                break
            case _:
                print('Invalid Choice')

if __name__ == "__main__":
    main()
