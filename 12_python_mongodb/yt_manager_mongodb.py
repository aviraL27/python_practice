import os

from bson import ObjectId
from bson.errors import InvalidId
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

MONGODB_URI = os.getenv("MONGODB_URI")
if not MONGODB_URI:
    raise RuntimeError("MONGODB_URI is not set. Add it to your .env file.")

client = MongoClient(MONGODB_URI)

db = client['ytmanager']
video_collection = db['videos']

def add_video(name,time):
    video_collection.insert_one({'name': name.strip(), "time": time.strip()})

def list_videos():
    videos = list(video_collection.find())
    if not videos:
        print('No videos found.')
        return

    for video in videos:
        print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']}")

def update_video(video_id,new_name,new_time):
    try:
        object_id = ObjectId(video_id.strip())
    except InvalidId:
        print('Invalid video ID format.')
        return

    result = video_collection.update_one(
        {'_id': object_id},
        {'$set': {"name": new_name.strip(), "time": new_time.strip()}}
    )

    if result.matched_count == 0:
        print('No video found with that ID.')
    else:
        print('Video updated successfully.')

def delete_video(video_id):
    try:
        object_id = ObjectId(video_id.strip())
    except InvalidId:
        print('Invalid video ID format.')
        return

    result = video_collection.delete_one({'_id': object_id})
    if result.deleted_count == 0:
        print('No video found with that ID.')
    else:
        print('Video deleted successfully.')

def main():
    while True:
        print('\n youtube manager app')
        print('1. List all youtube videos ')
        print('2. Add a youtube video')
        print('3. Update a youtube video details')
        print('4. Delete a youtube video')
        print('5. Exit the app')
        choice = input('Enter your choice: ').strip()

        if choice == '1':
            list_videos()
        elif choice =='2':
            name = input('Enter the video name: ')
            time = input('Enter the video time: ')
            add_video(name,time)
        elif choice =='3':
            video_id = input('Enter the video id: ')
            name = input('Enter the updated video name: ')
            time = input('Enter the updated video time: ')
            update_video(video_id, name,time)
        elif choice =='4':
            video_id = input('Enter the video id: ')
            delete_video(video_id)
        elif choice == '5':
            break
        else:
            print('invalid choice')

if __name__ == '__main__':
    try:
        main()
    finally:
        client.close()