import urllib.request

def download_images():
    num_images = int(input("How many images would you like to download? "))

    url_list = []
    for i in range(num_images):
        url = input(f"Enter the URL for image {i+1}: ")
        url_list.append(url)

    start_count = 1  # Start image naming from "resim1.jpg" 
    for url in url_list:
        urllib.request.urlretrieve(url, "resim" + str(start_count) + ".jpg")
        start_count += 1

if __name__ == "__main__":
    download_images()
