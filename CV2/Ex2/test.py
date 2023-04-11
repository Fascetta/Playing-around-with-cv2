import cv2

# Step 1: Pick objects to classify and download their cover images
# In this example, we'll use 3 book covers: book1.jpg, book2.jpg, book3.jpg

# Step 2: Load the database of book cover images and extract their descriptors
database = []
for i in range(1, 4):
    image_path = f'data/A{i}.jpg'
    image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

    # Create SIFT object
    sift = cv2.SIFT_create()

    # Detect keypoints and compute descriptors
    keypoints, descriptors = sift.detectAndCompute(image, None)

    # Store descriptors in the database
    database.append(descriptors)

# Step 3: Load the test image
test_image_path = 'data/DS2.jpg'
test_image = cv2.imread(test_image_path, cv2.IMREAD_GRAYSCALE)

# Create SIFT object for the test image
sift = cv2.SIFT_create()

# Detect keypoints and compute descriptors for the test image
test_keypoints, test_descriptors = sift.detectAndCompute(test_image, None)

# Step 4: Perform feature matching
matches = []
for i in range(3):
    # Create BFMatcher object
    bf = cv2.BFMatcher(cv2.NORM_L2, crossCheck=True)

    # Match descriptors of the test image with descriptors of each book cover
    book_matches = bf.match(test_descriptors, database[i])

    # Store the matches
    matches.append(book_matches)

# Step 5: Find the best match
max_matches = max(matches, key=lambda x: len(x))
best_match_index = matches.index(max_matches)

# Step 6: Check if the best match is above a threshold
# You can adjust the threshold value to suit your needs
threshold = 10
if len(max_matches) > threshold:
    # Object is classified as the book with the best match
    print(f"The object is classified as book{best_match_index + 1}.")
else:
    # Object is not classified
    print("The object is not classified.")

# Print the number of matches for each book cover
for i in range(3):
    print(f"Number of matches for book{i + 1}: {len(matches[i])}")
