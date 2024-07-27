from pymongo import MongoClient
from bson import ObjectId
client=MongoClient("take_from_env",tlsAllowInvalidCertificates=True)
print(client)
db=client["ytmanager"]
video_collection=db["videos"]
print(video_collection)

def list_all_videos():
       for video in video_collection.find():
           print(f"ID: {video['_id']}, Name: {video['name']} and Time: {video['time']} ")
def add_video(name,time):
    video_collection.insert_one({"name": name , "time": time})
def updated_video(video_id,new_name,new_time):
     video_collection.update_one(
         {'_id': ObjectId(video_id)},
         {"$set": {"name": new_name,"time": new_time} }
     )
def delete_video(video_id):
    video_collection.delete_one({"_id": ObjectId(video_id)})

def main():
    while True:
        print("\nyoutube manager app")
        print("1. List all videos")
        print("2. Add a video")
        print("3. Update a video")
        print("4. Delete a video")
        print("5. Exit the app")
        choice =input("enter your choice: ")
        
        
        
        if choice == '1':
            list_all_videos()
        elif choice == '2':
            name=input("enter your video name: ")
            time=input("enter video time: ")
            add_video(name,time)
        elif choice == '3':
            video_id=input("enter the video id to update: ")
            name=input("enter your updated video name: ")
            time=input("enter updated video time: ")
            updated_video(video_id,name,time)
        elif choice == '4':
            video_id=input("enter the video id to delete: ")
            delete_video(video_id)
        elif choice == '5':
            break
        
    else:
        print("invalid choice")
        










if __name__=="__main__":
 main()