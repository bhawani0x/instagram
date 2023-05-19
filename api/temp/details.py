import instaloader
import time
from datetime import datetime, timezone
import os

# Creating an instance of the Instaloader class
bot = instaloader.Instaloader()


# bot.login(user="Your_username",passwd="Your_password") #Use this code to log-in to your account.


def getBasicInfo():
    profileid = input('Enter the userid of the profile\n')
    try:
        # Loading the profile from an Instagram handle
        profile = instaloader.Profile.from_username(bot.context, profileid)
        print("Username: ", profile.username)
        print("User ID: ", profile.userid)
        print("Number of Posts: ", profile.mediacount)
        print("Followers Count: ", profile.followers)
        print("Following Count: ", profile.followees)
        print("Bio: ", profile.biography)
        print("External URL: ", profile.external_url)
        print('\n')
    except Exception:
        print(f"{profileid} not found" + '\n')


def searchInformation():
    searchitem = input('Enter the search keyword\n')
    # Provide the search query here
    search_results = instaloader.TopSearchResults(bot.context, searchitem)
    print('\n')
    # Iterating over the extracted usernames
    for username in search_results.get_profiles():
        print(username)

    print('\n')
    # Iterating over the extracted hashtags
    for hashtag in search_results.get_hashtags():
        print(hashtag)

    print('\n')

    #download post
    choice = input('do you want to download post of above profile(Y/N) : ')

    # date between
    # start_date = input('Enter the start date in YYYY-MM-DD format: ')
    # end_date = input('Enter the end date in YYYY-MM-DD format: ')
    start_date = "2023-05-01"
    end_date = "2023-05-19"
    #convert date
    start_datetime = datetime.strptime(start_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)
    end_datetime = datetime.strptime(end_date, '%Y-%m-%d').replace(tzinfo=timezone.utc)

    if choice in ['y', 'Y']:
        for username in search_results.get_profiles():
            profile = instaloader.Profile.from_username(bot.context, username.username)
            private = profile.is_private
            if not private:
                posts = profile.get_posts()
                count = 0
                for post in posts:
                    if count >5:
                        exit()
                    post_date = post.date_local.replace(tzinfo=timezone.utc)
                    if start_datetime <= post_date <= end_datetime:
                        bot.download_post(post, target=f"{username}/post")
                        time.sleep(2)
                        print(f"Downloaded post from {post.owner_username}")
                        count =+1
            if private:
                print("private account cant download media")
                print("\n")
                continue
    print('\n')


# def downloadPost():
#     # useerid = input('Enter the userid of the profile\n')
#     # Loading a profile from an Instagram handle
#
#     useerid = "dipesh_bisht121"
#     profile = instaloader.Profile.from_username(bot.context, useerid)
#     if profile.is_private:
#         print("private account cant download media")
#         exit()
#     print("wait for few sec")
#     time.sleep(3)
#     # Retrieving all posts in an object
#     posts = profile.get_posts()
#     # sorted_posts = sorted(posts, key=lambda p: p.likes, reverse=True)
#     count = 0
#     # Iterating and downloading all the individual posts
#     for post in posts:
#         # if count >= 5:
#         #     break
#         try:
#             if post.is_video != True:
#                 bot.download_post(post, target=f"{useerid}/pic")
#                 time.sleep(2)
#                 count += 1
#             if post.is_video:
#                 bot.download_post(post, target=f"{useerid}/video")
#                 time.sleep(2)
#                 count += 1
#         except Exception:
#             continue

def downloadPost():
    useerid = "dipesh_bisht121"
    profile = instaloader.Profile.from_username(bot.context, useerid)
    if profile.is_private:
        print("Private account cannot download media.")
        exit()
    print("Please wait for a few seconds...")
    time.sleep(3)

    posts = profile.get_posts()
    count = 0

    for post in posts:
        try:
            if count > 5:
                break

            if not post.is_video:
                pic_filename = f"{useerid}/pic/my_pic_{count}.jpg"
                os.makedirs(os.path.dirname(pic_filename), exist_ok=True)  # Create the directory if it doesn't exist
                bot.download_post(post, target=pic_filename, filename=f"my_pic_{count}.jpg")
                time.sleep(2)
                count += 1
            if post.is_video:
                video_filename = f"{useerid}/video/my_video_{count}.mp4"
                os.makedirs(os.path.dirname(video_filename), exist_ok=True)  # Create the directory if it doesn't exist
                bot.download_post(post, target=video_filename, filename=f"my_video_{count}.mp4")
                time.sleep(2)
                count += 1
        except Exception:
            continue


if __name__ == '__main__':
    # option = '0'
    # while option != '4':
    #     option = input(
    #         '\nSelect YOur option\n1)Get Profile Info\n2)Search for Top profiles and Hastags\n3)Download Top 5 Profile Posts\n4)Exit\n\nenter your choice :')
    #     if option == '1':
    #         getBasicInfo()
    #     elif option == '2':
    #         searchInformation()
    #     elif option == '3':
    #         downloadPost()
    #     elif option == '4':
    #         exit
    #     else:
    #         print('Wrong input please try again\n')

    # searchInformation()

    # Call the function to download posts
     downloadPost()
